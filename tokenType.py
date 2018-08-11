from enum import Enum


class TokenType(Enum):
    OPEN = "OPEN"
    CLOSE = "CLOSE"
    INTEGER = "INTEGER"
    PLUS = "PLUS"
    MINUS = "MINUS"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
    EQ = "EQ"
    TRUE = "TRUE"
    FALSE = "FALSE"
