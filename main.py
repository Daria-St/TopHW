# from math import pi
#
#
# def circle_area(radius):
#     if type(radius) not in [int, float]:
#         raise TypeError('Радиус должет быть числом')
#     #прописываем исключение, которое вылазит в случае неверного значения - вылазит ошибкой!
#     if radius < 0:
#         raise ValueError('Радиус не может быть меньше нуля')
#     return pi*radius**2
#
# # radius_list = [2, 0, -1, 7 + 9j, True, [2], 'one']
# #
# # for r in radius_list:
# #     s = circle_area(r)
# #     print(f'Радиус {r} | Площадь {s}')


# #Напишем мини калькулятор
# import math
#
#
# def addition (a, b):
#     return a + b
#
# def substraction (a, b):
#     return a - b
#
# def multiplication (a, b):
#     if type(a) not in [int, float] or type(b) not in [int, float]:
#         raise TypeError('Нужно ввести число')
#     return a * b
#
# def division (a, b):
#     return a / b
#
# def square (a):
#     return math.sqrt(a)

#ПРАКТИКА САМОСТОЯТЕЛЬНАЯ


def area_rectangle(a, b):
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError('Нужно ввести число')
    if a < 0 or b < 0:
        raise ValueError('Радиус не может быть меньше нуля')
    return a * b

def area_triangle(a, b, c):
    if type(a) not in [int, float] or type(b) not in [int, float] or type(c) not in [int, float]:
        raise TypeError('Нужно ввести число')
    if a < 0 or b < 0 or c < 0:
        raise ValueError('Радиус не может быть меньше нуля')
    p = (a + b + c)/2
    return ((p*(p-a)*(p-b)*(p-c))**2)

def area_square(a):
    if type(a) not in [int, float]:
        raise TypeError('Нужно ввести число')
    if a < 0:
        raise ValueError('Радиус не может быть меньше нуля')
    return a*a

def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a