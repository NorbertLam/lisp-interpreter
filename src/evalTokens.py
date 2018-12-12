from tokenType import TokenType


name_value = {}


def evaluate_tokens(tokens):
    while tokens:
        output = evaluate_expression(tokens)

    return output


def evaluate_expression(tokens):
    while tokens:
        curr = tokens.pop(0)

        if curr.type == TokenType.LPAREN:
            expr = parse_expr(tokens)

            if tokens[0].type == TokenType.INTEGER:
                tokens.pop(0)

            nxt = tokens.pop(0)

            if nxt.type == TokenType.RPAREN:
                return expr
            else:
                print("RPAREN Error")
                return
        elif curr.type == TokenType.INTEGER:
            return curr.value
        elif curr.type == TokenType.NAME:
            return name_value[curr.value]
        elif curr.type == TokenType.TRUE or curr.type == TokenType.FALSE:
            return curr.value
        else:
            print("LPAREN Error")
            return


def parse_expr(tokens):
    if tokens:
        curr = tokens.pop(0)

        if curr.type == TokenType.PLUS:
            exp1 = evaluate_expression(tokens)
            exp2 = evaluate_expression(tokens)

            return exp1 + exp2
        elif curr.type == TokenType.MINUS:
            exp1 = evaluate_expression(tokens)
            exp2 = evaluate_expression(tokens)

            return exp1 - exp2
        elif curr.type == TokenType.MULTIPLY:
            exp1 = evaluate_expression(tokens)
            exp2 = evaluate_expression(tokens)

            return exp1 * exp2
        elif curr.type == TokenType.DIVIDE:
            exp1 = evaluate_expression(tokens)
            exp2 = evaluate_expression(tokens)

            return exp1 // exp2
        elif curr.type == TokenType.INTEGER:
            return curr.value
        elif curr.type == TokenType.DEFINE:
            name = tokens.pop(0)
            value = []
            lparen_count, rparen_count = 1, 0

            while lparen_count != rparen_count:
                if tokens[0].type == TokenType.LPAREN:
                    lparen_count += 1
                elif tokens[0].type == TokenType.RPAREN:
                    rparen_count += 1
                value.append(tokens.pop(0))

            name_value[name.value] = evaluate_expression(value)

        elif curr.type == TokenType.AND:
            exp1 = parse_expr(tokens)
            exp2 = parse_expr(tokens)

            return exp1 and exp2
        elif curr.type == TokenType.OR:
            exp1 = evaluate_expression(tokens)
            exp2 = evaluate_expression(tokens)

            return exp1 or exp2
        elif curr.type == TokenType.NOT:
            return not evaluate_expression(tokens)
        elif curr.type == TokenType.EQ:
            exp1 = evaluate_expression(tokens)
            exp2 = evaluate_expression(tokens)

            return exp1 == exp2
        elif curr.type == TokenType.TRUE or curr.type == TokenType.FALSE:
            return curr.value
        elif curr.type == TokenType.PRINT:
            exp = parse_expr(tokens)
            print(exp)

            return parse_expr(tokens)
        elif curr.type == TokenType.COND:
            return evaluate_cond_cases(tokens)

        return parse_expr(tokens)


def evaluate_cond_cases(tokens):
    tokens.pop(0)

    if tokens[0].type == TokenType.ELSE:
        exp = []

        while tokens[0].type != TokenType.RCOND:
            exp.append(tokens.pop(0))
        tokens.pop(0)

        return parse_expr(exp)

    evaluation = evaluate_expression(tokens)
    if evaluation:
        output = evaluate_expression(tokens)
        del tokens[:-1]

        return output
    else:
        while tokens[0].type != TokenType.LCOND:
            tokens.pop(0)

        return evaluate_cond_cases(tokens)
