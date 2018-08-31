import unittest
from tokenizer import tokenize
from evalTokens import evaluate


class TestBoolean(unittest.TestCase):

    def test_boolean_not_true(self):
        result = evaluate(tokenize("(not #t)"))
        expected = False
        self.assertEqual(result, expected)

    def test_boolean_not_false(self):
        result = evaluate(tokenize("(not #f)"))
        expected = True
        self.assertEqual(result, expected)

    def test_boolean_or_ff(self):
        result = evaluate(tokenize("(or #f #f)"))
        expected = False
        self.assertEqual(result, expected)

    def test_boolean_or_tf(self):
        result = evaluate(tokenize("(or #t #f)"))
        expected = True
        self.assertEqual(result, expected)

    def test_boolean_and_tf(self):
        result = evaluate(tokenize("(and #t #f)"))
        expected = False
        self.assertEqual(result, expected)

    def test_boolean_eq(self):
        result = evaluate(tokenize("(eq? #f #f)"))
        expected = True
        self.assertEqual(result, expected)

    def test_boolean_nested_or(self):
        result = evaluate(tokenize("(or #f (not #t))"))
        expected = False
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
