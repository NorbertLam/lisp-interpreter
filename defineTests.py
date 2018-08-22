import unittest
from tokenizer import tokenize
from parse import evaluate


class TestingDefine(unittest.TestCase):

    def test_basic(self):
        evaluate(tokenize("(define cat 5)"))
        result = evaluate(tokenize("(+ cat cat)"))
        expected = 10
        self.assertEqual(result, expected)

    def test_nest(self):
        evaluate(tokenize("(define rat (+ 6 11))"))
        result = evaluate(tokenize("(- rat 4)"))
        expected = 13
        self.assertEqual(result, expected)

    def test_alias(self):
        evaluate(tokenize("(define cat 5)"))
        evaluate(tokenize("(define rat (+ 6 11))"))
        result = evaluate(tokenize("(+ rat cat)"))
        expected = 22
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
