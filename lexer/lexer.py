import ply.lex as lex
from prettytable import PrettyTable


class Lexer(object):
    def __init__(self, tokens):
        self.lexer = lex.lex(object=tokens)

    # Function to find the column of a token
    def find_column(self, input, token):
        last_cr = input.rfind("\n", 0, token.lexpos)
        if last_cr < 0:
            last_cr = 0
        column = token.lexpos - last_cr + 1
        return column

    def build(self, data):
        # Give the lexer some input
        self.lexer.input(data)
        # Create a table with headers
        table = PrettyTable(["Token", "Value", "Line", "Column"])
        # Tokenize
        for tok in self.lexer:
            column = self.find_column(data, tok)
            table.add_row([tok.type, tok.value, tok.lineno, column])

        # print(table)
