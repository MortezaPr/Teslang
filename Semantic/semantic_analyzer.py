from Utils.symbol_table import SymbolTable

# SemanticAnalyzer.py


class SemanticAnalyzer:
    def __init__(self):
        self.errors = []
        self.symbol_table = SymbolTable()

    def analyze(self, node):
        """
        Start the analysis from the root node.
        """

        return node.accept(self)

    def visit_Program(self, node):
        """
        Visit a Program node.
        """
        if node.func:
            self.analyze(node.func)
        if node.prog:
            self.analyze(node.prog)

    def visit_FunctionDef(self, node):
        """
        Visit a Function Definition node.
        """
        if node.body:
            self.analyze(node.body)
        if node.return_fn:
            self.analyze(node.return_fn)

    def visit_Block(self, node):
        """
        Visit a Block node.
        """
        self.analyze(node.body)

    def visit_Body(self, node):
        """
        Visit a Body node.
        """
        self.analyze(node.statement)
        print(node)
        if node.body:
            self.analyze(node.body)

    def visit_ReturnInstruction(self, node):
        """
        Visit a Return Instruction node.
        """
        self.analyze(node.expression)

    def visit_WhileInstruction(self, node):
        """
        Visit a While Instruction node.
        """
        self.analyze(node.condition)
        self.analyze(node.while_statement)

    def visit_ForInstruction(self, node):
        """
        Visit a For Instruction node.
        """
        self.analyze(node.start_expr)
        self.analyze(node.end_expr)
        self.analyze(node.for_statement)

    def visit_DoWhileInstruction(self, node):
        """
        Visit a DoWhile Instruction node.
        """
        self.analyze(node.while_statement)
        self.analyze(node.condition)

    def visit_IfOrIfElseInstruction(self, node):
        """
        Visit an IfOrIfElse Instruction node.
        """
        self.analyze(node.cond)
        self.analyze(node.if_statement)
        if node.else_statement:
            self.analyze(node.else_statement)

    def visit_VariableDecl(self, node):
        """
        Visit a Variable Declaration node.
        """
        if node.expr:
            self.analyze(node.expr)

    def visit_Assignment(self, node):
        """
        Visit an Assignment node.
        """
        self.analyze(node.expr)

    def visit_OperationOnList(self, node):
        """
        Visit an Operation On List node.
        """
        self.analyze(node.expr)
        self.analyze(node.index_expr)

    def visit_TernaryExpr(self, node):
        """
        Visit a Ternary Expression node.
        """
        self.analyze(node.cond)
        self.analyze(node.first_expr)
        self.analyze(node.second_expr)

    def visit_FunctionCall(self, node):
        """
        Visit a Function Call node.
        """
        self.analyze(node.args)

    def visit_BinExpr(self, node):
        """
        Visit a Binary Expression node.
        """
        self.analyze(node.left)
        self.analyze(node.right)

    def visit_SingleExpr(self, node):
        """
        Visit a Single Expression node.
        """
        self.analyze(node.expr)

    def visit_Integer(self, node):
        """
        Visit an Integer node.
        """
        pass  # Nothing to do for simple types

    def visit_String(self, node):
        """
        Visit a String node.
        """
        pass  # Nothing to do for simple types

    def visit_Float(self, node):
        """
        Visit a Float node.
        """
        pass  # Nothing to do for simple types

    def visit_ErrorNode(self, node):
        """
        Visit an Error Node.
        """
        self.errors.append(node.message)
