import unittest
from tokenizer import tokenize
from evalTokens import evaluateTokens


class TestDefine(unittest.TestCase):

    def test_define_basic(self):
        ls = tokenize("(define cat 5)")
        evaluateTokens(ls)
        result = evaluateTokens(tokenize("(+ cat cat)"))
        expected = 10
        self.assertEqual(result, expected)

    def test_define_nest(self):
        evaluateTokens(tokenize("(define rat (+ 6 11))"))
        ls = tokenize("(- rat 4)")
        result = evaluateTokens(ls)

        expected = 13
        self.assertEqual(result, expected)

    def test_define_alias(self):
        evaluateTokens(tokenize("(define cat 5)"))
        evaluateTokens(tokenize("(define rat (+ 6 11))"))
        result = evaluateTokens(tokenize("(+ rat cat)"))
        expected = 22
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
