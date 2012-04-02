

class Symmetric_matrix(object):
    matrix=None
    size=None
    
    
    
    def __init__(self,size): 
        def zero(m,n):
    # Create zero matrix
            new_matrix = [[0 for row in range(n)] for col in range(m)]
            return new_matrix
        self.matrix=zero(size,size)
        self.size=size
        
    def set_diag(self,diag):
        "this method sets the diagonal elements of the matrix from the list diag (length size)"
        for count,element in enumerate(diag):
            matrix[count][count]=element
    
    def set_element(self,row,col,element):
        "this method sets the element at (row,col) to a given element"
        self.matrix[col][row]=element       
        self.matrix[row][col]=element
    
    def get_element(self,row,col):
        return self.matrix[col][row]
    
    
    def __repr__(self):
        print self.matrix
        
    
    def convert_to_list(self):
        "this method converts the matrix into a list representation."
        list=[]
        for count, col in enumerate(self.matrix):
            list+=col[count:]
        return list
    
    def convert_to_list_diag_free(self):
        "This method is the same as above but omits the diagonal elements."
        list=[]     
        for count, col in enumerate(self.matrix):
            list+=col[count+1:]
        return list  
    
    def set_list_in_matrix(self,list):
        "given a list, this method puts the elements in the list into the matrix, going down columns."
        if len(list)!=self.size*(self.size+1)/2:
            print "Error: list not appropriate size."
        else:
            tracker=0
            for count in range(self.size):
                for num in range(self.size-count):
                  self.set_element(count+num, count,list[tracker])
                  tracker+=1
                
    def set_list_in_matrix_diag_free(self,list):
        if len(list)!=self.size*(self.size-1)/2:
            print "Error: list not appropriate size."
        else:
            tracker=0
            for count in range(self.size-1):
                for num in range(1,self.size-count):
                  self.set_element(count+num, count,list[tracker])
                  tracker+=1

                  
                                
                    
                    
                
            
            
            
            

        