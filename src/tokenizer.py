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
    reversed_input = list(string)[::-1]
    symbols = set(['(', ')', '[', ']', '?', '+', '-', '*', '/'])
    split_output = []

    while reversed_input:
        if reversed_input[-1] in symbols:
            split_output.append(reversed_input.pop())
        elif reversed_input[-1].isspace():
            reversed_input.pop()
        elif reversed_input[-1] == '#':
            split_output.append(reversed_input.pop() + reversed_input.pop())
        elif reversed_input[-1].isdigit() or reversed_input[-1].isalpha():
            found_string = ""

            while reversed_input[-1].isdigit() or reversed_input[-1].isalpha():
                found_string += reversed_input.pop()
            if found_string == "eq":
                found_string += reversed_input.pop()
            split_output.append(found_string)

    return split_output


def tokenize_string(string):

    if string == '+':
        return Token(TokenType.PLUS, None)
    elif string == '-':
        return Token(TokenType.MINUS, None)
    elif string == '*':
        return Token(TokenType.MULTIPLY, None)
    elif string == '/':
        return Token(TokenType.DIVIDE, None)
    elif string == '(':
        return Token(TokenType.LPAREN, None)
    elif string == ')':
        return Token(TokenType.RPAREN, None)
    elif string == "not":
        return Token(TokenType.NOT, None)
    elif string == "and":
        return Token(TokenType.AND, None)
    elif string == "or":
        return Token(TokenType.OR, None)
    elif string == "eq?":
        return Token(TokenType.EQ, None)
    elif string == '#t':
        return Token(TokenType.TRUE, True)
    elif string == '#f':
        return Token(TokenType.FALSE, False)
    elif string == "define":
        return Token(TokenType.DEFINE, None)
    elif string == "print":
        return Token(TokenType.PRINT, None)
    elif string == "cond":
        return Token(TokenType.COND, None)
    elif string == "else":
        return Token(TokenType.ELSE, None)
    elif string == '[':
        return Token(TokenType.LCOND, None)
    elif string == ']':
        return Token(TokenType.RCOND, None)
    elif string =="defun":
        return Token(TokenType.DEFUN, None)
    elif string.isdigit():
        return Token(TokenType.INTEGER, int(string))
    elif string.isalpha():
        return Token(TokenType.ID, string)


def tokenize(string_input):
    return [tokenize_string(string) for string in custom_split(string_input)]
