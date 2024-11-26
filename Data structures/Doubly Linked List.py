"""Что такое двусвязный список?
Двусвязный список — это структура данных, где каждый элемент (узел) содержит ссылки на предыдущий и следующий элементы.

Основные операции:

insert(value) — добавить элемент.
remove(value) — удалить элемент.
print_list() — вывести все элементы.

Примеры использования:
Реализация undo/redo:

Двусвязный список используется для реализации функций отмены и повторного выполнения в приложениях, например, в графических редакторах.
Память в системах:

В операционных системах список используется для управления свободной памятью (например, в Linux free list).
Списки воспроизведения:

В медиаплеерах можно двигаться по трекам вперед и назад.
Очереди в реальных приложениях:

Используется в программах, где элементы часто добавляются и удаляются в середине.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def remove(self, value):
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                return
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")


# Пример использования
dll = DoublyLinkedList()
dll.insert(10)
dll.insert(20)
dll.insert(30)
dll.print_list()  # Вывод: 10 <-> 20 <-> 30 <-> None
dll.remove(20)
dll.print_list()  # Вывод: 10 <-> 30 <-> None