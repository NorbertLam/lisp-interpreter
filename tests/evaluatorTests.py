import unittest
import operator
import sys
import os
sys.path.append(os.path.abspath('../src'))
from evaluator import evaluate
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


class EvaluatorTests(unittest.TestCase):

    def test_evaluate_math_add_basic(self):
        exp = [
            BinaryFunctionNode(operator.add,
                               NumberNode(123),
                               NumberNode(41))
        ]
        result = evaluate(exp)
        expected = [164]
        self.assertEqual(result, expected)

    def test_evaluate_math_subtract_basic(self):
        exp = [
            BinaryFunctionNode(operator.sub,
                               NumberNode(48),
                               NumberNode(22))
        ]
        result = evaluate(exp)
        expected = [26]
        self.assertEqual(result, expected)

    def test_evaluate_math_multiply_basic(self):
        exp = [
            BinaryFunctionNode(operator.mul,
                               NumberNode(10),
                               NumberNode(10))
        ]
        result = evaluate(exp)
        expected = [100]
        self.assertEqual(result, expected)

    def test_evaluate_math_divide_basic(self):
        exp = [
            BinaryFunctionNode(operator.truediv,
                               NumberNode(225),
                               NumberNode(5))
        ]
        result = evaluate(exp)
        expected = [45]
        self.assertEqual(result, expected)

    def test_evaluate_cond_basic(self):
        exp = [
            CondNode([
                (BinaryFunctionNode(operator.eq,
                                    NumberNode(123),
                                    NumberNode(3)),
                 NumberNode(23)),
                (BinaryFunctionNode(operator.eq,
                                    NumberNode(246),
                                    NumberNode(542)),
                 NumberNode(55)),
                (BinaryFunctionNode(operator.eq,
                                    NumberNode(67),
                                    NumberNode(67)),
                 NumberNode(1))
            ])
        ]
        result = evaluate(exp)
        expected = [1]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()