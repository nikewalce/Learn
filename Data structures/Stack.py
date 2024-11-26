"""Часть 1: Стек (Stack)
Что такое стек?
Стек — это структура данных, работающая по принципу LIFO (Last In, First Out).
Последний добавленный элемент извлекается первым.

Основные операции:

push(item) — добавить элемент в стек.
pop() — удалить верхний элемент.
peek() — посмотреть верхний элемент, не удаляя его.
is_empty() — проверить, пуст ли стек.

Примеры использования:
Обратный порядок действий:

Например, в браузерах при нажатии кнопки "Назад" используется стек для хранения истории посещенных страниц.
Вы нажимаете "Назад", и верхняя страница стека удаляется.
Рекурсия:

Стек используется для хранения текущего состояния вызова функции.
Это основа работы большинства языков программирования.
Парсер выражений:

При компиляции программ языки разбирают выражения (например, 2 + 3 * 4) с использованием стека.
Отмена действий (Undo):

В текстовых редакторах (например, Word) стек используется для хранения списка действий, которые можно отменить."""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Стек пуст"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Стек пуст"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def print_stack(self):
        return print(self.stack)

# Пример использования
stack = Stack()
stack.push(10)
stack.push(20)
print(stack.peek())  # Вывод: 20
print(stack.pop())  # Вывод: 20
print(stack.is_empty())  # Вывод: False
print(stack.size())
stack.print_stack()
