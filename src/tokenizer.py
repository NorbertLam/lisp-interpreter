from tokenType import TokenType
from collections import deque


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
    deq = deque(string)
    symbols = set(['(', ')', '[', ']', '?', '+', '-', '*', '/'])
    split_output = []

    while deq:
        if deq[0] in symbols:
            split_output.append(deq.popleft())
        elif deq[0] == ' ':
            deq.popleft()
        else:
            split = ""

            if deq[0].isdigit():
                while deq[0].isdigit():
                    split += deq.popleft()
                if split:
                    split_output.append(split)
            elif deq[0] == '#':
                split_output.append(deq.popleft() + deq.popleft())
            else:
                while deq[0].isalpha():
                    split += deq.popleft()
                if split:
                    split_output.append(split)

    return deque(split_output)


def tokenize_split(split):
    tokens = []

    while split:
        if split[0] == '+':
            tokens.append(Token(TokenType.PLUS, None))
        elif split[0] == '-':
            tokens.append(Token(TokenType.MINUS, None))
        elif split[0] == '*':
            tokens.append(Token(TokenType.MULTIPLY, None))
        elif split[0] == '/':
            tokens.append(Token(TokenType.DIVIDE, None))
        elif split[0] == '(':
            tokens.append(Token(TokenType.LPAREN, None))
        elif split[0] == ')':
            tokens.append(Token(TokenType.RPAREN, None))
        elif split[0].lower() == "not":
            tokens.append(Token(TokenType.NOT, None))
        elif split[0].lower() == "and":
            tokens.append(Token(TokenType.AND, None))
        elif split[0].lower() == "or":
            tokens.append(Token(TokenType.OR, None))
        elif split[0].lower() == "eq?":
            tokens.append(Token(TokenType.EQ, None))
        elif split[0].lower() == '#t':
            tokens.append(Token(TokenType.TRUE, True))
        elif split[0].lower() == '#f':
            tokens.append(Token(TokenType.FALSE, False))
        elif split[0].lower() == "define":
            tokens.append(Token(TokenType.DEFINE, None))
        elif split[0].lower() == "print":
            tokens.append(Token(TokenType.PRINT, None))
        elif split[0].lower() == "cond":
            tokens.append(Token(TokenType.COND, None))
        elif split[0].lower() == "else":
            tokens.append(Token(TokenType.ELSE, None))
        elif split[0] == '[':
            tokens.append(Token(TokenType.LCOND, None))
        elif split[0] == ']':
            tokens.append(Token(TokenType.RCOND, None))
        elif split[0].isdigit():
            tokens.append(Token(TokenType.INTEGER, int(split[0])))
        elif split[0].isalpha():
            tokens.append(Token(TokenType.NAME, split[0]))

        split.popleft()

    return tokens


def tokenize(inpt):
    return tokenize_split(custom_split(inpt))
