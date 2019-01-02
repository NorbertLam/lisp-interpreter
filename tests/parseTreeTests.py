import unittest
import sys
import os
import operator
sys.path.append(os.path.abspath('../src'))
from parseTree import (
    DefineNode,
    NumberNode,
    BooleanNode,
    IdNode,
    CondNode,
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

    def test_id_node(self):
        expression_for_id["cat"] = 11
        result = IdNode("cat").evaluate()
        expected = 11
        self.assertEqual(result, expected)

    def test_cond_node(self):
        result = CondNode([
            (BinaryFunctionNode(operator.eq, NumberNode(4), NumberNode(5)), NumberNode(9)),
            (BinaryFunctionNode(operator.eq, NumberNode(7523), NumberNode(123)), NumberNode(5)),
            (BinaryFunctionNode(operator.eq, NumberNode(7), NumberNode(7)), NumberNode(34))
        ]).evaluate()
        expected = 34
        self.assertEqual(result, expected)

    def test_binary_function_node(self):
        result = BinaryFunctionNode(operator.add, NumberNode(4), NumberNode(7)).evaluate()
        expected = 11
        self.assertEqual(result, expected)

    def test_unary_function_node(self):
        result = UnaryFunctionNode(operator.abs, NumberNode(-25)).evaluate()
        expected = 25
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
