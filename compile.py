from Lexer.tokens import Tokens
from Lexer.lexer import Lexer
from Parser.parser import Parser
from Semantic.semantic_analyzer import SemanticAnalyzer


def compile_teslang(code):
    tokens = Tokens()
    lexer = Lexer(tokens)
    parser = Parser()

    # First Step: Lexical Analysis
    # lexer.build(code)

    # Second Step: Parsing
    parse_tree = parser.parse(code, lexer)


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