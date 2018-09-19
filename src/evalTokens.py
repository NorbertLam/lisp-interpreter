from tokenType import TokenType


def evaluateTokens(tokens):
    while tokens:
        output = evaluate(tokens)

    return output


def evaluate(tokens):
    while tokens:
        curr = tokens.pop(0)

        if curr.type == TokenType.LPAREN:
            expr = parseExpr(tokens)
        elif curr.type == TokenType.INTEGER:
            return curr.value
        elif curr.type == TokenType.NAME:
            return curr.value[1]
        elif curr.type == TokenType.TRUE or TokenType.FALSE:
            return curr.value
        else:
            print("LPAREN Error")
            return

        if tokens[0].type == TokenType.INTEGER:
            tokens.pop(0)

        nxt = tokens.pop(0)

        if nxt.type == TokenType.RPAREN:
            return expr
        else:
            print("RPAREN Error")
            return


def parseExpr(tokens):
    if tokens:
        curr = tokens.pop(0)

        if curr.type == TokenType.PLUS:
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
            exp1 = parseExpr(tokens)
            exp2 = parseExpr(tokens)

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
        elif curr.type == TokenType.TRUE or curr.type == TokenType.FALSE:
            return curr.value
        elif curr.type == TokenType.PRINT:
            exp = parseExpr(tokens)
            print(exp)
        elif curr.type == TokenType.COND:
            return evaluate_cond_cases(tokens)

        return parseExpr(tokens)


def evaluate_cond_cases(tokens):
    tokens.pop(0)

    if tokens[0].type == TokenType.ELSE:
        exp = []

        while tokens[0].type != TokenType.RCOND:
            exp.append(tokens.pop(0))
        tokens.pop(0)

        return parseExpr(exp)

    evaluation = evaluate(tokens)
    if evaluation:
        output = evaluate(tokens)
        del tokens[:-1]

        return output
    else:
        while tokens[0].type != TokenType.LCOND:
            tokens.pop(0)

        return evaluate_cond_cases(tokens)
