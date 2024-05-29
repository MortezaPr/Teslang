import ply.yacc as yacc
from Lexer.tokens import Tokens


class Parser:
    tokens = Tokens.tokens

    def __init__(self):
        self.lexer = None
        self.parser = yacc.yacc(module=self)

    def parse(self, data, lexer):
        self.lexer = lexer
        return self.parser.parse(data, lexer=lexer.lexer)

    # Grammar rules

    def p_program(self, p):
        """program : statement_list"""
        p[0] = ('program', p[1])

    def p_statement_list(self, p):
        """statement_list : statement
                          | statement_list statement"""
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[2]]

    def p_statement(self, p):
        """statement : assignment_statement
                     | print_statement"""
        p[0] = p[1]

    def p_assignment_statement(self, p):
        """assignment_statement : ID EQ expression SEMI_COLON"""
        p[0] = ('assign', p[1], p[3])

    def p_print_statement(self, p):
        """print_statement : PRINT LPAREN expression RPAREN SEMI_COLON"""
        p[0] = ('print', p[3])

    def p_expression_binop(self, p):
        """expression : expression PLUS expression
                      | expression MINUS expression
                      | expression TIMES expression
                      | expression DIVIDE expression"""
        p[0] = (p[2], p[1], p[3])

    def p_expression_group(self, p):
        """expression : LPAREN expression RPAREN"""
        p[0] = p[2]

    def p_expression_number(self, p):
        """expression : NUMBER"""
        p[0] = ('number', p[1])

    def p_expression_id(self, p):
        """expression : ID"""
        p[0] = ('id', p[1])

    def p_error(self, p):
        if p:
            print(f"Syntax error at '{p.value}', line {p.lineno}, column {self.find_column(p)}")
        else:
            print("Syntax error at EOF")

    def find_column(self, token):
        last_cr = self.lexer.lexer.lexdata.rfind('\n', 0, token.lexpos)
        if last_cr < 0:
            last_cr = 0
        column = token.lexpos - last_cr
        return column
