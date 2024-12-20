"""Что такое очередь?
Очередь — структура данных, работающая по принципу FIFO (First In, First Out).
Первый добавленный элемент извлекается первым.

Основные операции:

enqueue(item) — добавить элемент в очередь.
dequeue() — удалить первый элемент.
is_empty() — проверить, пуста ли очередь.

Примеры использования:
Очереди задач:

В системах печати задания отправляются в очередь и обрабатываются по порядку.
Серверы обработки запросов (например, обработка API-запросов) используют очередь для обработки поступающих запросов.
Буферизация данных:

Очереди используются в потоковой передаче данных, например, при воспроизведении видео.
Мультизадачность:

Операционные системы используют очереди для планирования задач, таких как выполнение процессов.
Реализация очередей сообщений:

Системы, такие как RabbitMQ или Kafka, используют концепцию очередей для доставки сообщений между микросервисами.
"""


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Очередь пуста"

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def print_queue(self):
        return print(self.queue)


# Пример использования
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
print(queue.dequeue())  # Вывод: 10
print(queue.size())  # Вывод: 1