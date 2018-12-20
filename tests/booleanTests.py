import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from tokenizer import tokenize  # noqa
from evaluator import evaluate_multiple_expression  # noqa


class TestBoolean(unittest.TestCase):

    def test_boolean_not_true(self):
        result = evaluate_multiple_expression(tokenize("(not #t)"))
        expected = False
        self.assertEqual(result, expected)

    def test_boolean_not_false(self):
        result = evaluate_multiple_expression(tokenize("(not #f)"))
        expected = True
        self.assertEqual(result, expected)

    def test_boolean_or_ff(self):
        result = evaluate_multiple_expression(tokenize("(or #f #f)"))
        expected = False
        self.assertEqual(result, expected)

    def test_boolean_or_tf(self):
        result = evaluate_multiple_expression(tokenize("(or #t #f)"))
        expected = True
        self.assertEqual(result, expected)

    def test_boolean_and_tf(self):
        result = evaluate_multiple_expression(tokenize("(and #t #f)"))
        expected = False
        self.assertEqual(result, expected)

    def test_boolean_eq(self):
        result = evaluate_multiple_expression(tokenize("(eq? #f #f)"))
        expected = True
        self.assertEqual(result, expected)

    def test_boolean_nested_or(self):
        result = evaluate_multiple_expression(tokenize("(or #t (not #f))"))
        expected = True
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
