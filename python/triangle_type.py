'''
https://www.codewars.com/kata/triangle-type

DESCRIPTION:

In this kata, you should calculate type of triangle with three given sides a, b and c 
(given in any order).

If all angles are less than 90°, this triangle is acute and function should return 1.

If one angle is strictly 90°, this triangle is right and function should return 2.

If one angle more than 90°, this triangle is obtuse and function should return 3.

If three sides cannot form triangle, or one angle is 180° (which turns triangle into 
segment) - function should return 0.

Input parameters are sides of given triangle. All input values are non-negative floating 
point or integer numbers (or both).

Examples:
triangle_type(2, 4, 6)  return 0 (Not triangle)
triangle_type(8, 5, 7)  return 1 (Acute, angles are approx. 82°, 38° and 60°)
triangle_type(3, 4, 5)  return 2 (Right, angles are approx. 37°, 53° and exactly 90°)
triangle_type(7, 12, 8)  return 3 (Obtuse, angles are approx. 34°, 106° and 40°)
If you stuck, this can help you: http://en.wikipedia.org/wiki/Law_of_cosines. But you 
can solve this kata even without angle calculation.

There is very small chance of random test to fail due to round-off error, in such case 
resubmit your solution.
'''

import math

def triangle_type(a, b, c):
    # Check if the sides can form a triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return 0  # Not a triangle

    # Calculate the squares of the side lengths
    a_sq = a * a
    b_sq = b * b
    c_sq = c * c

    # Calculate the cosines of the angles
    cos_a = (b_sq + c_sq - a_sq) / (2 * b * c)
    cos_b = (a_sq + c_sq - b_sq) / (2 * a * c)
    cos_c = (a_sq + b_sq - c_sq) / (2 * a * b)

    # Check the type of triangle based on the angles
    if cos_a < 0 or cos_b < 0 or cos_c < 0:
        return 3  # Obtuse triangle
    elif math.isclose(cos_a, 0) or math.isclose(cos_b, 0) or math.isclose(cos_c, 0):
        return 2  # Right triangle
    
    return 1  # Acute triangle