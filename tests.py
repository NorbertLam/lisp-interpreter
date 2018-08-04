import unittest
from lisp import Token, tokenize, evaluate


class TestingTokenize(unittest.TestCase):

    def test_tokenize00(self):
        result = tokenize("(+ 5 2)")
        expected = []
        expected.append(Token("OPEN", None))
        expected.append(Token("PLUS", None))
        expected.append(Token("INTEGER", 5))
        expected.append(Token("INTEGER", 2))
        expected.append(Token("CLOSE", None))
        self.assertListEqual(result, expected)

    def test_tokenize01(self):
        result = tokenize("(* 3 4)")
        expected = []
        expected.append(Token("OPEN", None))
        expected.append(Token("MULTIPLY", None))
        expected.append(Token("INTEGER", 3))
        expected.append(Token("INTEGER", 4))
        expected.append(Token("CLOSE", None))
        self.assertListEqual(result, expected)

    def test_tokenize02(self):
        result = tokenize("(+ 5 (* 3 4))")
        expected = []
        expected.append(Token("OPEN", None))
        expected.append(Token("PLUS", None))
        expected.append(Token("INTEGER", 5))
        expected.append(Token("OPEN", None))
        expected.append(Token("MULTIPLY", None))
        expected.append(Token("INTEGER", 3))
        expected.append(Token("INTEGER", 4))
        expected.append(Token("CLOSE", None))
        expected.append(Token("CLOSE", None))
        self.assertListEqual(result, expected)

    def test_evaluate_add00(self):
        result = evaluate(tokenize("(+ 5 2)")[::-1])
        expected = 7
        self.assertEqual(result, expected)

    def test_evaluate_add01(self):
        result = evaluate(tokenize("(+ 12 52)")[::-1])
        expected = 64
        self.assertEqual(result, expected)

    def test_evaluate_subtract00(self):
        result = evaluate(tokenize("(- 6 2)")[::-1])
        expected = 4
        self.assertEqual(result, expected)

    def test_evaluate_subtract01(self):
        result = evaluate(tokenize("(- 22 30)")[::-1])
        expected = -8
        self.assertEqual(result, expected)

    def test_evaluate_multiply00(self):
        result = evaluate(tokenize("(* 2 2)")[::-1])
        expected = 4
        self.assertEqual(result, expected)

    def test_evaluate_multiply01(self):
        result = evaluate(tokenize("(* 10 0)")[::-1])
        expected = 0
        self.assertEqual(result, expected)

    def test_evaluate_divide00(self):
        result = evaluate(tokenize("(/ 25 5)")[::-1])
        expected = 5
        self.assertEqual(result, expected)

    def test_evaluate_divide01(self):
        result = evaluate(tokenize("(/ 72 3)")[::-1])
        expected = 24
        self.assertEqual(result, expected)

    def test_evaluate00(self):
        result = evaluate(tokenize("(+ 10 (* 2 (/ 72 (- 6 3)")[::-1])
        expected = 58
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
