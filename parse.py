from tokenType import TokenType


alias = {}


def evaluate(tokens):
    if tokens:
        curr = tokens.pop(0)

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

            return evaluate(tokens)
        elif curr.type == TokenType.PRINT:
            exp = evaluate(tokens)
            print(exp)
        elif curr.type == TokenType.ID:
            return curr.value
        elif curr.type == TokenType.COND:
            return eval_sub_exp(tokens)
        elif curr.type == TokenType.ELSE:
            return evaluate(tokens)
        elif curr.type == TokenType.LEFT:
            return evaluate(tokens)
        elif curr.type == TokenType.RIGHT:
            return
        elif curr.type == TokenType.CLOSE:
            return evaluate(tokens)


def eval_sub_exp(tokens):
    exp1 = []
    tokens.pop(0)

    if tokens[0].type == TokenType.ELSE:
        return evaluate(tokens)

    while tokens[0].type != TokenType.CLOSE:
        exp1.append(tokens.pop(0))
    exp1.append(tokens.pop(0))

    if evaluate(exp1):
        return evaluate(tokens)
    else:
        while tokens[0].type != TokenType.LEFT:
            tokens.pop(0)
        return eval_sub_exp(tokens)
