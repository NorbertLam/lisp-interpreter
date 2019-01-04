import unittest
import sys
import os
import operator
sys.path.append(os.path.abspath('../src'))
from tokenizer import Token  # noqa
from tokenType import TokenType  # noga
from tokenParser import evaluate_multiple_expression  # noqa
from parseTree import (
    DefineNode,
    NumberNode,
    BooleanNode,
    IdNode,
    CondNode,
    BinaryFunctionNode,
    UnaryFunctionNode,
    expression_for_id
)


class ParserTest(unittest.TestCase):

    def test_parser_binary_function_node(self):
        exp = [
            Token(TokenType.LPAREN, None),
            Token(TokenType.PLUS, None),
            Token(TokenType.INTEGER, 5),
            Token(TokenType.INTEGER, 2),
            Token(TokenType.RPAREN, None)
        ]
        result = evaluate_multiple_expression(exp)
        expected = [
            BinaryFunctionNode(operator.add, NumberNode(5), NumberNode(2))
        ]
        self.assertEqual(result, expected)

    def test_parser_boolean_node(self):
        exp = [
            Token(TokenType.LPAREN, None),
            Token(TokenType.NOT, None),
            Token(TokenType.TRUE, True),
            Token(TokenType.RPAREN, None)
        ]
        result = evaluate_multiple_expression(exp)
        expected = [
            UnaryFunctionNode(operator.not_, BooleanNode(True))
        ]
        self.assertEqual(result, expected)

    def test_parser_boolean_node_nested_or(self):
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
        expected = [
            BinaryFunctionNode(operator.or_, BooleanNode(True), UnaryFunctionNode(operator.not_, BooleanNode(False)))
        ]
        self.assertEqual(result, expected)

    def test_parser_nested_math(self):
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
        expected = [
            BinaryFunctionNode(
                operator.add,
                NumberNode(10),
                BinaryFunctionNode(
                    operator.mul,
                    NumberNode(2),
                    BinaryFunctionNode(
                        operator.truediv,
                        NumberNode(72),
                        BinaryFunctionNode(
                            operator.sub,
                            NumberNode(6),
                            NumberNode(3)
                        )
                    )
                )
            )
        ]
        self.assertEqual(result, expected)

    def test_parser_define_node_basic(self):
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
        expected = [
            DefineNode("cat", NumberNode(5)),
            BinaryFunctionNode(operator.add, IdNode("cat"), IdNode("cat"))
        ]
        self.assertEqual(result, expected)

    def test_parser_cond_node_basic(self):
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
        expected = [
            DefineNode("cats", NumberNode(5)),
            DefineNode("dogs", NumberNode(6)),
            DefineNode("birds", NumberNode(5)),
            CondNode([
                (BinaryFunctionNode(operator.eq, IdNode("cats"), IdNode("birds")),
                 BinaryFunctionNode(operator.add, IdNode("cats"), IdNode("birds"))),
                (BinaryFunctionNode(operator.eq, IdNode("cats"), IdNode("dogs")),
                 BinaryFunctionNode(operator.add, IdNode("cats"), IdNode("dogs"))),
                (BooleanNode(True), NumberNode(0))
            ])
        ]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
