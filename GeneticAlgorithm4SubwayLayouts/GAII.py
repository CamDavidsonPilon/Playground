#
#This GA program finds the most efficient subway system given the position (relative to each other using distances) of N 
#stations. The program returns the adjaceny matrix of the graph.
#

import random
import Symmetric_matrix_class
import Graph_functions
import copy




class Individual(Symmetric_matrix_class.Symmetric_matrix):
    alleles=(0,1)
    score=None
    min_path_matrix=None

    
    def __init__(self,size,chromosome=None):
        Symmetric_matrix_class.Symmetric_matrix.__init__(self,size)
        if chromosome==None:
            self.chromosome=self.make_chromosome()
        else:
            self.chromosome=chromosome
        self.set_list_in_matrix_diag_free(self.chromosome)
        self.chromosome_matrix=self.matrix

            
    def make_chromosome(self):
        "I've decided to make the chromosome a list, which I can easily convert back and forth between list and matrix using methods."
        return [random.choice(self.alleles) for gene in range(self.size*(self.size-1)/2)]
    
    def fix_connectedness(self):
        "this function is called whenever the chromosome is changed, to ensure the graph is connected."
        check=self.check_connectedness()
        while check[0]==False:
            #print "="*30
            #print "fixed chromosome"
            #self.__repr__()
            #print "at point (%d,%d)" %(check[1],check[2])
            #print "="*30
            self.set_gene(1, row=check[1], col=check[2])
            check=self.check_connectedness()
                
    def check_connectedness(self):
        "Change parameter 1000 to something larger then size of matrix"
        self.min_path_matrix=Graph_functions.floyds_algorithm(self.chromosome_matrix)
        for col in range(self.size):
            for row in range(col+1,self.size):
                if self.min_path_matrix[col][row]==1000:
                    return [False,row,col]
        return [True]        
               
    def evaluate(self,enviroment):
        self.fix_connectedness()
        self.score=0
        for col in range(self.size):
            for row in range(col+1,self.size):
                min=self.min_path_matrix[col][row]
                self.score+=enviroment.discount_factor**(min-1)*enviroment.traffic_matrix.get_element(row,col) 
                if self.chromosome_matrix[col][row]==1:
                    self.score-=enviroment.distance_matrix.get_element(row,col)       

    def set_gene(self,new_gene,position=None,row=None,col=None):
        "either position!=None OR (not inclusive) row!=None, col!=None"
        if position!=None:
            self.chromosome[position]=new_gene
            self.set_list_in_matrix_diag_free(self.chromosome)
        elif row!=None and col!=None:
            self.set_element(row,col,new_gene)
            self.chromosome=self.convert_to_list_diag_free()    
        else:
            print "Error: empty location in set_gene()."    
            
    def _mutate(self,position):
        "mutates an individual using-. Then connects the graph, if nessecary."
        self.alternate_mut(position)
        
    def alternate_mut(self,pos):
        "puts the allele in current position of chromosome"
        self.set_gene(1-self.chromosome[pos], position=pos)
        
    def crossover(self, other):
        "crossovers two individuals using-"
        return self._twopoint(other)
    
    def _twopoint(self, other):
        "creates offspring via two-point crossover between mates."
        left, right = self._pickpivots()
        def mate(p0, p1):
            chromosome = p0.chromosome[:]
            chromosome[left:right] = p1.chromosome[left:right]
            child = p0.__class__(self.size,chromosome)
            return child
        return mate(self, other), mate(other, self)    
    
    def _pickpivots(self):
        left = random.randrange(1, self.size-2)
        right = random.randrange(left, self.size-1)
        return left, right
    
    def _copy(self):
        twin=self.__class__(self.size,self.chromosome[:])
        twin.score=self.score
        return twin
    
    def __repr__(self):
        "returns string representation of self"  
        print "<chromosome = %s : score = %s>" %(self.chromosome, self.score)
                
class Enviroment(object):
    def __init__(self, crossover_rate, max_generations, traffic_matrix, distance_matrix,discount_factor, mutation_rate, population_size, population=None):
        self.crossover_rate=crossover_rate
        self.max_generations=max_generations
        self.mutation_rate=mutation_rate
        self.population_size=population_size
        self.traffic_matrix=traffic_matrix
        self.distance_matrix=distance_matrix
        self.no_stations=len(self.distance_matrix.matrix)
        self.discount_factor=discount_factor
        self.generation=0
        self.freq_vector=[0]*self.population_size
        self.best_score=0
        self.best_individual=None
        self.avg_fitness=0
        if population==None:
            self.population=self.make_population()
            print "population created"
        else:
            self.population=population
    
    def make_population(self):
        return [Individual(self.no_stations) for individual in range(self.population_size)]
    
    
    def _run(self):
      while self.generation<self.max_generations:
        self.evaluate()  
        self.report()
        self.select()
        self.generation+=1    
      self.evaluate()  
      print "="*70
      print "="*70
      print "generation", self.generation
      print "population:"
      self.print_population() 
      print "best:",self.best_score
      self.best_individual.__repr__()
      print self.best_individual.matrix   
    
    def evaluate(self):
        total_score=0
        for individual in self.population:
            individual.evaluate(self)
            total_score+=individual.score
            if individual.score>self.best_score:
                self.best_score=individual.score
                self.best_individual=individual._copy()
        self.avg_fitness=float(total_score)/self.population_size        
        for count,ind in enumerate(self.population):
            self.freq_vector[count]=float(ind.score)/total_score
    
    def select(self):
        next_population=[self.best_individual._copy()]
        while len(next_population)<self.population_size:
            mate1=self.roulette_wheel()
            if random.random()<self.crossover_rate:
                mate2=self.roulette_wheel()
                offspring=mate1.crossover(mate2)
            else:
                offspring=[mate1._copy()]
            for ind in offspring:
                self.mutate(ind)
                next_population.append(ind)
        self.population=next_population[0:self.population_size]       
        
    def mutate(self,ind):
        for count in range(len(ind.chromosome)):
            if random.random()<self.mutation_rate:
                ind._mutate(count)
                
            
        
    def roulette_wheel(self):
        "this chooses a individual from the population based on the roulette wheel method."
        ind=0
        sum=self.freq_vector[ind]
        r_uniform=random.random()
        while sum<r_uniform:
            ind+=1
            sum+=self.freq_vector[ind]
        return self.population[ind]

        
    def print_population(self):
        for individual in self.population:
            individual.__repr__()
            
    
    def report(self):
        print "="*50
        print "generation: ", self.generation
        print "average fitness:", self.avg_fitness
        print "best score:",self.best_score
        print "best individual: ", 
        self.best_individual.__repr__()
        print "="*50
                        
        
        
                      
    def roulette_wheel(self):
        "this chooses a individual from the population based on the roulette wheel method."
        ind=0
        sum=self.freq_vector[ind]
        r_uniform=random.random()
        while sum<r_uniform:
            ind+=1
            sum+=self.freq_vector[ind]
        return self.population[ind]
    
                    


     
