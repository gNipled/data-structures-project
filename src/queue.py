class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None
        self.data_list = []

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data, None)
        if self.tail is not None:
            self.tail.next_node = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node
        self.data_list.append(data)

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        # data = self.head.data
        # if self.head.next_node is None:
        #     self.tail = None
        # self.head = self.head.next_node
        # self.data_list.pop(0)
        # return data
        pass

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        return '\n'.join(self.data_list)
