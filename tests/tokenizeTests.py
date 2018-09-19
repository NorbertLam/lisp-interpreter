import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from tokenType import TokenType  # noqa
from tokenizer import Token, tokenize  # noqa


class TestTokenize(unittest.TestCase):

    def test_tokenize_basic01(self):
        result = tokenize("(+ 5 2)")
        expected = [Token(TokenType.LPAREN, None),
                    Token(TokenType.PLUS, None),
                    Token(TokenType.INTEGER, 5),
                    Token(TokenType.INTEGER, 2),
                    Token(TokenType.RPAREN, None)]
        self.assertListEqual(result, expected)

    def test_tokenize_basic02(self):
        result = tokenize("(* 3 4)")
        expected = [Token(TokenType.LPAREN, None),
                    Token(TokenType.MULTIPLY, None),
                    Token(TokenType.INTEGER, 3),
                    Token(TokenType.INTEGER, 4),
                    Token(TokenType.RPAREN, None)]
        self.assertListEqual(result, expected)

    def test_tokenize_nested(self):
        result = tokenize("(+ 5 (* 3 4))")
        expected = [Token(TokenType.LPAREN, None),
                    Token(TokenType.PLUS, None),
                    Token(TokenType.INTEGER, 5),
                    Token(TokenType.LPAREN, None),
                    Token(TokenType.MULTIPLY, None),
                    Token(TokenType.INTEGER, 3),
                    Token(TokenType.INTEGER, 4),
                    Token(TokenType.RPAREN, None),
                    Token(TokenType.RPAREN, None)]
        self.assertListEqual(result, expected)

    def test_tokenize_boolean(self):
        result = tokenize("(not #f (or #f #t))")
        expected = [Token(TokenType.LPAREN, None),
                    Token(TokenType.NOT, None),
                    Token(TokenType.FALSE, False),
                    Token(TokenType.LPAREN, None),
                    Token(TokenType.OR, None),
                    Token(TokenType.FALSE, False),
                    Token(TokenType.TRUE, True),
                    Token(TokenType.RPAREN, None),
                    Token(TokenType.RPAREN, None)]
        self.assertEqual(result, expected)

    def test_tokenize_define(self):
        result = tokenize("(define cat 5)")
        expected = [Token(TokenType.LPAREN, None),
                    Token(TokenType.DEFINE, None),
                    Token(TokenType.NAME, ('cat', 5)),
                    Token(TokenType.INTEGER, 5),
                    Token(TokenType.RPAREN, None)]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
