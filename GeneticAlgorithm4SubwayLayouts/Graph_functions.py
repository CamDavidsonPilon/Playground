import copy


def zero(m,n):
    # Create zero matrix
    new_matrix = [[0 for row in range(n)] for col in range(m)]
    return new_matrix

def mult(matrix1,matrix2):
    # Matrix multiplication
    if len(matrix1[0]) != len(matrix2):
        # Check matrix dimensions
        print 'Matrices must be m*n and n*p to multiply!'
    else:
        # Multiply if correct dimensions
        new_matrix = zero(len(matrix1),len(matrix2[0]))
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    new_matrix[i][j] += matrix1[i][k]*matrix2[k][j]
        return new_matrix 
 
 #
 #Floyd's algorithm takes an adjacency matrix M and returns a matrix, S, s.t. (S)_ij is the shortest path between i and j.
 #
def floyds_algorithm(M):
    S=copy.deepcopy(M)
    size=len(M)
    for col in range(size):
        for row in range(size):
            if S[col][row]==0 and col!=row:
                S[col][row]=1000
    for k in range(size):
        for i in range(size):
            for j in range(size):
                S[j][i]=min(S[j][i],S[k][i]+S[j][k])
    return S      

def matrix_to_power_of(n,matrix):
    if n==1:
        return matrix
    else:
        product=mult(matrix,matrix_to_power_of(n-1, matrix))
    return product 

    
    