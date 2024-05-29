from Utils.symbol_table import SymbolTable


class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors = []

    def analyze(self, parse_tree):
        self.visit(parse_tree)
        self.display_errors()

    def visit(self, node):
        node_type = node[0]
        if node_type == 'program':
            for stmt in node[1]:
                self.visit(stmt)
        elif node_type == 'assign':
            var_name = node[1]
            value = node[2]
            if self.symbol_table.lookup(var_name) is None:
                self.symbol_table.insert(var_name, 'variable')
            self.visit(value)
        elif node_type in ('+', '-', '*', '/'):
            self.visit(node[1])
            self.visit(node[2])
        elif node_type == 'id':
            var_name = node[1]
            if self.symbol_table.lookup(var_name) is None:
                self.errors.append(f"Semantic error: Variable '{var_name}' not defined")
        elif node_type == 'number':
            pass

    def display_errors(self):
        for error in self.errors:
            print(error)
