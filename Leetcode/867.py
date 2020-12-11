'''
867. Transpose Matrix

Given a matrix A, return the transpose of A.
The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
'''

def transpose(A):
    row = len(A[0])
    column = len(A)
    B = A.copy()
    for i in range(row):
        for j in range(column):
            B[j][i] = A[i][j]
    return B
A= [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(A))


