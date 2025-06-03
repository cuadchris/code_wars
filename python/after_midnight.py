'''
https://www.codewars.com/kata/56fac4cfda8ca6ec0f001746/python

DESCRIPTION:

Write a function that takes a negative or positive integer, which represents the number 
of minutes before (-) or after (+) Sunday midnight, and returns the current day of the 
week and the current time in 24hr format ('hh:mm') as a string.

Examples:
       0  =>  should return 'Sunday 00:00'
      -3  =>  should return 'Saturday 23:57'
      45  =>  should return 'Sunday 00:45'
     759  =>  should return 'Sunday 12:39'
    1236  =>  should return 'Sunday 20:36'
    1447  =>  should return 'Monday 00:07'
    7832  =>  should return 'Friday 10:32'
   18876  =>  should return 'Saturday 02:36'
  259180  =>  should return 'Thursday 23:40' 
 -349000  =>  should return 'Tuesday 15:20'
 '''

def day_and_time(mins):
    
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    
    # I love using modulus to wrap around arrays. So cool.
    day = days[mins // (60 * 24) % len(days)]
    
    # Just discovered the zfill function. Depending on the value you pass in, it'll add
    # '0's to fill in the gaps. So '0' becomes '00', and 2 would become '02'. Very nifty.
    hour = str(mins // 60 % 24).zfill(2)
    
    seconds = str(mins % 60).zfill(2)
    
    return f'{day} {hour}:{seconds}'

# Broke this down for clarity; took a lot to not shove everything into a two-liner, haha
