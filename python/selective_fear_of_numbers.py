'''
https://www.codewars.com/kata/55b1fd84a24ad00b32000075/python

DESCRIPTION:

I've got a crazy mental illness. I dislike numbers a lot. But it's a little complicated:
The number I'm afraid of depends on which day of the week it is... This is a concrete 
description of my mental illness:

Monday --> 12

Tuesday --> numbers greater than 95

Wednesday --> 34

Thursday --> 0

Friday --> numbers divisible by 2

Saturday --> 56

Sunday --> 666 or -666

Write a function which takes a string (day of the week) and an integer (number to be tested)
so it tells the doctor if I'm afraid or not. (return a boolean)
'''

def am_I_afraid(day,num):
    
    if day == 'Monday' and num == 12: return True
    if day == 'Tuesday' and num > 95: return True
    if day == 'Wednesday' and num == 34: return True
    if day == 'Thursday' and num == 0: return True
    if day == 'Friday' and not num % 2: return True
    if day == 'Saturday' and num == 56: return True
    if day == 'Sunday' and abs(num) == 666: return True

    return False

# Silly kata, but I was unaware you could do this with dictionaries.

def am_I_afraid(day,num):

    return {
        'Monday':  num == 12,
        'Tuesday': num > 95,
        'Wednesday': num == 34,
        'Thursday': num == 0,
        'Friday': num % 2 == 0,
        'Saturday': num ==  56,
        'Sunday': abs(num) == 666,
    }[day]
