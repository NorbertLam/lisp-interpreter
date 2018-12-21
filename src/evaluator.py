from tokenType import TokenType


expression_for_id = {}
cond_expressions = []


def evaluate_multiple_expression(tokens):
    while tokens:
        output = evaluate_expression(tokens)
    del cond_expressions[:]
    return output


def evaluate_expression(tokens):
    curr = tokens.pop(0)

    if curr.type == TokenType.LPAREN:
        expr = evaluate_operator(tokens)
        nxt = tokens.pop(0)

        if nxt.type == TokenType.RPAREN or nxt.type == TokenType.RCOND:
            return expr
        else:
            print("RPAREN Error", nxt.type)
            return
    elif curr.type == TokenType.INTEGER:
        return curr.value
    elif curr.type == TokenType.ID:
        return expression_for_id[curr.value]
    elif curr.type == TokenType.TRUE or curr.type == TokenType.FALSE:
        return curr.value
    else:
        print("LPAREN Error", curr.type)
        return


def evaluate_operator(tokens):
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
    elif curr.type == TokenType.DEFINE:
        name = tokens.pop(0)
        expression_for_id[name.value] = evaluate_expression(tokens)
    elif curr.type == TokenType.AND:
        exp1 = evaluate_expression(tokens)
        exp2 = evaluate_expression(tokens)

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
    elif curr.type == TokenType.PRINT:
        exp = evaluate_operator(tokens)
        print(exp)

        return evaluate_operator(tokens)
    elif curr.type == TokenType.COND:
        return evaluate_cond_cases(tokens)


def evaluate_cond_cases(tokens):

    tokens.pop(0)  # pop [

    if tokens[0].type == TokenType.ELSE:
        tokens.pop(0)  # pop the ELSE
        cond = return_true_cond_case(cond_expressions)
        else_case = evaluate_else_case(tokens)
        if cond:
            return cond
        return else_case

    exp1 = evaluate_expression(tokens)
    exp2 = evaluate_expression(tokens)
    tokens.pop(0)  # pop ]
    cond_expressions.append((exp1, exp2))

    if tokens:
        return evaluate_cond_cases(tokens)


def return_true_cond_case(cond_cases):
    for case in cond_cases:
        if len(case) == 2 and case[0]:
            return case[1]


def evaluate_else_case(tokens):
    exp = evaluate_expression(tokens)
    tokens.pop(0)  # pop lingering )

    return exp
