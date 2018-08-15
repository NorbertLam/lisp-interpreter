import unittest
from tokenizer import tokenize
from parse import evaluate, alias


class TestingDefine(unittest.TestCase):

    def test_basic(self):
        result = evaluate(tokenize("(define cat 5)")[::-1])
        expected = 5
        self.assertEqual(result, expected)

    def test_nest(self):
        result = evaluate(tokenize("(define rat (+ 6 11))")[::-1])
        expected = 17
        self.assertEqual(result, expected)

    def test_alias(self):
        evaluate(tokenize("(define cat 5)")[::-1])
        evaluate(tokenize("(define rat (+ 6 11))")[::-1])
        result = evaluate(tokenize("(+ rat cat)")[::-1])
        expected = 22
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
