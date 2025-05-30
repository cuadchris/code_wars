'''
https://www.codewars.com/kata/64cac86333ab6a14f70c6fb6/python

DESCRIPTION:

You will be given an array of events, which are represented by strings. The strings are 
dates in HH:MM:SS format.

It is known that all events are recorded in chronological order and two events can't 
occur in the same second.

Return the minimum number of days during which the log is written.

Example:

Input -> ["00:00:00", "00:01:11", "02:15:59", "23:59:58", "23:59:59"]
Output -> 1

Input -> ["12:12:12"]
Output -> 1

Input -> ["12:00:00", "23:59:59", "00:00:00"]
Output -> 2

Input -> []
Output -> 0
'''

def check_logs(log):

    if len(log) == 1:
        return 1
    if len(log) == 0:
        return 0
    
    days = 1
    
    nums = [int("".join(x for x in i.split(":"))) for i in log]
    
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            days += 1
            
    return days

# So many diverse solutions. Mine is definitely convoluted.