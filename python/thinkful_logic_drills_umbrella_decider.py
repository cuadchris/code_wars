'''
https://www.codewars.com/kata/5865a28fa5f191d35f0000f8

DESCRIPTION:

Write a function take_umbrella() that takes two arguments: a string representing the current weather and
a float representing the chance of rain today.

Your function should return True or False based on the following criteria.

You should take an umbrella if it's currently raining or if it's cloudy and the chance of rain is over
0.20.

You shouldn't take an umbrella if it's sunny unless it's more likely to rain than not.
The options for the current weather are sunny, cloudy, and rainy.

For example, take_umbrella('sunny', 0.40) should return False.

As an additional challenge, consider solving this kata using only logical operaters and not using any if
statements.
'''

def take_umbrella(weather, rain_chance):
    return weather == "rainy" or (weather == "cloudy" and rain_chance > 0.2) or (weather == "sunny" and rain_chance > 0.5)