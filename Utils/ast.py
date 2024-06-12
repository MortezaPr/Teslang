class Node:
    def __init__(self, position: int):
        """
        Base class for all nodes in the AST.

        :param position: Position of the node in the source code.
        """
        self.position = position

    def accept(self, visitor):
        """
        Accepts a visitor that processes this node.

        :param visitor: The visitor instance.
        """
        className = self.__class__.__name__
        method = getattr(visitor, "visit_" + className, None)
        if method:
            return method(self)
        else:
            raise Exception(f"No visit_{className} method in visitor")


class Program(Node):
    def __init__(self, func: "FunctionDef", prog: "Program", position: int):
        """
        Represents a program consisting of functions and possibly other programs.

        :param func: The function definition.
        :param prog: Another program (for chaining programs).
        :param position: Position of the node in the source code.
        """
        super().__init__(position)
        self.func = func
        self.prog = prog


class Body(Node):
    def __init__(self, statement, body: "Body"):
        """
        Represents a body consisting of a statement and potentially another body.

        :param statement: The statement within the body.
        :param body: Another body (for chaining bodies).
        """
        self.statement = statement
        self.body = body


class ReturnInstruction(Node):
    def __init__(self, expression: "Node", position: int):
        """
        Represents a return instruction.

        :param expression: The expression to return.
        :param position: Position of the node in the source code.
        """
        super().__init__(position)
        self.expression = expression


class WhileInstruction(Node):
    def __init__(self, condition: "Node", while_statement: "Node", position: int):
        """
        Represents a while loop instruction.

        :param condition: The condition to evaluate.
        :param while_statement: The statement to execute while the condition is true.
        :param position: Position of the node in the source code.
        """
        super().__init__(position)
        self.condition = condition
        self.while_statement = while_statement


class ForInstruction(Node):
    def __init__(
        self,
        id: str,
        start_expr: "Node",
        end_expr: "Node",
        for_statement: "Node",
        position: int,
    ):
        """
        Represents a for loop instruction.

        :param id: The identifier for the loop variable.
        :param start_expr: The starting expression.
        :param end_expr: The ending expression.
        :param for_statement: The statement to execute in the loop.
        :param position: Position of the node in the source code.
        """
        super().__init__(position)
        self.id = id
        self.start_expr = start_expr
        self.end_expr = end_expr
        self.for_statement = for_statement


class DoWhileInstruction(Node):
    def __init__(self, while_statement: "Node", condition: "Node", position: int):
        """
        Represents a do-while loop instruction.

        :param while_statement: The statement to execute in the loop.
        :param condition: The condition to evaluate after the statement execution.
        :param position: Position of the node in the source code.
        """
        super().__init__(position)
        self.condition = condition
        self.while_statement = while_statement


class Block(Node):
    def __init__(self, body: "Body"):
        """
        Represents a block of code.

        :param body: The body of the block.
        """
        self.body = body


class IfOrIfElseInstruction(Node):
    def __init__(
        self,
        cond: "Node",
        if_statement: "Node",
        position: int,
        else_statement: "Node" = None,
    ):
        """
        Represents an if or if-else instruction.


        :param cond: The condition to evaluate.
        :param if_statement: The statement to execute if the condition is true.
        :param else_statement: The statement to execute if the condition is false.
        :param position: Position of the node in the source code.
        """
        super().__init__(position)
        self.cond = cond
        self.if_statement = if_statement
        self.else_statement = else_statement


class VariableDecl(Node):
    def __init__(self, id: str, type: str, position: int, expr: "Node" = None):
        """
        Represents a variable declaration.

        :param id: The identifier of the variable.
        :param type: The type of the variable.
        :param position: Position of the node in the source code.
        :param expr: The expression assigned to the variable.
        """
        super().__init__(position)
        self.id = id
        self.type = type
        self.expr = expr


