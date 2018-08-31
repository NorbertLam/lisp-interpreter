from tokenType import TokenType


alias = {}


def evaluate(tokens):
    if tokens:
        curr = tokens.pop(0)

        if curr.type == TokenType.LPAREN:
            expr = parseExpr(tokens)
        elif curr.type == TokenType.INTEGER or curr.type == TokenType.ID:
            return curr.value
        else:
            print(curr.type, "LPAREN Error")
            return

        nxt = tokens.pop(0)

        if nxt.type == TokenType.RPAREN:
            return expr
        else:
            for t in tokens:
                print(t.type, t.value)
            print(curr.type, "RPAREN Error")
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
            exp1 = parseExpr(tokens)
            exp2 = parseExpr(tokens)

            return exp1 or exp2
        elif curr.type == TokenType.NOT:
            return not parseExpr(tokens)
        elif curr.type == TokenType.EQ:
            exp1 = evaluate(tokens)
            exp2 = evaluate(tokens)

            return exp1 == exp2
        elif curr.type == TokenType.TRUE:
            return True
        elif curr.type == TokenType.FALSE:
            return False
        elif curr.type == TokenType.DEFINE:
            exp1 = evaluate(tokens)

            return exp1
        elif curr.type == TokenType.NAME:
            alias[curr.value[0]] = curr.value[1]

            return parseExpr(tokens)
        elif curr.type == TokenType.PRINT:
            exp = parseExpr(tokens)
            print(exp)
        elif curr.type == TokenType.ID:
            return curr.value
        elif curr.type == TokenType.COND:
            return evaluate_cond_cases(tokens)
        elif curr.type == TokenType.ELSE:
            return parseExpr(tokens)
        elif curr.type == TokenType.LCOND:
            return evaluate(tokens)
        elif curr.type == TokenType.RCOND:
            return evaluate(tokens)

        return parseExpr(tokens)


def evaluate_cond_cases(tokens):
    exp1 = []
    tokens.pop(0)

    if tokens[0].type == TokenType.ELSE:
        return parseExpr(tokens)

    while tokens[0].type != TokenType.RPAREN:
        exp1.append(tokens.pop(0))
    exp1.append(tokens.pop(0))

    if evaluate(exp1):
        return evaluate(tokens)
    else:
        while tokens[0].type != TokenType.LCOND:
            tokens.pop(0)
        return evaluate_cond_cases(tokens)
