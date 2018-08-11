import unittest
from tokenType import TokenType
from tokenizer import Token, tokenize


class TestingTokenize(unittest.TestCase):

    def test_tokenize_basic01(self):
        result = tokenize("(+ 5 2)")
        expected = [Token(TokenType.OPEN, None),
                    Token(TokenType.PLUS, None),
                    Token(TokenType.INTEGER, 5),
                    Token(TokenType.INTEGER, 2),
                    Token(TokenType.CLOSE, None)]
        self.assertListEqual(result, expected)

    def test_tokenize_basic02(self):
        result = tokenize("(* 3 4)")
        expected = [Token(TokenType.OPEN, None),
                    Token(TokenType.MULTIPLY, None),
                    Token(TokenType.INTEGER, 3),
                    Token(TokenType.INTEGER, 4),
                    Token(TokenType.CLOSE, None)]
        self.assertListEqual(result, expected)

    def test_tokenize_nested(self):
        result = tokenize("(+ 5 (* 3 4))")
        expected = [Token(TokenType.OPEN, None),
                    Token(TokenType.PLUS, None),
                    Token(TokenType.INTEGER, 5),
                    Token(TokenType.OPEN, None),
                    Token(TokenType.MULTIPLY, None),
                    Token(TokenType.INTEGER, 3),
                    Token(TokenType.INTEGER, 4),
                    Token(TokenType.CLOSE, None),
                    Token(TokenType.CLOSE, None)]
        self.assertListEqual(result, expected)

    def test_tokenize_boolean(self):
        result = tokenize("(not #f (or #f #t))")
        expected = [Token(TokenType.OPEN, None),
                    Token(TokenType.NOT, None),
                    Token(TokenType.FALSE, None),
                    Token(TokenType.OPEN, None),
                    Token(TokenType.OR, None),
                    Token(TokenType.FALSE, None),
                    Token(TokenType.TRUE, None),
                    Token(TokenType.CLOSE, None),
                    Token(TokenType.CLOSE, None)]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
