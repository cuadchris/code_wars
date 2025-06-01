'''
https://www.codewars.com/kata/5572392fee5b0180480001ae

DESCRIPTION:

Having two standards for a keypad layout is inconvenient!

Computer keypad's layout:
7 8 9  \n
4 5 6  \n
1 2 3  \n
  0 \n

Cell phone keypad's layout:
1 2 3\n 
4 5 6\n  
7 8 9\n  
  0\n

Solve the horror of unstandardized keypads by providing a function that converts computer input to a number as if it was typed on a phone.

Example:
"789" -> "123"

Notes:
You get a string with numbers only
'''

# Cool 1-liner
def computer_to_phone(numbers):
    return numbers.translate(str.maketrans('123789', '789123'))

# Different way to break down what's going on.
def computer_to_phone(numbers):
    
    res = []
    
    dict = {
        "7": "1",
        "8": "2",
        "9": "3",
        "1": "7",
        "2": "8",
        "3": "9"
    }
    
    for i in numbers:
        if i in dict:
            res.append(dict[i])
        else:
            res.append(i)
            
    return "".join(res)
