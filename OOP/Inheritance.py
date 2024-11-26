"""
Наследование
Позволяет создавать новый класс на основе существующего, наследуя его свойства и методы.
Пример: Родительские и дочерние классы. упрощение кода (например, создание общего родительского класса)"""

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Гав!"

class Cat(Animal):
    def speak(self):
        return "Мяу!"

# Использование
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # Вывод: Гав! Мяу!