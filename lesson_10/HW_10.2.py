import math
from abc import ABC, abstractmethod
"""Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру. Наслідуйте від нього
декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру. Властивості по типу
“довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор. Створіть Декілька різних
об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної."""
class Shape:
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        area = math.pi * self.radius**2
        return area
    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter

class Trapezoid(Shape):
    def __init__(self, bottom, top, left, right, high):
        self.bottom = bottom
        self.top = top
        self.left = left
        self.right = right
        self.high = high
    def calculate_area(self):
        area = (self.bottom+self.top) / 2 * self.high
        return area
    def calculate_perimeter(self):
        perimeter = self.bottom + self.top + self.left + self.right
        return perimeter

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def calculate_area(self):
        area = self.side ** 2
        return area
    def calculate_perimeter(self):
        perimeter = 4 * self.side
        return perimeter


my_circle = Circle(12)
print(f"The Circle area is {my_circle.calculate_area()}")
print(f"The Circle perimeter is {my_circle.calculate_perimeter()}")

my_square = Square(3)
print(f"The Square area is {my_square.calculate_area()}")
print(f"The Square perimeter is {my_square.calculate_perimeter()}")

my_trapezoid = Trapezoid(10,3,2,2,7)
print(f"Trapesoid area is  {my_trapezoid.calculate_area()}")
print(f"Trapesoid perimeter is {my_trapezoid.calculate_perimeter()}")

