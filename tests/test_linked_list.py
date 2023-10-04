"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList

ll1 = LinkedList()
ll2 = LinkedList()
ll3 = LinkedList()
ll4 = LinkedList()


class TestLinkedList(unittest.TestCase):

    def test_insert_beginning(self):
        self.assertEquals(str(ll1), 'None')
        ll1.insert_beginning({'id': 1})
        self.assertEquals(str(ll1), "{'id': 1} -> None")
        ll1.insert_beginning({'id': 2})
        self.assertEquals(str(ll1), "{'id': 2} -> {'id': 1} -> None")

    def test_insert_at_end(self):
        self.assertEquals(str(ll2), 'None')
        ll2.insert_at_end({'id': 1})
        self.assertEquals(str(ll2), "{'id': 1} -> None")
        ll2.insert_at_end({'id': 2})
        self.assertEquals(str(ll2), "{'id': 1} -> {'id': 2} -> None")

    def test___str__(self):
        self.assertEquals(str(ll3), 'None')
        ll3.insert_beginning({'id': 1})
        ll3.insert_at_end({'id': 2})
        ll3.insert_at_end({'id': 3})
        ll3.insert_beginning({'id': 0})
        self.assertEquals(str(ll3), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")

    def test_to_list(self):
        self.assertEquals(len(LinkedList().to_list()), 0)
        self.assertEquals(len(ll3.to_list()), 4)

    def test_get_data_by_id(self):
        ll4.insert_at_end({'id': 1})
        ll4.insert_at_end({45,23,1})
        ll4.insert_at_end('id45user1name')
        ll4.insert_at_end([45, 45, 45, 1])
        self.assertEquals(type(ll4.get_data_by_id(1)), dict)
        self.assertIsNone(ll4.get_data_by_id(45))


