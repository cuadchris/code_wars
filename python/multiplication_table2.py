'''
https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/python

DESCRIPTION:

Your task, is to create N×N multiplication table, of size provided in parameter.

For example, when given size is 3:

1 2 3
2 4 6
3 6 9

For the given example, the return value should be:

[[1,2,3],[2,4,6],[3,6,9]]
'''

# initial solution

def multiplication_table(size):
    table = []
    for i in range(1, size + 1):
        row = []
        for j in range(1, size + 1):
            row.append(i * j)
        table.append(row)
    return table

# optimized. less calculations


def multiplication_table(size):
    # Initialize the table with zeros
    table = [[0] * size for _ in range(size)]

    for i in range(1, size + 1):
        for j in range(i, size + 1):
            table[i - 1][j - 1] = table[j - 1][i - 1] = i * j

    return table