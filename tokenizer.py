from tokenType import TokenType


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        type = self.type
        value = self.value
        return f'{type}, {value}'

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

            tokens.append(Token(TokenType.INTEGER, int(num)))
        elif inpt[i] == '+':
            tokens.append(Token(TokenType.PLUS, None))
        elif inpt[i] == '-':
            tokens.append(Token(TokenType.MINUS, None))
        elif inpt[i] == '*':
            tokens.append(Token(TokenType.MULTIPLY, None))
        elif inpt[i] == '/':
            tokens.append(Token(TokenType.DIVIDE, None))
        elif inpt[i] == '(':
            tokens.append(Token(TokenType.OPEN, None))
        elif inpt[i] == ')':
            tokens.append(Token(TokenType.CLOSE, None))
        i += 1

    return tokens
