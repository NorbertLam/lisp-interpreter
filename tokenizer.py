from tokenType import TokenType
from parse import evaluate, alias


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
    pairing = {}

    while i < len(inpt):
        if tokens and tokens[-1].type == TokenType.DEFINE:
            i += 1
            name = ""

            while inpt[i].isalpha():
                name += inpt[i]
                i += 1

            if not inpt[i].isalpha():
                i -= 1
            value = evaluate(tokenize("(" + inpt[i:]))
            pairing[name] = value
            alias[name] = value
            tokens.append(Token(TokenType.NAME, (name, value)))
        else:
            if inpt[i].isdigit():
                num = ""

                while inpt[i].isdigit():
                    num += str(inpt[i])
                    i += 1

                if not inpt[i].isdigit():
                    i -= 1
                if tokens[-1].type != TokenType.NAME:
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
            elif inpt[i] == 'n'and inpt[i + 1] == 'o' and inpt[i + 2] == 't':
                tokens.append(Token(TokenType.NOT, None))
                i += 2
            elif inpt[i] == 'a' and inpt[i + 1] == 'n' and inpt[i + 2] == 'd':
                tokens.append(Token(TokenType.AND, None))
                i += 2
            elif inpt[i] == 'o' and inpt[i + 1] == 'r':
                tokens.append(Token(TokenType.OR, None))
                i += 1
            elif inpt[i] == 'e'and inpt[i + 1] == 'q' and inpt[i + 2] == '?':
                tokens.append(Token(TokenType.EQ, None))
                i += 2
            elif inpt[i] == '#':
                if inpt[i + 1] == 't':
                    tokens.append(Token(TokenType.TRUE, None))
                elif inpt[i + 1] == 'f':
                    tokens.append(Token(TokenType.FALSE, None))
                i += 1
            elif inpt[i] == 'd' and "define" in ''.join(inpt[i:i+6]):
                tokens.append(Token(TokenType.DEFINE, None))
                i += 5
            elif inpt[i] == 'p' and 'print' in ''.join(inpt[i:i+5]):
                tokens.append(Token(TokenType.PRINT, None))
                i += 4
            elif inpt[i] == 'c' and 'cond' in ''.join(inpt[i:i+4]):
                tokens.append(Token(TokenType.COND, None))
                i += 3
            elif inpt[i] == 'e' and 'else' in ''.join(inpt[i:i+4]):
                tokens.append(Token(TokenType.ELSE, None))
                i += 3
            elif inpt[i] == '[':
                tokens.append(Token(TokenType.LEFT, None))
            elif inpt[i] == ']':
                tokens.append(Token(TokenType.RIGHT, None))
            elif inpt[i].isalpha():
                identity = ""

                while inpt[i].isalpha():
                    identity += str(inpt[i])
                    i += 1

                if not inpt[i].isdigit():
                    i -= 1

                if identity in pairing:
                    tokens.append(Token(TokenType.ID, pairing[identity]))
                else:
                    if identity in alias:
                        tokens.append(Token(TokenType.ID, alias[identity]))
            i += 1

    return tokens
