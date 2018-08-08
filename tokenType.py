from enum import Enum


class TokenType(Enum):
    OPEN = "OPEN"
    CLOSE = "CLOSE"
    INTEGER = "INTEGER"
    PLUS = "PLUS"
    MINUS = "MINUS"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
