# file full of linear algebra operations

#####################################################
# DOT PRODUCT OF TWO VECTORS
#####################################################
def dotProduct(a, b):
    if len(a) != len(b):
        print("Vectors must be the same size!")
        return
    res = 0
    for i in range(0, len(a)):
        res += a[i]*b[i]
    return res

#####################################################
# CROSS PRODUCT OF TWO VECTORS (3 elements)
#####################################################
def crossProduct(a, b):
    if len(a) != len(b):
        print("Vectors must be the same size!")
        return
    # since lengths are the same only check one
    if len(a) != 3:
        print("Vectors must be only 3 elements!")
        return
    # initialize array to be returned
    res = [0]*len(a)
    res[0] = (a[1]*b[2]) - (a[2]*b[1])
    res[1] = (-1)*( (a[0]*b[2]) - (a[2]*b[0]) )
    res[2] = (a[0]*b[1]) - (a[1]*b[0])
    return res

#####################################################
# ADD TWO MATRICIES TOGETER
# Each row of the matrix must be of the same length
#####################################################
def add(A, B):
    if checkIfSameSize(A, B) == 0:
        print("Matricies must be of same size!")
        return
    rows = len(A)
    cols = len(A[0])
    Res = [[0 for i in range(rows)] for j in range(cols)]
    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            Res[i][j] = A[i][j] + B[i][j]
    return Res

#####################################################
# TRANSPOSE A MATRIX
#####################################################
def transpose(A):
    # make sure all rows are same length
    if checkRows1(A) == 0:
        print("All rows must be the same length!")
        return
    rows = len(A)
    cols = len(A[0])
    # initialize a 2d array of size of transpose
    Res = [[0 for i in range(rows)] for j in range(cols)]
    for i in range(0, len(Res)):
        for j in range(0, len(Res[i])):
            Res[i][j] = A[j][i]
    return Res

#####################################################
# MULTIPLY TWO MATRICIES
#####################################################
# helper function for 'multiply'
def mult(A, b):
    res = [0]*len(b) # create a vector to be returned
    add = 0          # used to store multiplication results
    # outer loop iterates over ROWS
    for i in range(0, len(A)):
        # iterate across the row
        for j in range(0, len(A[i])):
            add += b[j] * A[i][j]
        res[i] = add
        add = 0
    return res

def multiply(A, B):

    # make sure each matrix is rectangular in shape
    if checkRows1(A) == 0:
        print("All rows of A must be the same length!")
        return
    if checkRows1(B) == 0:
        print("All rows of B must be the same length!")
        return
    # make sure matricies can be multiplied by each other
    # row length of A must be equal to column length of B
    if len(A[0]) != len(B):
        printf("Matricies cannot be multiplied together. Row length of A must be equal to column length of B!")
        return
    rows = len(B[0])
    cols = len(A)
    Res = [[0 for i in range(rows)] for j in range(cols)]
    # here we will fill the rows with the result from the helper function 'mult'
    v = [0]*len(B) # will be the vector to pass to the helper function
    for i in range(0, len(B[0])):
        # create the vector to be passed to helper function
        for j in range(0, len(B)):
            v[j] = B[j][i]
        # pass matrix and vector v to 'mult'
        addCol = mult(A, v)
        #print(addCol)
        # add this column to the matrix 'Res'
        for k in range(0, len(A)):
            Res[k][i] = addCol[k]
    return Res

#####################################################
# CHECKS IF MATRICIES ARE OF IDENTICAL SIZE
#####################################################
def checkIfSameSize(A, B):
    if len(A) != len(B):
        return 0
    if checkRows2(A, B) == 0:
            return 0
    return 1


#####################################################
# CHECKS IF MATRICIES' ROWS ARE OF IDENTICAL SIZE
#####################################################
def checkRows2(A, B):
    for i in range(0, len(A)):
        if len(A[i]) != len(B[i]):
            return 0
    return 1

#####################################################
# CHECKS IF MATRIX ROWS ARE OF IDENTICAL SIZE
#####################################################
def checkRows1(A):
    for i in range(0, (len(A)-1)):
        if len(A[i]) != len(A[i+1]):
            return 0
    return 1

#####################################################
# print the matrix out in a 'matrix' form
#####################################################
def printMatrixForm(A):
    for x in A:
        print(x)

#####################################################
##################### MAIN ##########################
# Below are some matricies and some tests
A = [
[9, 8, 7],
[4, 5, 6],
[3, 2, 1]
]
B = [
[0, 0, 0],
[1, 1, 1],
[2, 2, 2]
]

C = [
[1, 2, 3],
[6, 7, 2]
]

D = [
[1, 2, 3, 4],
[12, 4, 5, 9],
[12, 13, 14, 2]
]


E = [
[1, 2],
[3, 4],
[5, 6]
]

#v1 = [3, 4, 1]
#v2 = [5, 1, 3]
#print(dotProduct(v1, v2))
#print(crossProduct(v1, v2))

print(add(A, B))
print(add(A, C))
print(transpose(E))
print(transpose(D))
print(multiply(A, B))
printMatrixForm(multiply(A,D))
