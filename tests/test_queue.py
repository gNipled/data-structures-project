"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue

queue = Queue()
queue_1 = Queue()


class TestQueue(unittest.TestCase):

    def test_Queue_enqueue(self):
        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)
        queue.enqueue('data1')
        self.assertIsNone(queue.tail.next_node)
        self.assertIsNone(queue.head.next_node)
        queue.enqueue('data2')
        self.assertIsNone(queue.tail.next_node)
        self.assertEquals(queue.head.data, 'data1')
        self.assertEquals(queue.tail.data, 'data2')
        self.assertEquals(queue.head.next_node.data, 'data2')

    def test_Queue___str__(self):
        self.assertEquals(str(queue_1), '')
        queue_1.enqueue('data1')
        self.assertEquals(str(queue_1), 'data1')
        queue_1.enqueue('data2')
        self.assertEquals(str(queue_1), 'data1\ndata2')


