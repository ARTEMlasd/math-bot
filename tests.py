from utils import *

assert romb(2, 3) == 3
assert romb(2, 5) == 5
assert get_square_of_circle(121) > 0, "значение должно быть больше 0"
assert type(get_square_of_circle(2)) == int or float
assert type(get_square_of_triangle_gerone) == int or float
assert get_square_of_triangle_gerone(4,5,4) == 7.806247497997997
assert quadratic_equation(-12321, -16, -123123313123) == "Корней нету"

print("Все тесты пройдены успешно!")
