# semantic_checker/semantic_analyzer.py

from utils.symbol_table import SymbolTable


class NodeVisitor:
    def visit(self, node):
        if node is None:
            return
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f'No visit_{type(node).__name__} method')


class SemanticAnalyzer(NodeVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.current_function = None

    def visit_Program(self, node):
        self.visit(node.func)
        if node.prog:
            self.visit(node.prog)

    def visit_FunctionDef(self, node):
        self.symbol_table.define(node.name, node.rettype, {'params': node.params.parameters})
        self.current_function = node
        self.visit(node.params)
        if node.body:
            self.visit(node.body)
        elif node.return_fn:
            self.visit(node.return_fn)
        # self.current_function = None

    def visit_Body(self, node):
        self.visit(node.statement)
        if node.body:
            self.visit(node.body)

    def visit_ReturnInstruction(self, node):
        if not self.current_function:
            raise Exception("Return statement not inside a function")
        expr_type = self.visit(node.expression)
        if not (
                expr_type == "int" and self.current_function.rettype == "bool") and expr_type != self.current_function.rettype:
            raise Exception(f"Return type mismatch: expected {self.current_function.rettype}, got {expr_type}")

    def visit_WhileInstruction(self, node):
        self.visit(node.condition)
        self.visit(node.while_statement)

    def visit_ForInstruction(self, node):
        self.visit(node.start_expr)
        self.visit(node.end_expr)
        self.visit(node.for_statement)

    def visit_Block(self, node):
        self.visit(node.body)

    def visit_IfOrIfElseInstruction(self, node):
        self.visit(node.cond)
        self.visit(node.if_statement)
        if node.else_statement:
            self.visit(node.else_statement)

    def visit_VariableDecl(self, node):
        if node.id in self.symbol_table.symbols:
            raise Exception(f"Variable '{node.id}' already declared")
        self.symbol_table.define(node.id, node.type)
        if node.expr:
            expr_type = self.visit(node.expr)
            if expr_type != node.type:
                raise Exception(f"Type mismatch in declaration of '{node.id}': expected {node.type}, got {expr_type}")

    def visit_ParametersList(self, node):
        for param in node.parameters:
            self.visit(param)

    def visit_Parameter(self, node):
        if node.id in self.symbol_table.symbols:
            raise Exception(f"Parameter '{node.id}' already declared")
        self.symbol_table.define(node.id, node.type)

    def visit_Assignment(self, node):
        if node.id not in self.symbol_table.symbols:
            raise Exception(f"Variable '{node.id}' not declared")
        var_type = self.symbol_table.lookup(node.id)['type']
        expr_type = self.visit(node.expr)
        if var_type != expr_type:
            raise Exception(f"Type mismatch in assignment to '{node.id}': expected {var_type}, got {expr_type}")

    def visit_OperationOnList(self, node):
        self.visit(node.expr)
        self.visit(node.index_expr)

    def visit_TernaryExpr(self, node):
        self.visit(node.cond)
        expr1_type = self.visit(node.first_expr)
        expr2_type = self.visit(node.second_expr)
        if expr1_type != expr2_type:
            raise Exception(f"Type mismatch in ternary expression: {expr1_type} vs {expr2_type}")
        return expr1_type

    def visit_FunctionCall(self, node):
        func = self.symbol_table.lookup(node.id)
        if not func:
            raise Exception(f"Function '{node.id}' not declared")
        expected_params = func['attributes']['params']
        if len(node.args.exprs) != len(expected_params):
            raise Exception(f"Argument count mismatch in call to '{node.id}'")
        for arg, param in zip(node.args.exprs, expected_params):
            arg_type = self.visit(arg)
            if arg_type != param.type:
                raise Exception(f"Type mismatch in call to '{node.id}': expected {param.type}, got {arg_type}")
        return func['type']

    def visit_ExprList(self, node):
        for expr in node.exprs:
            self.visit(expr)

    def visit_BinExpr(self, node):
        left_type = self.visit(node.left)
        right_type = self.visit(node.right)
        if left_type != right_type:
            raise Exception(f"Type mismatch in binary expression: {left_type} vs {right_type}")
        return left_type

    def visit_SingleExpr(self, node):
        expr_type = self.visit(node.expr)
        return expr_type

    def visit_Num(self, node):
        return 'int'

    def visit_Var(self, node):
        if node.name not in self.symbol_table.symbols:
            raise Exception(f"Variable '{node.name}' not declared")
        return self.symbol_table.lookup(node.name)['type']

    def visit_Text(self, node):
        return 'str'
