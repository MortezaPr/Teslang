import ply.yacc as yacc
from Lexer.tokens import Tokens
from Utils.ast import *


class Parser:
    tokens = Tokens.tokens

    def __init__(self):
        self.lexer = None
        self.parser = yacc.yacc(module=self)

    def parse(self, data, lexer):
        self.lexer = lexer
        return self.parser.parse(data, lexer=lexer.lexer)

    def p_prog(self, p):
        """prog : empty 
                | func prog"""
        if len(p) == 3:
            #todo
            p[0] = Program(prog=p[2], func=p[1], position=p.lineno(1))

    def p_empty(self, p):
        """empty :"""
        pass
        p[0] = []

    def p_stmt(self, p):
        """stmt : expr SEMI_COLON
                | defvar SEMI_COLON
                | func SEMI_COLON
                | single_if
                | else_if
                | while_loop
                | for_loop
                | do_while
                | return_is SEMI_COLON
                | block"""
        
        p[0] = p[1]

    def p_body(self, p):
        """body : empty
            | stmt body"""
        if len(p) == 3:
            p[0] = Body(statement=p[1], body=p[2])

    def p_return_is(self, p):
        """return_is : RETURN expr"""
        p[0] = ReturnInstruction(expression=p[2], position=p.lineno(1))

    def p_while_loop(self, p):
        """while_loop : WHILE LPAREN expr RPAREN stmt"""
        p[0] = WhileInstruction(condition=p[3], while_statement=p[5], position=p.lineno(1))

    def p_for_loop(self, p):
        """for_loop : FOR LPAREN ID EQ expr TO expr RPAREN stmt"""
        p[0] = ForInstruction(id=p[3], start_expr=p[5], end_expr=p[7], for_statement=p[9],
                                position=p.lineno(1))

    def p_do_while(self, p):
        """do_while : DO stmt WHILE DOUBLE_LSQUAREBR expr DOUBLE_RSQUAREBR"""
        p[0] = WhileInstruction(condition=p[3], while_statement=p[5], position=p.lineno(1))

    def p_block(self, p):
        """block : BEGIN body END"""
        p[0] = Block(body=p[2])

    def p_single_if(self, p):
        """single_if : IF DOUBLE_LSQUAREBR  expr DOUBLE_RSQUAREBR stmt"""
        p[0] = IfOrIfElseInstruction(cond=p[3], if_statement=p[5], position=p.lineno(1), else_statement=None)

    def p_else_if(self, p):
        """else_if : IF DOUBLE_LSQUAREBR expr DOUBLE_RSQUAREBR stmt ELSE stmt"""
        p[0] = IfOrIfElseInstruction(cond=p[3], if_statement=p[5], pos=p.lineno(1), else_statement=p[7])

    def p_defvar(self, p):
        """defvar : ID DBL_COLON type
                    | ID DBL_COLON type EQ expr"""
        if len(p) == 4:
            p[0] = VariableDecl(id=p[1], type=p[3], pos=p.lineno(1), expr=None)
        elif len(p) == 6:
            p[0] = VariableDecl(id=p[1], type=p[3], pos=p.lineno(1), expr=p[5])
        
    def p_type(self, p):
        """type : INT
                | STRING
                | VECTOR
                | NULL
                | BOOLEAN"""
        p[0] = p[1]

    def p_func1(self, p):
        """func : FN ID LPAREN flist RPAREN LESS_THAN type GREATER_THAN LCURLYEBR body RCURLYEBR"""
        p[0] = FunctionDef(rettype=p[7], name=p[2], params=p[4], body=p[10], pos=p.lineno(1))

    def p_func2(self, p):
        """func :  FN ID LPAREN flist RPAREN LESS_THAN type GREATER_THAN EQ GREATER_THAN return_is"""
        p[0] = FunctionDef(rettype=p[7], name=p[2], params=p[4], return_fn=p[11], pos=p.lineno(1))

    def p_flist(self, p):
        """flist : empty
                | ID AS type
                | ID  AS type COMMA flist"""
        if len(p) == 3:
            p[0] = ParametersList(parameters=[Parameter(type=p[3], id=p[1])])
        if len(p) == 5:
            p[0] = ParametersList(parameters=p[5].parameters + [Parameter(type=p[3], id=p[1])])
        
    def p_clist(self, p):
        """clist : empty
                | expr
                | expr COMMA clist"""
        if len(p) == 2:
            if p[1] == []:
                exprs = []
            else:
                exprs = [p[1]]
                p[0] = ExprList(exprs=exprs)
        elif len(p) == 4:
            p[0] = ExprList(exprs=p[3].exprs + [p[1]])

    
    def p_expr(self, p):
        """expr : expr LSQUAREBR expr RSQUAREBR
                | LSQUAREBR clist RSQUAREBR
                | expr QUESTION_MARK expr COLON expr
                | expr PLUS expr
                | expr MINUS expr
                | expr TIMES expr
                | expr DIVIDE expr
                | expr GREATER_THAN expr
                | expr LESS_THAN expr
                | expr DOUBLE_EQ expr
                | expr GREATER_THAN_EQ expr
                | expr LESS_THAN_EQ expr
                | expr NOT_EQ expr
                | expr AND expr
                | expr OR expr
                | NOT expr
                | PLUS expr
                | MINUS expr
                | ID
                | ID EQ expr
                | ID LPAREN clist RPAREN
                | NUMBER
                | STRING"""
        if len(p) == 4 or len(p) == 3:
            if p[1] == '-':
                p[2].value = -p[2].value
            elif p[1] == '!':
                if p[2].value:
                    p[2].value = 0
                else:
                    p[2].value = 1
            p[0] = p[2]
        else:
            if p.slice[1].type in ('number', 'iden', 'string'):
                p[0] = p.slice[1]
            else:
                p[0] = p[1]


def p_expr_assignment(self, p):
    """assignment :  iden equal expr"""
    p[0] = Assignment(id=p[1], expr=p[3], pos=p.lineno(1))

    
        
    # def find_column(self, token):
    #     last_cr = self.lexer.lexer.lexdata.rfind('\n', 0, token.lexpos)
    #     if last_cr < 0:
    #         last_cr = 0
    #     column = token.lexpos - last_cr
    #     return column
