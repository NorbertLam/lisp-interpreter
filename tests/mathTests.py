import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from tokenizer import tokenize  # noqa
from evaluator import evaluate_multiple_expression  # noqa


class TestMath(unittest.TestCase):

    def test_evaluate_multiple_expression_add_01(self):
        result = evaluate_multiple_expression(tokenize("(+ 5 2)"))
        expected = 7
        self.assertEqual(result, expected)

    def test_evaluate_multiple_expression_add_02(self):
        result = evaluate_multiple_expression(tokenize("(+ 12 52)"))
        expected = 64
        self.assertEqual(result, expected)

    def test_evaluate_multiple_expression_subtract_01(self):
        result = evaluate_multiple_expression(tokenize("(- 6 2)"))
        expected = 4
        self.assertEqual(result, expected)

    def test_evaluate_multiple_expression_subtract_02(self):
        result = evaluate_multiple_expression(tokenize("(- 22 30)"))
        expected = -8
        self.assertEqual(result, expected)

    def test_evaluate_multiple_expression_multiply_01(self):
        result = evaluate_multiple_expression(tokenize("(* 2 2)"))
        expected = 4
        self.assertEqual(result, expected)

    def test_evaluate_multiple_expression_multiply_02(self):
        result = evaluate_multiple_expression(tokenize("(* 10 0)"))
        expected = 0
        self.assertEqual(result, expected)

    def test_evaluate_multiple_expression_divide_01(self):
        result = evaluate_multiple_expression(tokenize("(/ 25 5)"))
        expected = 5
        self.assertEqual(result, expected)

    def test_evaluate_multiple_expression_divide_02(self):
        result = evaluate_multiple_expression(tokenize("(/ 72 3)"))
        expected = 24
        self.assertEqual(result, expected)

    def test_evaluate_multiple_expression_nested_01(self):
        result = evaluate_multiple_expression(tokenize("(+ 10 (* 2 (/ 72 (- 6 3))))"))
        expected = 58
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
