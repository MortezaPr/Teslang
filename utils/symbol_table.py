# utils/symbol_table.py

class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def define(self, name, type, attributes=None):
        if name in self.symbols:
            raise Exception(f"Symbol '{name}' already defined")
        self.symbols[name] = {'type': type, 'attributes': attributes}

    def lookup(self, name):
        if name not in self.symbols:
            raise Exception(f"Symbol '{name}' not found")
        return self.symbols[name]

    def update(self, name, attributes):
        if name not in self.symbols:
            raise Exception(f"Symbol '{name}' not found")
        self.symbols[name].update(attributes)

    def __str__(self):
        return str(self.symbols)
