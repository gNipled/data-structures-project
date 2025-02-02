"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack

stack = Stack()
stack_1 = Stack()
stack_2 =Stack()


class TestStack(unittest.TestCase):

    def test_Stack_Push(self):
        stack.push('data1')
        stack.push('data2')
        self.assertEquals(stack.top.data, 'data2')
        self.assertEquals(stack.top.next_node.data, 'data1')
        with self.assertRaises(AttributeError):
            stack.top.next_node.next_node.data

    def test_Stack_Pop(self):
        stack_1.push('data1')
        self.assertEquals(stack_1.pop(), 'data1')
        self.assertIsNone(stack_1.top)
        stack_1.push('data1')
        stack_1.push('data2')
        self.assertEquals(stack_1.pop(), 'data2')
        self.assertEquals(stack_1.top.data, 'data1')

    def test_Stack___str__(self):
        self.assertEquals(str(stack_2), '')
        stack_2.push('data1')
        stack_2.push('data2')
        self.assertEquals(str(stack_2), 'data1\ndata2')
