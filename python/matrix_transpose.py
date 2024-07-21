'''
DESCRIPTION:

Write a function that outputs the transpose of a matrix - a new matrix where the columns and rows of the
original are swapped.

For example, the transpose of:

| 1 2 3 |
| 4 5 6 |
is

| 1 4 |
| 2 5 |
| 3 6 |

The input to your function will be an array of matrix rows. You can assume that each row has the same
length, and that the height and width of the matrix are both positive.
'''

def transpose(matrix):
    
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    transposed = [[None] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed