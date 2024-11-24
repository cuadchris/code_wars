'''
https://www.codewars.com/kata/583df40bf30065fa9900010c/python

DESCRIPTION:

Write a function that takes as parameters an array (arr) and 2 integers (x and y). The 
function should return the mean between the mean of the the first x elements of the 
array and the mean of the last y elements of the array.

The mean should be computed if both x and y have values higher than 1 but less or equal 
to the array's length. Otherwise the function should return -1.

Examples
[1, 3, 2, 4], 2, 3 => should return 2.5
because: the mean of the the first 2 elements of the array is (1+3)/2=2 and the mean of 
the last 3 elements of the array is (4+2+3)/3=3 so the mean of those 2 means is (2+3)/2=2.5.

[1, 3, 2, 4], 1, 2 => should return -1
because x is not higher than 1.

[1, 3, 2, 4], 2, 8 => should return -1
because 8 is higher than the array's length.
'''

def get_mean(arr,x,y):
    
    arr_length = len(arr)
    
    if x <= 1 or y <= 1 or x > arr_length or y > arr_length:
        return -1
    
    return (sum(arr[:x])/x + sum(arr[-y:])/y) / 2