class Node:
    def __init__(self, position):
        self.position = position


class Program(Node):
    def __init__(self, func, prog, position):
        super().__init__(position)
        self.func = func
        self.prog = prog


class Body(Node):
    def __init__(self, statement, body):
        self.statement = statement
        self.body = body

class ReturnInstruction(Node):
    def __init__(self, expression, position):
        super().__init__(position)
        self.expression = expression

class WhileInstruction(Node):
    def __init__(self, condition, while_statement, position):
        super().__init__(position)
        self.condition = condition
        self.while_statement = while_statement

class ForInstruction(Node):
    def __init__(self, id, start_expr, end_expr, for_statement, position):
        super().__init__(position)
        self.id = id
        self.start_expr = start_expr
        self.end_expr = end_expr
        self.for_statement = for_statement

class DoWhileInstruction(Node):
    def __init__(self, while_statement, condition, position):
        super().__init__(position)
        self.condition = condition
        self.while_statement = while_statement

class Block(Node):
    def __init__(self, body):
        self.body = body


class IfOrIfElseInstruction(Node):
    def __init__(self, cond, if_statement, position, else_statement=None):
        super().__init__(position)
        self.cond = cond
        self.if_statement = if_statement
        self.else_statement = else_statement

class VariableDecl(Node):
    def __init__(self, id, type, position, expr=None):
        super().__init__(position)
        self.id = id
        self.type = type
        self.expr = expr

class FunctionDef(Node):
    def __init__(self, rettype, name, params, position, body=None, return_fn=None):
        super().__init__(position)        
        self.rettype = rettype
        self.name = name
        self.fmlparams = params
        self.body = body
        self.return_fn = return_fn

class ParametersList(Node):
    def __init__(self, parameters):
        self.parameters = parameters
    def __str__(self) -> str:
        return str(self.parameters)
    
class Parameter(Node):
    def __init__(self, type, id):
        self.type = type
        self.id = id

class ExprList(Node):
    def __init__(self, exprs):
        self.exprs = exprs

class Assignment(Node):
    def __init__(self, id, expr, pos):
        self.id = id
        self.expr = expr
        self.pos = pos