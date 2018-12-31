from parseNode import ParseNode


definitions = {}


class DefineNode(ParseNode):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

    def __str__(self):
        return "DefineNode(" + str(self.name) + ", " + str(self.expr) + ")"

    def evaluate(self):
        definitions[self.name] = self.expr.evaluate()


class NumberNode(ParseNode):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return "NumberNode(" + str(self.number) + ")"

    def evaluate(self):
        return self.number


class BooleanNode(ParseNode):
    def __init__(self, boolean):
        self.boolean = boolean

    def __str__(self):
        return "BooleanNode(" + str(self.boolean) + ")"

    def evaluate(self):
        return self.boolean


class PrintNode(ParseNode):
    def __init__(self, expr):
        self.expr = expr

    def __str__(self):
        return "PrintNode(" + str(self.expr) + ")"

    def evaluate(self):
        print(self.expr.evaluate())


class BinaryFunctionNode(ParseNode):
    def __init__(self, func, expr1, expr2):
        self.func = func
        self.expr1 = expr1
        self.expr2 = expr2

    def __str__(self):
        return "BinaryFunctionNode(" + str(self.expr1) + ", " + str(self.expr2) + ")"

    def evaluate(self):
        return self.func(self.expr1.evaluate(), self.expr2.evaluate())


class UnaryFunctionNode(ParseNode):
    def __init__(self, func, expr):
        self.func = func
        self.expr = expr

    def __str__(self):
        return "UnaryFunctionNode(" + str(self.expr) + ")"

    def evaluate(self):
        return self.func(self.expr.evaluate())