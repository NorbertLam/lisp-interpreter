from parseNode import ParseNode


class DefineNode(ParseNode):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

    def __str__(self):
        return "DefineNode(" + str(self.name) + ", " + str(self.expr) + ")"


class PrintNode(ParseNode):
    def __init__(self, expr):
        self.expr = expr

    def __str__(self):
        return "PrintNode(" + str(self.expr) + ")"


class BinaryFunctionNode(ParseNode):
    def __init__(self, func, expr1, expr2):
        self.func = func
        self.expr1 = expr1
        self.expr2 = expr2

    def __str__(self):
        return "BinaryFunctionNode(" + str(self.expr1) + ", " + str(self.expr2) + ")"


class UnaryFunctionNode(ParseNode):
    def __init__(self, func, expr):
        self.func = func
        self.expr = expr

    def __str__(self):
        return "UnaryFunctionNode(" + str(self.expr) + ")"
