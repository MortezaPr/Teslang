class SymbolTable:
    def __init__(self, parent=None):
        self.symbols = {}
        self.parent = parent

    def insert(self, name, symbol_type):
        if name in self.symbols:
            raise Exception(f"Variable '{name}' is already defined")
        self.symbols[name] = symbol_type

    def lookup(self, name):
        if name in self.symbols:
            return self.symbols[name]
        elif self.parent:
            return self.parent.lookup(name)
        return None

    def enter_scope(self):
        return SymbolTable(self)

    def exit_scope(self):
        return self.parent
