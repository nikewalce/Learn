"""Абстракция (Abstraction)
Скрытие деталей реализации и предоставление только важных характеристик объекта.
Пример: Интерфейсы, абстрактные классы. проектирование систем (например, интерфейсы для модулей)"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Использование
rect = Rectangle(5, 10)
print(f"Площадь: {rect.area()}")        # Вывод: Площадь: 50
print(f"Периметр: {rect.perimeter()}")  # Вывод: Периметр: 30