myList=[[1, 2, 3, 4, 5], [12, 13, 23], [10, 20, 30], [11, 22, 33], [12, 24, 36]]
l2 = []  #l2 is empty, declared to store transpose of above list
mat = [ [ 1, 3, 5 ], [ 3, 2, 4 ], [ 5, 4, 1 ] ]

class Matrix2Dim:
    attribute_1: (5, 5)
    attribute_2: [[1, 2, 3, 4, 5], [12, 13, 23,24,25], [10, 20, 30,40,50], [11, 22, 33, 44, 55], [12, 24, 36, 38, 50]]

# Fills transpose of mat[N][N] in tr[N][N]
def transpose(mat, tr, N):
    for i in range(N):
        for j in range(N):
            tr[i][j] = mat[j][i]


# Returns true if mat[N][N] is symmetric, else false
def isSymmetric(mat, N):
    tr = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]
    transpose(mat, tr, N)
    for i in range(N):
        for j in range(N):
            if (mat[i][j] != tr[i][j]):
                return False
    return True
