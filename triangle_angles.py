""" Solution for http://www.checkio.org/mission/triangle-angles/ in Python 2.7 """

import math

def calculate_angle(a, b, c):
    cos = (b*b + c*c - a*a) / (2.0 * b * c)
    result = math.acos(cos)/math.pi * 180

    result = int(round(result))
    if result >= 180:
        result -= 180

    return result

def checkio(a, b, c):
    all = [a, b, c]
    all.sort()

    if all[0] + all[1] < all[2]:
        return [0, 0, 0]
        
    angle_a = calculate_angle(a, b, c)
    angle_b = calculate_angle(b, c, a)
    angle_c = calculate_angle(c, a, b)
    result = [angle_a, angle_b, angle_c]
    result.sort()
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
