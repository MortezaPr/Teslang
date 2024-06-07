# class SymbolTable:
#     def __init__(self, parent=None):
#         self.symbols = {}
#         self.parent = parent

#     def insert(self, name, symbol_type):
#         if name in self.symbols:
#             raise Exception(f"Variable '{name}' is already defined")
#         self.symbols[name] = symbol_type

#     def lookup(self, name):
#         if name in self.symbols:
#             return self.symbols[name]
#         elif self.parent:
#             return self.parent.lookup(name)
#         return None

#     def enter_scope(self):
#         return SymbolTable(self)

#     def exit_scope(self):
#         return self.parent


class Symbol:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"<{self.name}>"


class VariableSymbol(Symbol):
    def __init__(self, type, name, assigned=False):
        super().__init__(name)
        self.type = type
        self.assigned = assigned
        self.register = None

    def set_register(self, register):
        self.register = register


class FunctionSymbol(Symbol):
    redefined = False

    def __init__(self, rettype, name, params):
        super().__init__(name)
        self.rettype = rettype
        self.params = params

    def __str__(self):
        return f"<{self.name} : {self.rettype}({self.params})>"


class SymbolTable:
    def __init__(self, parent=None):
        self.symbols = {}
        self.parent = parent

    def insert(self, symbol):
        if symbol.name in self.symbols:
            raise Exception(f"Symbol '{symbol.name}' is already defined")
        self.symbols[symbol.name] = symbol

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

    def mark_as_defined(self, name):
        if name in self.symbols:
            self.symbols[name].redefined = True

    def print_symbols(self):
        for key in self.symbols:
            print(key, self.symbols[key])


# Example usage
if __name__ == "__main__":
    global_table = SymbolTable()

    # Adding a variable symbol to the global scope
    var_symbol = VariableSymbol("int", "x", True)
    global_table.insert(var_symbol)

    # Adding a function symbol to the global scope
    func_params = ["int a", "int b"]
    func_symbol = FunctionSymbol("int", "add", func_params)
    global_table.insert(func_symbol)

    # Entering the first local scope
    first_local_table = global_table.enter_scope()

    # Adding a variable in the first local scope
    local_var_symbol = VariableSymbol("int", "y")
    first_local_table.insert(local_var_symbol)

    # Entering a nested local scope within the first local scope
    nested_local_table = first_local_table.enter_scope()

    # Adding a variable in the nested local scope
    nested_local_var_symbol = VariableSymbol("int", "z")
    nested_local_table.insert(nested_local_var_symbol)

    # Lookup for symbols
    print(global_table.lookup("x"))  # Should find 'x'
    print(first_local_table.lookup("x"))  # Should find 'x' in the parent (global) scope
    print(first_local_table.lookup("y"))  # Should find 'y' in the first local scope
    print(
        nested_local_table.lookup("x")
    )  # Should find 'x' in the parent (global) scope
    print(
        nested_local_table.lookup("y")
    )  # Should find 'y' in the parent (first local) scope
    print(nested_local_table.lookup("z"))  # Should find 'z' in the nested local scope

    # Exiting nested local scope
    nested_local_table = nested_local_table.exit_scope()
    print(
        nested_local_table.lookup("z")
    )  # Should return None as 'z' is not in the first local scope

    # Exiting first local scope
    first_local_table = first_local_table.exit_scope()
    print(
        first_local_table.lookup("y")
    )  # Should return None as 'y' is not in the global scope
