

INTEGER, PLUS, MINUS, MULTIPLY, DIVIDE = \
    "INTEGER", "PLUS", "MINUS", "MULTIPLY", "DIVIDE"
OPEN, CLOSE, = "OPEN", "CLOSE"


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return "Token({type}, {value}".format(
            type=self.type,
            value=self.value
        )

    def __eq__(self, other):
        return isinstance(other, Token) and self.type == other.type \
               and self.value == other.value


def tokenize(inpt):
    tokens = []
    i = 0

    while i < len(inpt):
        if inpt[i].isdigit():
            num = ""

            while inpt[i].isdigit():
                num += str(inpt[i])
                i += 1

            if not inpt[i].isdigit():
                i -= 1

            tokens.append(Token(INTEGER, int(num)))
        elif inpt[i] == '+':
            tokens.append(Token(PLUS, None))
        elif inpt[i] == '-':
            tokens.append(Token(MINUS, None))
        elif inpt[i] == '*':
            tokens.append(Token(MULTIPLY, None))
        elif inpt[i] == '/':
            tokens.append(Token(DIVIDE, None))
        elif inpt[i] == '(':
            tokens.append(Token(OPEN, None))
        elif inpt[i] == ')':
            tokens.append(Token(CLOSE, None))
        i += 1

    return tokens


def evaluate(tokens):
    curr = tokens.pop()
    output = 0

    if curr.type == "OPEN":
        output += evaluate(tokens)
    elif curr.type == "PLUS":
        exp1 = evaluate(tokens)
        exp2 = evaluate(tokens)

        return exp1 + exp2
    elif curr.type == "MINUS":
        exp1 = evaluate(tokens)
        exp2 = evaluate(tokens)

        return exp1 - exp2
    elif curr.type == "MULTIPLY":
        exp1 = evaluate(tokens)
        exp2 = evaluate(tokens)

        return exp1 * exp2
    elif curr.type == "DIVIDE":
        exp1 = evaluate(tokens)
        exp2 = evaluate(tokens)

        return exp1 // exp2
    elif curr.type == "INTEGER":
        output += curr.value
    else:
        return output

    return output
