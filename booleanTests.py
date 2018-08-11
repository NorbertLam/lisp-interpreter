import unittest
from tokenizer import tokenize
from parse import evaluate


class TestingBoolean(unittest.TestCase):

    def test_not_true(self):
        result = evaluate(tokenize("(not #t)")[::-1])
        expected = False
        self.assertEqual(result, expected)

    def test_not_false(self):
        result = evaluate(tokenize("(not #f)")[::-1])
        expected = True
        self.assertEqual(result, expected)

    def test_or_ff(self):
        result = evaluate(tokenize("(or #f #f)")[::-1])
        expected = False
        self.assertEqual(result, expected)

    def test_or_tf(self):
        result = evaluate(tokenize("(or #t #f)")[::-1])
        expected = True
        self.assertEqual(result, expected)

    def test_and_tf(self):
        result = evaluate(tokenize("(and #t #f)")[::-1])
        expected = False
        self.assertEqual(result, expected)

    def test_eq(self):
        result = evaluate(tokenize("(eq #f #f)")[::-1])
        expected = True
        self.assertEqual(result, expected)

    def test_nested_or(self):
        result = evaluate(tokenize("(or #f (not #t))")[::-1])
        expected = False
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
