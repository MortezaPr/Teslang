from lexer.tokens import Tokens
from lexer.lexer import Lexer
from parser.parser import Parser
from semantic_checker.semantic_analyzer import SemanticAnalyzer
from utils.ir_generator import IRGenerator


def compile_source(code):
    try:
        tokens = Tokens()
        lexer = Lexer(tokens)

        parser = Parser()

        lexer.build(code)

        try:
            parse_tree = parser.parse(code, lexer)
            print("Parse Tree:", parse_tree)  # Print the parse tree for debugging
        except Exception as e:
            print(f"Parser Error: {e}")

        try:
            analyzer = SemanticAnalyzer()
            analyzer.visit(parse_tree)
            print("Semantic analysis completed successfully.")
            print("Symbol Table:", analyzer.symbol_table)
        except Exception as e:
            print(f"Semantic Error: {e}")

        try:
            ir_generator = IRGenerator()
            ir_generator.visit(parse_tree)
            for ir in ir_generator.ir:
                print(ir)
        except:
            print(f"IR Generation Error: {e}")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    with open("teslang_source.txt") as f:
        compile_source(f.read())
