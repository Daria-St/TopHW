#документация для ознакомления https://docs.python.org/3/library/unittest.html

# import unittest
# from main import circle_area
# from math import pi
#
# #Этот класс должен унаследовать какой-то тестовый случай
# class TestCircleArea(unittest.TestCase):
#     def test_area(self):
#         #методу подается 2 параметра: 1й это функция, 2й - та же функция записанная выражением
#         self.assertEqual(circle_area(3), pi*3**2)
#         self.assertEqual(circle_area(1), pi)
#         self.assertEqual(circle_area(0), 0)
#         self.assertEqual(circle_area(2.5), pi*2.5**2)
#
#     def test_values(self):
#         #вызывает ли операция исключения (радиус не может быть отрицательным числом). Сначала идет ожидаемое
#         # значение, затем функция и значение, которое подставляется в функцию.
#         self.assertRaises(ValueError, circle_area, -2)
#         self.assertRaises(ValueError, circle_area, -1)
#
#     #тест на типы (ошибка типа, например если введена строка)
#     def test_types(self):
#         self.assertRaises(TypeError, circle_area, 5+2j)
#         self.assertRaises(TypeError, circle_area, 'two')
#         self.assertRaises(TypeError, circle_area, True)
#         self.assertRaises(TypeError, circle_area, [16, 89])
#
# if __name__ == '__main__':
#     unittest.main()



# import unittest
# from main import addition, substraction, multiplication, division, square
# import math
#
# class TestCircleArea(unittest.TestCase):
#     def test_types(self):
#         self.assertRaises(TypeError, addition, *('34', 80))
#         self.assertRaises(TypeError, substraction, *('34', 80))
#         self.assertRaises(TypeError, multiplication, *('34', 80))
#         self.assertRaises(TypeError, division, *('34', 80))
#         self.assertRaises(TypeError, square, '45')
#
#
# if __name__ == '__main__':
#      unittest.main()



#ПРАКТИКА

import unittest
from main import area_rectangle, area_triangle, area_square, is_triangle

class TestCircleArea(unittest.TestCase):


    def test_types(self):
        self.assertRaises(TypeError, area_rectangle, *('11', 2))
        self.assertRaises(TypeError, area_triangle, *('5', 3, 7))
        self.assertRaises(TypeError, area_square, 'two')

    def test_values(self):
        self.assertRaises(ValueError, area_rectangle, *(-2, 3))
        self.assertRaises(ValueError, area_triangle, *(-4, 3, 7))
        self.assertRaises(ValueError, area_square, -3)

    def test_area(self):
        self.assertTrue(is_triangle(2, 2, 5))


if __name__ == '__main__':
     unittest.main()