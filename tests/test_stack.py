"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


class TestNode(unittest.TestCase):
    def test_node(self):
        node_1 = Node(1, None)
        node_2 = Node('a', node_1)
        self.assertEqual(node_1.data, 1)
        self.assertEqual(node_2.data, 'a')


class TestStack(unittest.TestCase):
    def test_push(self):
        stack_test = Stack()
        stack_test.push('data1')
        stack_test.push('data2')
        stack_test.push('data3')
        self.assertEqual(stack_test.top.data, 'data3')
        self.assertEqual(stack_test.top.next_node.data, 'data2')
        self.assertEqual(stack_test.top.next_node.next_node.data, 'data1')
        self.assertEqual(stack_test.top.next_node.next_node.next_node, None)

    def test_pop(self):
        stack_test = Stack()
        stack_test.push('data1')
        stack_test.push('data2')
        data = stack_test.pop()
        self.assertEqual(stack_test.top.data, 'data1')
        self.assertEqual(data, 'data2')
        data_2 = stack_test.pop()
        self.assertEqual(stack_test.top, None)
        self.assertEqual(data_2, 'data1')
