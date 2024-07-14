class ASTNode:
    def accept(self, visitor):
        return visitor.visit(self)

class Program(ASTNode):
    def __init__(self, prog, func, position):
        self.prog = prog
        self.func = func
        self.position = position

class Body(ASTNode):
    def __init__(self, statement, body):
        self.statement = statement
        self.body = body

class ReturnInstruction(ASTNode):
    def __init__(self, expression, position):
        self.expression = expression
        self.position = position

class WhileInstruction(ASTNode):
    def __init__(self, condition, while_statement, position):
        self.condition = condition
        self.while_statement = while_statement
        self.position = position

class ForInstruction(ASTNode):
    def __init__(self, id, start_expr, end_expr, for_statement, position):
        self.id = id
        self.start_expr = start_expr
        self.end_expr = end_expr
        self.for_statement = for_statement
        self.position = position

class Block(ASTNode):
    def __init__(self, body):
        self.body = body

class IfOrIfElseInstruction(ASTNode):
    def __init__(self, cond, if_statement, position, else_statement=None):
        self.cond = cond
        self.if_statement = if_statement
        self.position = position
        self.else_statement = else_statement

class VariableDecl(ASTNode):
    def __init__(self, id, type, position, expr=None):
        self.id = id
        self.type = type
        self.position = position
        self.expr = expr

class FunctionDef(ASTNode):
    def __init__(self, rettype, name, params, body=None, return_fn=None, position=None):
        self.rettype = rettype
        self.name = name
        self.params = params
        self.body = body
        self.return_fn = return_fn
        self.position = position

class ParametersList(ASTNode):
    def __init__(self, parameters):
        self.parameters = parameters

class Parameter(ASTNode):
    def __init__(self, type, id):
        self.type = type
        self.id = id

class ExprList(ASTNode):
    def __init__(self, exprs):
        self.exprs = exprs

class Assignment(ASTNode):
    def __init__(self, id, expr, position):
        self.id = id
        self.expr = expr
        self.position = position

class OperationOnList(ASTNode):
    def __init__(self, expr, index_expr, position):
        self.expr = expr
        self.index_expr = index_expr
        self.position = position

class TernaryExpr(ASTNode):
    def __init__(self, cond, first_expr, second_expr, position):
        self.cond = cond
        self.first_expr = first_expr
        self.second_expr = second_expr
        self.position = position

class FunctionCall(ASTNode):
    def __init__(self, id, args, position):
        self.id = id
        self.args = args
        self.position = position

class BinExpr(ASTNode):
    def __init__(self, left, op, right, position):
        self.left = left
        self.op = op
        self.right = right
        self.position = position

class SingleExpr(ASTNode):
    def __init__(self, op, expr, position):
        self.op = op
        self.expr = expr
        self.position = position

class Num(ASTNode):
    def __init__(self, value):
        self.value = value

class Var(ASTNode):
    def __init__(self, name):
        self.name = name


class Text(ASTNode):
    def __init__(self, value):
        self.value = value