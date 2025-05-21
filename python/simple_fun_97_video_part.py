'''
https://www.codewars.com/kata/589809f0fcc4b92ea200033a

DESCRIPTION:

You have been watching a video for some time. Knowing the total video duration find out what portion of
the video you have already watched.

Example:

For part = "02:20:00" and total = "07:00:00", the output should be [1, 3].

You have watched 1 / 3 of the whole video.

Input/Output
[input] string part

A string of the following format "hh:mm:ss" representing the time you have been watching the video.

[input] string total

A string of the following format "hh:mm:ss" representing the total video duration.

[output] an integer array

An array of the following format [a, b] (where a / b is a reduced fraction).
'''

import math

def video_part(part, total):

    def to_seconds(time_str):
        h, m, s = map(int, time_str.split(':'))
        return h * 3600 + m * 60 + s
    
    part_seconds = to_seconds(part)
    total_seconds = to_seconds(total)
    
    gcd = math.gcd(part_seconds, total_seconds)
    return [part_seconds // gcd, total_seconds // gcd]