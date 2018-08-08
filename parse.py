from tokenType import TokenType


def evaluate(tokens):
    curr = tokens.pop()

    if curr.type == TokenType.OPEN:
        return evaluate(tokens)
    elif curr.type == TokenType.PLUS:
        exp1 = evaluate(tokens)
        exp2 = evaluate(tokens)

        return exp1 + exp2
    elif curr.type == TokenType.MINUS:
        exp1 = evaluate(tokens)
        exp2 = evaluate(tokens)

        return exp1 - exp2
    elif curr.type == TokenType.MULTIPLY:
        exp1 = evaluate(tokens)
        exp2 = evaluate(tokens)

        return exp1 * exp2
    elif curr.type == TokenType.DIVIDE:
        exp1 = evaluate(tokens)
        exp2 = evaluate(tokens)

        return exp1 // exp2
    elif curr.type == TokenType.INTEGER:
        return curr.value
    else:
        return 0
