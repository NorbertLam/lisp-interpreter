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


def custom_split(string):
    deq = list(string)[::-1]
    symbols = set(['(', ')', '[', ']', '?', '+', '-', '*', '/'])
    split_output = []

    while deq:
        if deq[-1] in symbols:
            split_output.append(deq.pop())
        elif deq[-1] == ' ':
            deq.pop()
        else:
            split = ""

            if deq[-1].isdigit():
                while deq[-1].isdigit():
                    split += deq.pop()
                if split:
                    split_output.append(split)
            elif deq[-1] == '#':
                split_output.append(deq.pop() + deq.pop())
            else:
                while deq[-1].isalpha():
                    split += deq.pop()
                if split:
                    split_output.append(split)

    return split_output


def tokenize_split(split):
    tokens = []

    for s in split:
        if s == '+':
            tokens.append(Token(TokenType.PLUS, None))
        elif s == '-':
            tokens.append(Token(TokenType.MINUS, None))
        elif s == '*':
            tokens.append(Token(TokenType.MULTIPLY, None))
        elif s == '/':
            tokens.append(Token(TokenType.DIVIDE, None))
        elif s == '(':
            tokens.append(Token(TokenType.LPAREN, None))
        elif s == ')':
            tokens.append(Token(TokenType.RPAREN, None))
        elif s.lower() == "not":
            tokens.append(Token(TokenType.NOT, None))
        elif s.lower() == "and":
            tokens.append(Token(TokenType.AND, None))
        elif s.lower() == "or":
            tokens.append(Token(TokenType.OR, None))
        elif s.lower() == "eq?":
            tokens.append(Token(TokenType.EQ, None))
        elif s.lower() == '#t':
            tokens.append(Token(TokenType.TRUE, True))
        elif s.lower() == '#f':
            tokens.append(Token(TokenType.FALSE, False))
        elif s.lower() == "define":
            tokens.append(Token(TokenType.DEFINE, None))
        elif s.lower() == "print":
            tokens.append(Token(TokenType.PRINT, None))
        elif s.lower() == "cond":
            tokens.append(Token(TokenType.COND, None))
        elif s.lower() == "else":
            tokens.append(Token(TokenType.ELSE, None))
        elif s == '[':
            tokens.append(Token(TokenType.LCOND, None))
        elif s == ']':
            tokens.append(Token(TokenType.RCOND, None))
        elif s.isdigit():
            tokens.append(Token(TokenType.INTEGER, int(s)))
        elif s.isalpha():
            tokens.append(Token(TokenType.NAME, s))

    return tokens


def tokenize(inpt):
    return tokenize_split(custom_split(inpt))
