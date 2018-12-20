import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from tokenizer import tokenize  # noqa
from evaluator import evaluate_multiple_expression  # noqa


class TestDefine(unittest.TestCase):

    def test_define_basic(self):
        result = evaluate_multiple_expression(tokenize("(define cat 5)"
                                          "(+ cat cat)"))
        expected = 10
        self.assertEqual(result, expected)

    def test_define_nest(self):
        result = evaluate_multiple_expression(tokenize("(define rat (+ 6 11))"
                                          "(- rat 4)"))
        expected = 13
        self.assertEqual(result, expected)

    def test_define_alias(self):
        result = evaluate_multiple_expression(tokenize("(define cat 5)"
                                          "(define rat (+ 6 11))"
                                          "(+ rat cat)"))
        expected = 22
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
