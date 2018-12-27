import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from tokenizer import Token  # noqa
from tokenType import TokenType  # noga
from evaluator import evaluate_multiple_expression  # noqa


class EvaluatorTests(unittest.TestCase):

    def test_boolean_not_true(self):
        exp = [
            Token(TokenType.LPAREN, None),
            Token(TokenType.NOT, None),
            Token(TokenType.TRUE, True),
            Token(TokenType.RPAREN, None)
        ]
        result = evaluate_multiple_expression(exp)
        expected = False
        self.assertEqual(result, expected)

    def test_boolean_not_false(self):
        exp = [
            Token(TokenType.LPAREN, None),
            Token(TokenType.NOT, None),
            Token(TokenType.FALSE, False),
            Token(TokenType.RPAREN, None)
        ]
        result = evaluate_multiple_expression(exp)
        expected = True
        self.assertEqual(result, expected)

    def test_boolean_or_ff(self):
        exp = [
            Token(TokenType.LPAREN, None),
            Token(TokenType.OR, None),
            Token(TokenType.FALSE, False),
            Token(TokenType.FALSE, False),
            Token(TokenType.RPAREN, None)
        ]
        result = evaluate_multiple_expression(exp)
        expected = False
        self.assertEqual(result, expected)

    def test_boolean_or_tf(self):
        exp = [
            Token(TokenType.LPAREN, None),
            Token(TokenType.OR, None),
            Token(TokenType.TRUE, True),
            Token(TokenType.FALSE, False),
            Token(TokenType.RPAREN, None)
        ]
        result = evaluate_multiple_expression(exp)
        expected = True
        self.assertEqual(result, expected)

    def test_boolean_and_tf(self):
        exp = [
            Token(TokenType.LPAREN, None),
            Token(TokenType.AND, None),
            Token(TokenType.TRUE, True),
            Token(TokenType.FALSE, False),
            Token(TokenType.RPAREN, None)
        ]
        result = evaluate_multiple_expression(exp)
        expected = False
        self.assertEqual(result, expected)

    def test_boolean_eq(self):
        exp = [
            Token(TokenType.LPAREN, None),
            Token(TokenType.EQ, None),
            Token(TokenType.FALSE, False),
            Token(TokenType.FALSE, False),
            Token(TokenType.RPAREN, None)
        ]
        result = evaluate_multiple_expression(exp)
        expected = True
        self.assertEqual(result, expected)

    def test_boolean_nested_or(self):
        exp = [
            Token(TokenType.LPAREN, None),
            Token(TokenType.OR, None),
            Token(TokenType.TRUE, True),
            Token(TokenType.LPAREN, None),
            Token(TokenType.NOT, None),
            Token(TokenType.FALSE, False),
            Token(TokenType.RPAREN, None),
            Token(TokenType.RPAREN, None)
        ]
        result = evaluate_multiple_expression(exp)
        expected = True
        self.assertEqual(result, expected)

    def test_cond_basic(self):
        exp = [
            Token(TokenType.LPAREN, None),
            Token(TokenType.DEFINE, None),
            Token(TokenType.ID, "cats"),
            Token(TokenType.INTEGER, 5),
            Token(TokenType.RPAREN, None),
            Token(TokenType.LPAREN, None),
            Token(TokenType.DEFINE, None),
            Token(TokenType.ID, "dogs"),
            Token(TokenType.INTEGER, 6),
            Token(TokenType.RPAREN, None),
            Token(TokenType.LPAREN, None),
            Token(TokenType.DEFINE, None),
            Token(TokenType.ID, "birds"),
            Token(TokenType.INTEGER, 5),
            Token(TokenType.RPAREN, None),
            Token(TokenType.LPAREN, None),
            Token(TokenType.COND, None),
            Token(TokenType.LCOND, None),
            Token(TokenType.LPAREN, None),
            Token(TokenType.EQ, None),
            Token(TokenType.ID, "cats"),
            Token(TokenType.ID, "birds"),
            Token(TokenType.RPAREN, None),
            Token(TokenType.LPAREN, None),
            Token(TokenType.PLUS, None),
            Token(TokenType.ID, "cats"),
            Token(TokenType.ID, "birds"),
            Token(TokenType.RPAREN, None),
            Token(TokenType.RCOND, None),
            Token(TokenType.LCOND, None),
            Token(TokenType.LPAREN, None),
            Token(TokenType.EQ, None),
            Token(TokenType.ID, "cats"),
            Token(TokenType.ID, "dogs"),
            Token(TokenType.RPAREN, None),
            Token(TokenType.LPAREN, None),
            Token(TokenType.PLUS, None),
            Token(TokenType.ID, "cats"),
            Token(TokenType.ID, "dogs"),
            Token(TokenType.RPAREN, None),
            Token(TokenType.RCOND, None),
            Token(TokenType.LCOND, None),
            Token(TokenType.ELSE, None),
            Token(TokenType.INTEGER, 0),
            Token(TokenType.RCOND, None),
            Token(TokenType.RPAREN, None)
        ]

        result = evaluate_multiple_expression(exp)
        expected = 10
        self.assertEqual(result, expected)

    def test_cond_else(self):
        exp = [
            Token(TokenType.LPAREN, None),
            Token(TokenType.DEFINE, None),
            Token(TokenType.ID, "cats"),
            Token(TokenType.INTEGER, "1"),
            Token(TokenType.RPAREN, None),
            Token(TokenType.LPAREN, None),
            Token(TokenType.DEFINE, None),
            Token(TokenType.ID, "dogs"),
            Token(TokenType.INTEGER, "2"),
            Token(TokenType.RPAREN, None),
            Token(TokenType.LPAREN, None),
            Token(TokenType.DEFINE, None),
            Token(TokenType.ID, "birds"),
            Token(TokenType.INTEGER, "3"),
            Token(TokenType.RPAREN, None),
            Token(TokenType.LPAREN, None),
            Token(TokenType.COND, None),
            Token(TokenType.LCOND, None),
            Token(TokenType.LPAREN, None),
            Token(TokenType.EQ, None),
            Token(TokenType.ID, "cats"),
            Token(TokenType.ID, "birds"),
            Token(TokenType.RPAREN, None),
            Token(TokenType.LPAREN, None),
            Token(TokenType.PLUS, None),
            Token(TokenType.ID, "cats"),
            Token(TokenType.ID, "birds"),
            Token(TokenType.RPAREN, None),
            Token(TokenType.RCOND, None),
            Token(TokenType.LCOND, None),
            Token(TokenType.LPAREN, None),
            Token(TokenType.EQ, None),
            Token(TokenType.ID, "cats"),
            Token(TokenType.ID, "dogs"),
            Token(TokenType.RPAREN, None),
            Token(TokenType.LPAREN, None),
            Token(TokenType.PLUS, None),
            Token(TokenType.ID, "cats"),
            Token(TokenType.ID, "dogs"),
            Token(TokenType.RPAREN, None),
            Token(TokenType.RCOND, None),
            Token(TokenType.LCOND, None),
            Token(TokenType.ELSE, None),
            Token(TokenType.INTEGER, 0),
            Token(TokenType.RCOND, None),
            Token(TokenType.RPAREN, None)
        ]

        result = evaluate_multiple_expression(exp)
        expected = 0
        self.assertEqual(result, expected)

    def test_define_basic(self):
        exp = [
            Token(TokenType.LPAREN, None),
            Token(TokenType.DEFINE, None),
            Token(TokenType.ID, "cat"),
            Token(TokenType.INTEGER, 5),
            Token(TokenType.RPAREN, None),
            Token(TokenType.LPAREN, None),
            Token(TokenType.PLUS, None),
            Token(TokenType.ID, "cat"),
            Token(TokenType.ID, "cat"),
            Token(TokenType.RPAREN, None)
        ]
        result = evaluate_multiple_expression(exp)
        expected = 10
        self.assertEqual(result, expected)

    def test_define_nest(self):
        exp = [
            Token(TokenType.LPAREN, None),
            Token(TokenType.DEFINE, None),
            Token(TokenType.ID, "rat"),
            Token(TokenType.LPAREN, None),
            Token(TokenType.PLUS, None),
            Token(TokenType.INTEGER, 6),
            Token(TokenType.INTEGER, 11),
            Token(TokenType.RPAREN, None),
            Token(TokenType.RPAREN, None),
            Token(TokenType.LPAREN, None),
            Token(TokenType.MINUS, None),
            Token(TokenType.ID, "rat"),
            Token(TokenType.INTEGER, 4),
            Token(TokenType.RPAREN, None)
        ]
        result = evaluate_multiple_expression(exp)
        expected = 13
        self.assertEqual(result, expected)

    def test_define_alias(self):
        exp = [
            Token(TokenType.LPAREN, None),
            Token(TokenType.DEFINE, None),
            Token(TokenType.ID, "cat"),
            Token(TokenType.INTEGER, 5),
            Token(TokenType.RPAREN, None),
            Token(TokenType.LPAREN, None),
            Token(TokenType.DEFINE, None),
            Token(TokenType.ID, "rat"),
            Token(TokenType.LPAREN, None),
            Token(TokenType.PLUS, None),
            Token(TokenType.INTEGER, 6),
            Token(TokenType.INTEGER, 11),
            Token(TokenType.RPAREN, None),
            Token(TokenType.RPAREN, None),
            Token(TokenType.LPAREN, None),
            Token(TokenType.PLUS, None),
            Token(TokenType.ID, "rat"),
            Token(TokenType.ID, "cat"),
            Token(TokenType.RPAREN, None)
        ]
        result = evaluate_multiple_expression(exp)
        expected = 22
        self.assertEqual(result, expected)

    def test_evaluate_multiple_expression_add_01(self):
        exp = [
            Token(TokenType.LPAREN, None),
            Token(TokenType.PLUS, None),
            Token(TokenType.INTEGER, 5),
            Token(TokenType.INTEGER, 2),
            Token(TokenType.RPAREN, None)
        ]
        result = evaluate_multiple_expression(exp)
        expected = 7
        self.assertEqual(result, expected)

    def test_evaluate_multiple_expression_add_02(self):
        exp = [
            Token(TokenType.LPAREN, None),
            Token(TokenType.PLUS, None),
            Token(TokenType.INTEGER, 12),
            Token(TokenType.INTEGER, 52),
            Token(TokenType.RPAREN, None)
        ]
        result = evaluate_multiple_expression(exp)
        expected = 64
        self.assertEqual(result, expected)

    def test_evaluate_multiple_expression_subtract_01(self):
        exp = [
            Token(TokenType.LPAREN, None),
            Token(TokenType.MINUS, None),
            Token(TokenType.INTEGER, 6),
            Token(TokenType.INTEGER, 2),
            Token(TokenType.RPAREN, None)
        ]
        result = evaluate_multiple_expression(exp)
        expected = 4
        self.assertEqual(result, expected)

    def test_evaluate_multiple_expression_subtract_02(self):
        exp = [
            Token(TokenType.LPAREN, None),
            Token(TokenType.MINUS, None),
            Token(TokenType.INTEGER, 22),
            Token(TokenType.INTEGER, 30),
            Token(TokenType.RPAREN, None)
        ]
        result = evaluate_multiple_expression(exp)
        expected = -8
        self.assertEqual(result, expected)

    def test_evaluate_multiple_expression_multiply_01(self):
        exp = [
            Token(TokenType.LPAREN, None),
            Token(TokenType.PLUS, None),
            Token(TokenType.INTEGER, 2),
            Token(TokenType.INTEGER, 2),
            Token(TokenType.RPAREN, None)
        ]
        result = evaluate_multiple_expression(exp)
        expected = 4
        self.assertEqual(result, expected)

    def test_evaluate_multiple_expression_multiply_02(self):
        exp = [
            Token(TokenType.LPAREN, None),
            Token(TokenType.MULTIPLY, None),
            Token(TokenType.INTEGER, 10),
            Token(TokenType.INTEGER, 0),
            Token(TokenType.RPAREN, None)
        ]
        result = evaluate_multiple_expression(exp)
        expected = 0
        self.assertEqual(result, expected)

    def test_evaluate_multiple_expression_divide_01(self):
        exp = [
            Token(TokenType.LPAREN, None),
            Token(TokenType.DIVIDE, None),
            Token(TokenType.INTEGER, 25),
            Token(TokenType.INTEGER, 5),
            Token(TokenType.RPAREN, None)
        ]
        result = evaluate_multiple_expression(exp)
        expected = 5
        self.assertEqual(result, expected)

    def test_evaluate_multiple_expression_divide_02(self):
        exp = [
            Token(TokenType.LPAREN, None),
            Token(TokenType.DIVIDE, None),
            Token(TokenType.INTEGER, 72),
            Token(TokenType.INTEGER, 3),
            Token(TokenType.RPAREN, None)
        ]
        result = evaluate_multiple_expression(exp)
        expected = 24
        self.assertEqual(result, expected)

    def test_evaluate_multiple_expression_nested_01(self):
        exp = [
            Token(TokenType.LPAREN, None),
            Token(TokenType.PLUS, None),
            Token(TokenType.INTEGER, 10),
            Token(TokenType.LPAREN, None),
            Token(TokenType.MULTIPLY, None),
            Token(TokenType.INTEGER, 2),
            Token(TokenType.LPAREN, None),
            Token(TokenType.DIVIDE, None),
            Token(TokenType.INTEGER, 72),
            Token(TokenType.LPAREN, None),
            Token(TokenType.MINUS, None),
            Token(TokenType.INTEGER, 6),
            Token(TokenType.INTEGER, 3),
            Token(TokenType.RPAREN, None),
            Token(TokenType.RPAREN, None),
            Token(TokenType.RPAREN, None),
            Token(TokenType.RPAREN, None)
        ]
        result = evaluate_multiple_expression(exp)
        expected = 58
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
