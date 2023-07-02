# https://www.codewars.com/kata/5596700a386158e3aa000011/python

# DESCRIPTION:

# Given two numbers m and n, such that 0 ≤ m ≤ n :

# convert all numbers from m to n (inclusive) to binary
# sum them as if they were in base 10
# convert the result to binary
# return as a string
# Example
# 1, 4  -->  1111010

# because:
#     1  // 1 in binary is 1
# +  10  // 2 in binary is 10
# +  11  // 3 in binary is 11
# + 100  // 4 in binary is 100
# -----
#   122  // 122 in binary is 1111010

def binary_pyramid(m,n):

    return bin(sum(int(bin(x)[2:]) for x in range(m, n + 1)))[2:]