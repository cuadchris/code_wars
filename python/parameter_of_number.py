# DESCRIPTION:

# Let's define a parameter of number n as the least common multiple (LCM) of the sum of 
# its digits and their product.

# Calculate the parameter of the given number n.

# Input/Output
# [input] integer n

# A positive integer. It is guaranteed that no zero appears in n.

# [output] an integer

# The parameter of the given number.

# Example:
# For n = 22, the output should be 4.

# Both the sum and the product of digits equal 4, and LCM(4, 4) = 4.

# For n = 1234, the output should be 120.

# 1+2+3+4=10 and 1*2*3*4=24, LCM(10,24)=120

from functools import reduce
def parameter(n):
    
    # To loop through each digit in a number, you first need to convert it to a string,
    # then you can loop through this string, separating each character and converting it
    # back to int. So essentially, 1234 -> '1234' -> [1, 2, 3, 4]
    n_list = [int(x) for x in str(n)]
    
    # Get the sum of this list, and the product
    add = reduce(lambda x, y: x + y, n_list)
    mult = reduce(lambda x, y: x * y, n_list)
    
    # Extra variables just for clarity.
    LCM = old_mult = mult
    
    # So basically, this while loop will continue increasing the LCM until modulus
    # returns 0, which gives you the LCM between mult and add.
    while LCM % add:
        LCM += old_mult
        
    return LCM