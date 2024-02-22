'''
https://www.codewars.com/kata/5f6d533e1475f30001e47514

DESCRIPTION:

You are given a list of unique integers arr, and two integers a and b. Your task is to find out whether or not
a and b appear consecutively in arr, and return a boolean value (True if a and b are consecutive, False otherwise).

It is guaranteed that a and b are both present in arr.
'''

def consecutive(arr, a, b):
        
    for i in range(len(arr) - 1):
        if arr[i] == a or arr[i] == b:
            if arr[i + 1] == a or arr[i + 1] == b:
                return True
            
    return False