'''
https://www.codewars.com/kata/55f3da49e83ca1ddae0000ad

DESCRIPTION:
6kyu
To introduce the problem think to my neighbor who drives a tanker truck.
The level indicator is down and he is worried because he does not know if
he will be able to make deliveries. We put the truck on a horizontal ground
and measured the height of the liquid in the tank.

Fortunately the tank is a perfect cylinder and the vertical walls on each end
are flat. The height of the remaining liquid is h, the diameter of the
cylinder base is d, the total volume is vt (h, d, vt are positive or null
integers). You can assume that h <= d.

Could you calculate the remaining volume of the liquid? Your function
tankvol(h, d, vt) returns an integer which is the truncated result (e.g floor)
of your float calculation.
'''

import math


def tankvol(h, d, vt):

    radius = d/2
    base_area = math.pi * (radius ** 2)
    tank_height = vt / (math.pi * radius ** 2)
    tri_height = radius - h
    tri_base = math.sqrt(radius ** 2 - tri_height ** 2) * 2
    cosine = tri_height/radius
    angle = math.degrees(math.acos(cosine) * 2)
    sector_area = base_area * (angle/360)
    tri_area = .5 * tri_base * tri_height
    water_area = sector_area - tri_area
    water_volume = int(water_area * tank_height)

    return water_volume

# Needed to brush up on some old math to solve this, lol. Whipped out the
# white-board as well. Very fun!