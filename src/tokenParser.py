import operator
from tokenType import TokenType
from parseTree import (
    DefineNode,
    NumberNode,
    BooleanNode,
    IdNode,
    CondNode,
    PrintNode,
    BinaryFunctionNode,
    UnaryFunctionNode,
    expression_for_id
)

parser_expression_for_id = {}


def evaluate_multiple_expression(tokens):
    output = []

    while tokens:
        output.append(evaluate_expression(tokens))

    return output


def evaluate_expression(tokens):
    curr = tokens.pop(0)

    if curr.type == TokenType.LPAREN:
        expr = evaluate_operator(tokens)
        nxt = tokens.pop(0)

        if nxt.type == TokenType.RPAREN:
            return expr
        else:
            print("RPAREN Error", nxt.type)
            return
    elif curr.type == TokenType.INTEGER:
        return NumberNode(curr.value)
    elif curr.type == TokenType.ID:
        return IdNode(parser_expression_for_id[curr.value])
    elif curr.type == TokenType.TRUE or curr.type == TokenType.FALSE:
        return BooleanNode(curr.value)
    else:
        print("LPAREN Error", curr.type)
        return


def evaluate_operator(tokens):
    curr = tokens.pop(0)

    if curr.type == TokenType.PLUS:
        exp1 = evaluate_expression(tokens)
        exp2 = evaluate_expression(tokens)

        return BinaryFunctionNode(operator.add, exp1, exp2)
    elif curr.type == TokenType.MINUS:
        exp1 = evaluate_expression(tokens)
        exp2 = evaluate_expression(tokens)

        return BinaryFunctionNode(operator.sub, exp1, exp2)
    elif curr.type == TokenType.MULTIPLY:
        exp1 = evaluate_expression(tokens)
        exp2 = evaluate_expression(tokens)

        return BinaryFunctionNode(operator.mul, exp1, exp2)
    elif curr.type == TokenType.DIVIDE:
        exp1 = evaluate_expression(tokens)
        exp2 = evaluate_expression(tokens)

        return BinaryFunctionNode(operator.truediv, exp1, exp2)
    elif curr.type == TokenType.DEFINE:
        name = tokens.pop(0)
        exp = evaluate_expression(tokens)

        return DefineNode(name.value, exp)
    elif curr.type == TokenType.AND:
        exp1 = evaluate_expression(tokens)
        exp2 = evaluate_expression(tokens)

        return BooleanNode(exp1 and exp2)
    elif curr.type == TokenType.OR:
        exp1 = evaluate_expression(tokens)
        exp2 = evaluate_expression(tokens)

        return BooleanNode(exp1 or exp2)
    elif curr.type == TokenType.NOT:
        return BooleanNode(not evaluate_expression(tokens))
    elif curr.type == TokenType.EQ:
        exp1 = evaluate_expression(tokens)
        exp2 = evaluate_expression(tokens)

        return BooleanNode(exp1 == exp2)
    elif curr.type == TokenType.PRINT:
        exp = evaluate_operator(tokens)

        return PrintNode(exp)
    elif curr.type == TokenType.COND:
        cond_cases = evaluate_cond_cases(tokens)

        return CondNode(cond_cases)


def evaluate_cond_cases(tokens):
    cond_expressions = []

    while tokens[0].type == TokenType.LCOND:
        tokens.pop(0)  # pop [

        if tokens[0].type == TokenType.ELSE:
            tokens.pop(0)  # pop the ELSE
            cond_expressions.append((True, evaluate_expression(tokens)))
            tokens.pop(0)  # pop lingering )

            return cond_expressions
        else:
            exp1 = evaluate_expression(tokens)
            exp2 = evaluate_expression(tokens)
            tokens.pop(0)  # pop ]
            cond_expressions.append((exp1, exp2))


def get_cond_return_expression(cond_cases):
    for cond, exp in cond_cases:
        if cond:
            return exp
