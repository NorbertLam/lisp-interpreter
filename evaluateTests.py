import unittest
from tokenizer import tokenize
from parse import evaluate


class TestingEvaluate(unittest.TestCase):

    def test_evaluate_add_01(self):
        result = evaluate(tokenize("(+ 5 2)")[::-1])
        expected = 7
        self.assertEqual(result, expected)

    def test_evaluate_add_02(self):
        result = evaluate(tokenize("(+ 12 52)")[::-1])
        expected = 64
        self.assertEqual(result, expected)

    def test_evaluate_subtract_01(self):
        result = evaluate(tokenize("(- 6 2)")[::-1])
        expected = 4
        self.assertEqual(result, expected)

    def test_evaluate_subtract_02(self):
        result = evaluate(tokenize("(- 22 30)")[::-1])
        expected = -8
        self.assertEqual(result, expected)

    def test_evaluate_multiply_01(self):
        result = evaluate(tokenize("(* 2 2)")[::-1])
        expected = 4
        self.assertEqual(result, expected)

    def test_evaluate_multiply_02(self):
        result = evaluate(tokenize("(* 10 0)")[::-1])
        expected = 0
        self.assertEqual(result, expected)

    def test_evaluate_divide_01(self):
        result = evaluate(tokenize("(/ 25 5)")[::-1])
        expected = 5
        self.assertEqual(result, expected)

    def test_evaluate_divide_02(self):
        result = evaluate(tokenize("(/ 72 3)")[::-1])
        expected = 24
        self.assertEqual(result, expected)

    def test_evaluate_nested_01(self):
        result = evaluate(tokenize("(+ 10 (* 2 (/ 72 (- 6 3)")[::-1])
        expected = 58
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
