'''
https://www.codewars.com/kata/5970915e54c27bd71000007b

DESCRIPTION:

You will be given a sphere with radius r. Imagine that sphere gets cut with a plane, in this case the
figure that is made with this cut is a circle. You will also be given the distance h between centres of
sphere and circle.Your task is to return the surface area of the original sphere,area of circle and
perimeter of circle, all of them rounded to 3 decimal places and order must be same as in the description.
'''

from math import pi, sqrt

def stereometry(r, h):

    sphere_surface_area = round(4 * pi * r**2, 3)
    
    circle_radius = sqrt(r**2 - h**2)
    
    circle_area = round(pi * circle_radius**2, 3)
    
    circle_perimeter = round(2 * pi * circle_radius, 3)
    
    return (sphere_surface_area, circle_area, circle_perimeter)