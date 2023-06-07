import math


def validate_input(text):  # '1,2,3'
    try:
        s = []
        command = text.split(',')
        for i in command:
            s.append(int(i))
        return s
    except (ValueError, TypeError):
        return False


def romb(d1, d2):
    s = 0.5 * (d1 * d2)
    return s


def get_square_of_circle(r):
    S = r ** 2 * 3.14
    return S


def get_square_of_triangle_gerone(a, b, c):
    if (a + b) <= c or (b + c) <= a or (c + a) <= b:
        return "треугольника не существует"
    else:
        p = (a + b + c) / 2
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return S


def get_square_of_triangle_base(a, b):
    S = (1 / 2) * (a * b)
    print(S)


def quadratic_equation(a, b, c):
    D = b ** 2 - (4 * a * c)
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return (x1, x2)
    elif D == 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        return (x1)
    else:
        x1 = "Корней нету"
        return (x1)


"""
a = [1]
get_square_of_circle(2)
get_square_of_triangle_gerone(13, 9, 11)
quadratic_equation(2, 4, 5)
"""
