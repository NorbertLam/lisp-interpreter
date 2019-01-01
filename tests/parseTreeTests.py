import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from parseTree import (
    DefineNode,
    NumberNode,
    BooleanNode,
    IdNode,
    BinaryFunctionNode,
    UnaryFunctionNode,
    expression_for_id
)


class ParseTreeTests(unittest.TestCase):

    def test_define_node(self):
        DefineNode("dog", NumberNode(123)).evaluate()
        result = expression_for_id["dog"]
        expected = 123
        self.assertEqual(result, expected)

    def test_number_node(self):
        result = NumberNode(5).evaluate()
        expected = 5
        self.assertEqual(result, expected)

    def test_boolean_node(self):
        result = BooleanNode(True).evaluate()
        expected = True
        self.assertEqual(result, expected)

    def test_Id_node(self):
        DefineNode("cat", NumberNode(11)).evaluate()
        result = IdNode("cat").evaluate()
        expected = 11
        self.assertEqual(result, expected)

    def test_binary_function_node(self):
        def add(a, b):
            return a + b
        result = BinaryFunctionNode(add, NumberNode(4), NumberNode(7)).evaluate()
        expected = 11
        self.assertEqual(result, expected)

    def test_unary_function_node(self):
        def square(a):
            return a**2
        result = UnaryFunctionNode(square, NumberNode(25)).evaluate()
        expected = 625
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
