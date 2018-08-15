from tokenType import TokenType


alias = {}


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
    elif curr.type == TokenType.AND:
        exp1 = evaluate(tokens)
        exp2 = evaluate(tokens)

        return exp1 and exp2
    elif curr.type == TokenType.OR:
        exp1 = evaluate(tokens)
        exp2 = evaluate(tokens)

        return exp1 or exp2
    elif curr.type == TokenType.NOT:
        return not evaluate(tokens)
    elif curr.type == TokenType.EQ:
        exp1 = evaluate(tokens)
        exp2 = evaluate(tokens)

        return exp1 == exp2
    elif curr.type == TokenType.TRUE:
        return True
    elif curr.type == TokenType.FALSE:
        return False
    elif curr.type == TokenType.DEFINE:
        return evaluate(tokens)
    elif curr.type == TokenType.NAME:
        alias[curr.value[0]] = curr.value[1]

        return alias[curr.value[0]]
    elif curr.type == TokenType.PRINT:
        exp = evaluate(tokens)
        print(exp)
    elif curr.type == TokenType.ID:
        return curr.value
    elif curr.type == TokenType.CLOSE:
        tokens.pop()
        return evaluate(tokens)