class FunctionDef(Node):
    def __init__(
        self,
        rettype: str,
        name: str,
        params: "ParametersList",
        position: int,
        body: "Block" = None,
        return_fn: "ReturnInstruction" = None,
    ):
        """
        Represents a function definition.

        :param rettype: The return type of the function.
        :param name: The name of the function.
        :param params: The list of parameters for the function.
        :param position: Position of the node in the source code.
        :param body: The body of the function.
        :param return_fn: The return statement of the function.
        """
        super().__init__(position)
        self.rettype = rettype
        self.name = name
        self.fmlparams = params
        self.body = body
        self.return_fn = return_fn


class ParametersList(Node):
    def __init__(self, parameters: list["Parameter"]):
        """
        Represents a list of parameters.

        :param parameters: The parameters in the list.
        """
        self.parameters = parameters

    def __str__(self) -> str:
        return str(self.parameters)


class Parameter(Node):
    def __init__(self, type: str, id: str):
        """
        Represents a parameter in a function definition.

        :param type: The type of the parameter.
        :param id: The identifier of the parameter.
        """
        self.type = type
        self.id = id


class ExprList(Node):
    def __init__(self, exprs: list["Node"]):
        """
        Represents a list of expressions.

        :param exprs: The expressions in the list.
        """
        self.exprs = exprs


class Assignment(Node):
    def __init__(self, id: str, expr: "Node", position: int):
        """
        Represents an assignment operation.

        :param id: The identifier of the variable being assigned.
        :param expr: The expression assigned to the variable.
        :param position: Position of the node in the source code.
        """
        super().__init__(position)
        self.id = id
        self.expr = expr


class OperationOnList(Node):
    def __init__(self, expr: "Node", index_expr: "Node", position: int):
        """
        Represents an operation on a list element.

        :param expr: The list expression.
        :param index_expr: The index expression.
        :param position: Position of the node in the source code.
        """
        super().__init__(position)
        self.expr = expr
        self.index_expr = index_expr


class TernaryExpr(Node):
    def __init__(
        self, cond: "Node", first_expr: "Node", second_expr: "Node", position: int
    ):
        """
        Represents a ternary expression.

        :param cond: The condition to evaluate.
        :param first_expr: The expression if the condition is true.
        :param second_expr: The expression if the condition is false.
        :param position: Position of the node in the source code.
        """
        super().__init__(position)
        self.cond = cond
        self.first_expr = first_expr
        self.second_expr = second_expr


class FunctionCall(Node):
    def __init__(self, id: str, args: "ExprList", position: int):
        """
        Represents a function call.

        :param id: The identifier of the function being called.
        :param args: The arguments to the function.
        :param position: Position of the node in the source code.
        """
        super().__init__(position)
        self.id = id
        self.args = args


class BinExpr(Node):
    def __init__(self, left: "Node", op: str, right: "Node", position: int):
        """
        Represents a binary expression.

        :param left: The left-hand side of the expression.
        :param op: The operator.
        :param right: The right-hand side of the expression.
        :param position: Position of the node in the source code.
        """
        super().__init__(position)
        self.left = left
        self.op = op
        self.right = right

class SingleExpr(Node):
    def __init__(self, op, expr, position: int):
        super().__init__(position)
        self.op = op
        self.expr = expr


class Integer(Node):
    def __init__(self, value: int, position: int):
        """
        Represents an integer constant.

        :param value: The integer value.
        :param position: Position of the node in the source code.
        """
        super().__init__(position)
        self.value = value


class String(Node):
    def __init__(self, value: str, position: int):
        """
        Represents a string constant.

        :param value: The string value.
        :param position: Position of the node in the source code.
        """
        super().__init__(position)
        self.value = value


class Float(Node):
    def __init__(self, value: float, position: int):
        """
        Represents a float constant.

        :param value: The float value.
        :param position: Position of the node in the source code.
        """
        super().__init__(position)
        self.value = value


class ErrorNode(Node):
    def __init__(self, message: str, position: int):
        """
        Represents an error node.

        :param message: The error message.
        :param position: Position of the node in the source code.
        """
        super().__init__(position)
        self.message = message
