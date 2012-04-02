import Symmetric_matrix_class
import Graph_functions
import copy
import GAII
import random



def random_list(size,lower,upper):
    traffic=[]
    for count in range(size*(size-1)/2):
        traffic+=[random.randint(lower,upper)]
    return traffic

    
N=12
T=Symmetric_matrix_class.Symmetric_matrix(N)
D=Symmetric_matrix_class.Symmetric_matrix(N)
Tlist=[164, 121, 155, 198, 173, 162, 68, 160, 65, 1000, 200, 161, 185, 97, 98, 73, 53, 153, 67, 186, 114, 152, 144, 109, 150, 91, 172, 158, 56, 108, 126, 141, 95, 141, 73, 96, 97, 143, 125, 161, 84, 194, 51, 60, 115, 103, 153, 69, 81, 161, 199, 164, 60, 122, 164, 132, 107, 162, 124, 140, 173, 154, 86, 125, 191, 137]
Dlist=[36, 44, 50, 56, 26, 31, 31, 35, 60, 21, 100, 31, 38, 28, 56, 49, 34, 35, 24, 38, 54, 55, 32, 25, 21, 59, 51, 44, 45, 39, 25, 46, 30, 38, 25, 41, 43, 22, 24, 46, 23, 31, 54, 57, 34, 24, 40, 33, 50, 25, 43, 22, 59, 32, 52, 32, 37, 38, 27, 59, 44, 35, 42, 36, 32, 25]
T.set_list_in_matrix_diag_free(Tlist)
D.set_list_in_matrix_diag_free(Dlist)
env=GAII.Enviroment(0.8,10000,T,D,0.6,0.04,25)
env._run()



