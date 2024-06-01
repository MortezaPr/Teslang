from Lexer.tokens import Tokens
from Lexer.lexer import Lexer
from Parser.grammar import Parser
from Semantic.semantic_analyzer import SemanticAnalyzer


def compile_teslang(code):
    tokens = Tokens()
    lexer = Lexer(tokens)
    # parser = Parser()

    lexer.build(code)
    # parse_tree = parser.parse(code, lexer)
    #
    # if parse_tree:
    #     analyzer = SemanticAnalyzer()
    #     analyzer.analyze(parse_tree)


if __name__ == "__main__":
    with open("./Tests/code.txt") as f:
        data = f.read()
        f.close()
    compile_teslang(data)