import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from tokenizer import tokenize
from evalTokens import evaluateTokens


class TestBoolean(unittest.TestCase):

    def test_boolean_not_true(self):
        result = evaluateTokens(tokenize("(not #t)"))
        expected = False
        self.assertEqual(result, expected)

    def test_boolean_not_false(self):
        result = evaluateTokens(tokenize("(not #f)"))
        expected = True
        self.assertEqual(result, expected)

    def test_boolean_or_ff(self):
        result = evaluateTokens(tokenize("(or #f #f)"))
        expected = False
        self.assertEqual(result, expected)

    def test_boolean_or_tf(self):
        result = evaluateTokens(tokenize("(or #t #f)"))
        expected = True
        self.assertEqual(result, expected)

    def test_boolean_and_tf(self):
        result = evaluateTokens(tokenize("(and #t #f)"))
        expected = False
        self.assertEqual(result, expected)

    def test_boolean_eq(self):
        result = evaluateTokens(tokenize("(eq? #f #f)"))
        expected = True
        self.assertEqual(result, expected)

    def test_boolean_nested_or(self):
        result = evaluateTokens(tokenize("(or #t (not #f))"))
        expected = True
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
