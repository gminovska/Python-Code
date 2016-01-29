import math

def polysum (n, s):
    '''
the function takes 2 arguments: n-number of sides of a regular polygone,
and s-the length of the sides.
Returns the sum of the area and the square of the perimeter
    '''
    area = (0.25 * n * s**2)/math.tan(math.pi/n)
    perimeter = s * n
    return round(area + (perimeter*perimeter),4)
