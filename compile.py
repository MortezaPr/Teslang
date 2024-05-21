from Lexer.lexer import Lexer
from Lexer.tokens import Tokens


class Compiler(object):
    def __init__(self, data):
        self.data = data

        # Create instance of Tokens with lexer_messages as an argument
        self.tokens = Tokens()

        # Create instance of Lexer with tokens as an argument
        self.lexer = Lexer(self.tokens)

    def compile(self):
        self.lexer.build(self.data)


if __name__ == '__main__':
    with open("./Test/code.txt") as f:
        data = f.read()
        f.close()
    compiler = Compiler(data)
    compiler.compile()
