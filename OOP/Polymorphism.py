"""Полиморфизм (Polymorphism)
Способность объектов разных классов использовать один и тот же интерфейс.
Пример: Переопределение методов (method overriding). гибкость кода (например, единый интерфейс для разных видов объектов).
"""

class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Рисую круг")

class Square(Shape):
    def draw(self):
        print("Рисую квадрат")

# Использование
shapes = [Circle(), Square()]
for shape in shapes:
    shape.draw()