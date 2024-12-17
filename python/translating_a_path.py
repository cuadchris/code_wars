'''
https://www.codewars.com/kata/636173d79cf0de003d6834e4

DESCRIPTION:

You are a robot.

As a robot, you are programmed to take walks following a path.

The path is input to you as a string of the following characters where:

"^" -> step up
"v" -> step down
">" -> step right
"<" -> step left
For example, a valid path would look like:

"^^vv>><<^v>"
However, you are a robot that cannot understand this string of characters just by looking at it. You need detailed instructions on how
to follow the path.

Your objective is to write a program to translate the input path to a set of detailed and readable instructions that even a robot like you
could understand.

To do this, you must translate the previous example

"^^vvvv>><<^v>"
to a "line feed separated string" equivalent to:

Take 2 steps up
Take 4 steps down
Take 2 steps right
Take 2 steps left
Take 1 step up
Take 1 step down
Take 1 step right
Notice that groups of the same characters translate to one instruction only, telling you to take multiple steps.

Notes:

The input path will NEVER contain invalid characters, only the four characters for the directions.

The instruction lines are separated only by a newline ("\n") character. This character is not present at the beginning of the first 
instruction line nor at the end of the last instruction line.

An empty path with no characters should output a "Paused" string meaning that you, the robot, are not supposed to move anywhere and are in a 
paused state.
'''

import re
def walk(path):
    
    if not path:
        return "Paused"
    
    directions = {
        "<": "left",
        ">": "right",
        "^": "up",
        "v": "down"
    }
    
    regex = "[<]+|[>]+|[\^]+|[v]+"
    
    matches = re.findall(regex, path)
    
    answer = []
    newLine = '\n'
    
    for match in matches:
        if len(match) == 1:
            answer.append(f"Take {len(match)} step {directions[match[0]]}{newLine}")
        else:
            answer.append(f"Take {len(match)} steps {directions[match[0]]}{newLine}")
            
    return "".join(answer).strip("\n")

# Honestly, I'm surprised at how tough this was. The top solutions on the site used a method called "groupby" from "itertools". I was aware of
# itertools, but not of groupby. Need more practice!