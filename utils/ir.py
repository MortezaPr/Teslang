# utils/ir.py

class IRNode:
    def __init__(self):
        self.id = None  # Unique ID for each IR node, useful for debugging

class IRFunction(IRNode):
    def __init__(self, name, params, body):
        super().__init__()
        self.name = name
        self.params = params
        self.body = body

    def __str__(self):
        body_str = "\n".join(str(instr) for instr in self.body)
        return f"proc {self.name}\n{body_str}\n"

class IRInstruction(IRNode):
    pass

class IRBinaryOperation(IRInstruction):
    def __init__(self, op, left, right, result):
        super().__init__()
        self.op = op
        self.left = left
        self.right = right
        self.result = result

    def __str__(self):
        return f"{self.op} {self.result}, {self.left}, {self.right}"

class IRUnaryOperation(IRInstruction):
    def __init__(self, op, operand, result):
        super().__init__()
        self.op = op
        self.operand = operand
        self.result = result

    def __str__(self):
        return f"{self.op} {self.result}, {self.operand}"

class IRAssignment(IRInstruction):
    def __init__(self, variable, value):
        super().__init__()
        self.variable = variable
        self.value = value

    def __str__(self):
        return f"mov {self.variable}, {self.value}"

class IRReturn(IRInstruction):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def __str__(self):
        return f"ret {self.value}"

class IRLabel(IRInstruction):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return f"label {self.name}"

class IRGoto(IRInstruction):
    def __init__(self, label):
        super().__init__()
        self.label = label

    def __str__(self):
        return f"goto {self.label}"

class IRConditionalGoto(IRInstruction):
    def __init__(self, condition, label):
        super().__init__()
        self.condition = condition
        self.label = label

    def __str__(self):
        return f"if {self.condition} goto {self.label}"

class IRFunctionCall(IRInstruction):
    def __init__(self, function_name, args, result=None):
        super().__init__()
        self.function_name = function_name
        self.args = args
        self.result = result

    def __str__(self):
        args_str = ", ".join(self.args)
        if self.result:
            return f"call {self.function_name}, {self.result}, {args_str}"
        else:
            return f"call {self.function_name}, {args_str}"
