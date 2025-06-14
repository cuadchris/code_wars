'''
https://www.codewars.com/kata/643af0fa9fa6c406b47c5399

Description:
Given a point in a Euclidean plane (x and y), return the quadrant the point exists in: 1, 2, 3 or 4
(integer). x and y are non-zero integers, therefore the given point never lies on the axes.

Examples:

(1, 2)     => 1
(3, 5)     => 1
(-10, 100) => 2
(-1, -9)   => 3
(19, -56)  => 4
'''

def quadrant(x, y):
    
    return 1 if x > 0 and y > 0 else 2 if x < 0 and y > 0 else 3 if x < 0 and y < 0 else 4 if x > 0 and y < 0 else None

# sheesh
