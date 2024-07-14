# IR/ir_generator.py
from semantic_checker.semantic_analyzer import NodeVisitor
from utils.ir import *

class IRGenerator(NodeVisitor):
    def __init__(self):
        self.ir = []
        self.temp_count = 0
        self.current_function = None
        self.current_ir = None

    def new_temp(self):
        self.temp_count += 1
        return f"r{self.temp_count}"

    def visit_Program(self, node):
        node.func.accept(self)
        if node.prog:
            node.prog.accept(self)

    def visit_FunctionDef(self, node):
        params = [param.id for param in node.params.parameters]
        body = []
        self.current_ir = body
        self.current_function = node.name

        # Emit the function prologue
        function_ir = IRFunction(node.name, params, body)
        self.ir.append(function_ir)

        if node.body:
            node.body.accept(self)
        elif node.return_fn:
            node.return_fn.accept(self)

    def visit_Body(self, node):
        node.statement.accept(self)
        if node.body:
            node.body.accept(self)

    def visit_ReturnInstruction(self, node):
        value = node.expression.accept(self)
        self.current_ir.append(IRReturn(value))

    def visit_WhileInstruction(self, node):
        start_label = self.new_temp()
        end_label = self.new_temp()
        condition = node.condition.accept(self)

        self.current_ir.append(IRLabel(start_label))
        self.current_ir.append(IRConditionalGoto(condition, end_label))
        node.while_statement.accept(self)
        self.current_ir.append(IRGoto(start_label))
        self.current_ir.append(IRLabel(end_label))

    def visit_ForInstruction(self, node):
        # Simplified version for IR generation
        start_label = self.new_temp()
        end_label = self.new_temp()
        start_expr = node.start_expr.accept(self)
        end_expr = node.end_expr.accept(self)

        self.current_ir.append(IRAssignment(node.id, start_expr))
        self.current_ir.append(IRLabel(start_label))
        condition = f"{node.id} <= {end_expr}"
        self.current_ir.append(IRConditionalGoto(condition, end_label))
        node.for_statement.accept(self)
        self.current_ir.append(IRAssignment(node.id, f"{node.id} + 1"))
        self.current_ir.append(IRGoto(start_label))
        self.current_ir.append(IRLabel(end_label))

    def visit_Block(self, node):
        node.body.accept(self)

    def visit_IfOrIfElseInstruction(self, node):
        else_label = self.new_temp()
        end_label = self.new_temp()
        condition = node.cond.accept(self)
        self.current_ir.append(IRConditionalGoto(condition, else_label))
        node.if_statement.accept(self)
        self.current_ir.append(IRGoto(end_label))
        self.current_ir.append(IRLabel(else_label))
        if node.else_statement:
            node.else_statement.accept(self)
        self.current_ir.append(IRLabel(end_label))

    def visit_VariableDecl(self, node):
        if node.expr:
            value = node.expr.accept(self)
            self.current_ir.append(IRAssignment(node.id, value))

    def visit_ParametersList(self, node):
        for param in node.parameters:
            param.accept(self)

    def visit_Assignment(self, node):
        value = node.expr.accept(self)
        self.current_ir.append(IRAssignment(node.id, value))

    def visit_OperationOnList(self, node):
        expr = node.expr.accept(self)
        index_expr = node.index_expr.accept(self)
        result = self.new_temp()
        self.current_ir.append(IRBinaryOperation("[]", expr, index_expr, result))
        return result

    def visit_TernaryExpr(self, node):
        first_expr = node.first_expr.accept(self)
        second_expr = node.second_expr.accept(self)
        condition = node.cond.accept(self)
        result = self.new_temp()
        self.current_ir.append(IRConditionalGoto(condition, first_expr))
        self.current_ir.append(IRAssignment(result, second_expr))
        return result

    def visit_FunctionCall(self, node):
        args = [arg.accept(self) for arg in node.args.exprs]
        result = self.new_temp()
        self.current_ir.append(IRFunctionCall(node.id, args, result))
        return result

    def visit_ExprList(self, node):
        return [expr.accept(self) for expr in node.exprs]

    def visit_BinExpr(self, node):
        left = node.left.accept(self)
        right = node.right.accept(self)
        result = self.new_temp()
        self.current_ir.append(IRBinaryOperation(node.op, left, right, result))
        return result

    def visit_SingleExpr(self, node):
        operand = node.expr.accept(self)
        result = self.new_temp()
        self.current_ir.append(IRUnaryOperation(node.op, operand, result))
        return result

    def visit_Num(self, node):
        return str(node.value)

    def visit_Var(self, node):
        return node.name
