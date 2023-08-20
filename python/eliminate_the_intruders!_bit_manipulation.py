# https://www.codewars.com/kata/5a0d38c9697598b67a000041/python

# You are given a string representing a number in binary. Your task is to delete all the 
# unset bits in this string and return the corresponding number (after keeping only the '1's).

# In practice, you should implement this function:
# def eliminate_unset_bits(number):

# Examples:
# eliminate_unset_bits("11010101010101") ->  255 (= 11111111)
# eliminate_unset_bits("111") ->  7
# eliminate_unset_bits("1000000") -> 1
# eliminate_unset_bits("000") -> 0

def eliminate_unset_bits(number):
    
    try: return int(number.replace('0', ''), 2)
    except: return 0