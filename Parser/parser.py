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
            # todo
            p[0] = Program(prog=p[2], func=p[1], position=p.lineno(1))

    def p_func(self, p):
        """func : func1
        | func2"""
        p[0] = p[1]

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
        | block
        | builtin_methods SEMI_COLON
        | function_call SEMI_COLON
        | func1
        | func2"""

        p[0] = p[1]

    def p_body(self, p):
        """body : empty
        | stmt body"""
        if len(p) == 3:
            p[0] = Body(statement=p[1], body=p[2])

    def p_return_is(self, p):
        """return_is : RETURN expr
                     | RETURN"""
        if len(p) == 3:
            p[0] = ReturnInstruction(expression=p[2], position=p.lineno(1))

    def p_while_loop(self, p):
        """while_loop : WHILE LPAREN expr RPAREN stmt"""
        p[0] = WhileInstruction(
            condition=p[3], while_statement=p[5], position=p.lineno(1)
        )

    def p_for_loop(self, p):
        """for_loop : FOR LPAREN ID EQ expr TO expr RPAREN stmt"""
        p[0] = ForInstruction(
            id=p[3],
            start_expr=p[5],
            end_expr=p[7],
            for_statement=p[9],
            position=p.lineno(1),
        )

    def p_do_while(self, p):
        """do_while : DO stmt WHILE DOUBLE_LSQUAREBR expr DOUBLE_RSQUAREBR"""
        p[0] = WhileInstruction(
            condition=p[3], while_statement=p[5], position=p.lineno(1)
        )

    def p_block(self, p):
        """block : BEGIN body END"""
        p[0] = Block(body=p[2])

    def p_single_if(self, p):
        """single_if : IF DOUBLE_LSQUAREBR  expr DOUBLE_RSQUAREBR stmt"""
        p[0] = IfOrIfElseInstruction(
            cond=p[3], if_statement=p[5], position=p.lineno(1), else_statement=None
        )

    def p_else_if(self, p):
        """else_if : IF DOUBLE_LSQUAREBR expr DOUBLE_RSQUAREBR stmt ELSE stmt"""
        p[0] = IfOrIfElseInstruction(
            cond=p[3], if_statement=p[5], position=p.lineno(1), else_statement=p[7]
        )

    def p_defvar(self, p):
        """defvar : ID DBL_COLON type
        | ID DBL_COLON type EQ expr"""
        if len(p) == 4:
            p[0] = VariableDecl(id=p[1], type=p[3], position=p.lineno(1), expr=None)
        elif len(p) == 6:
            p[0] = VariableDecl(id=p[1], type=p[3], position=p.lineno(1), expr=p[5])

    def p_type(self, p):
        """type : INT
        | STRING
        | VECTOR
        | NULL
        | BOOLEAN"""
        p[0] = p[1]

    def p_func1(self, p):
        """func1 : FN ID LPAREN flist RPAREN LESS_THAN type GREATER_THAN LCURLYEBR body RCURLYEBR"""
        p[0] = FunctionDef(
            rettype=p[7], name=p[2], params=p[4], body=p[10], position=p.lineno(1)
        )

    def p_func2(self, p):
        """func2 :  FN ID LPAREN flist RPAREN LESS_THAN type GREATER_THAN EQ GREATER_THAN return_is"""
        p[0] = FunctionDef(
            rettype=p[7], name=p[2], params=p[4], return_fn=p[11], position=p.lineno(1)
        )

    def p_flist(self, p):
        """flist : empty
        | ID AS type
        | ID  AS type COMMA flist"""
        if len(p) == 3:
            p[0] = ParametersList(parameters=[Parameter(type=p[3], id=p[1])])
        if len(p) == 5:
            p[0] = ParametersList(
                parameters=p[5].parameters + [Parameter(type=p[3], id=p[1])]
            )

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
        """expr : on_list
        | expr_list
        | ternary_expr
        | binary_expr
        | single_expr
        | ID
        | assignment
        | function_call
        | NUMBER
        | STRING
        | NULL
        | LPAREN expr RPAREN"""
        if len(p) == 4 or len(p) == 3:
            if p[1] == "-":
                p[2].value = -p[2].value
            elif p[1] == "!":
                if p[2].value:
                    p[2].value = 0
                else:
                    p[2].value = 1
            p[0] = p[2]
        else:
            if p.slice[1].type in ("number", "iden", "string"):
                p[0] = p.slice[1]
            else:
                p[0] = p[1]

    def p_assignment_expr(self, p):
        """assignment : ID EQ expr
                    | on_list EQ expr"""
        p[0] = Assignment(id=p[1], expr=p[3], position=p.lineno(1))

    def p_on_list(self, p):
        """on_list : expr LSQUAREBR expr RSQUAREBR"""
        p[0] = OperationOnList(expr=p[1], index_expr=p[3], position=p.lineno(1))

    def p_expr_list(self, p):
        """expr_list : LSQUAREBR clist RSQUAREBR"""
        p[0] = p[2]

    def p_ternary_expr(self, p):
        """ternary_expr : expr QUESTION_MARK expr COLON expr"""
        p[0] = TernaryExpr(
            cond=p[1], first_expr=p[2], second_expr=p[3], position=p.lineno(1)
        )

    def p_function_call(self, p):
        """function_call : ID LPAREN clist RPAREN
                        | builtin_methods"""
        if len(p) == 4:
            p[0] = FunctionCall(id=p[1], args=None, position=p.lineno(1))
        elif len(p) == 5:
            p[0] = FunctionCall(id=p[1], args=p[3], position=p.lineno(1))

    def p_binary_expr(self, p):
        """binary_expr :  expr PLUS expr
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
        | expr OR expr"""
        p[0] = BinExpr(left=p[1], op=p[2], right=p[3], position=p.lineno(1))


    def p_single_expr(self, p):
        """ single_expr : NOT expr
        | PLUS expr
        | MINUS expr"""

        p[0] = SingleExpr(op=p[1], expr=p[2], position=p.lineno(1))

    def p_builtin_methods(self, p):
        """builtin_methods : SCAN LPAREN RPAREN
        | PRINT LPAREN clist RPAREN
        | LENGTH LPAREN clist RPAREN
        | EXIT LPAREN clist RPAREN
        | LIST LPAREN NUMBER RPAREN"""
        if len(p) == 4:
            p[0] = FunctionCall(id=p[1], args=None, position=p.lineno(1))
        elif len(p) == 5:
            p[0] = FunctionCall(id=p[1], args=p[3], position=p.lineno(1))

    # ------- Error ------------------
    def p_single_if_error(self, p):
        """single_if : IF LCURLYEBR error RCURLYEBR stmt"""
        print("Invalid syntax for if statement at line", p.lineno(1))

    def p_while_loop_error(self, p):
        """while_loop : WHILE LPAREN error RPAREN stmt"""
        print("Invalid expression for while loop at line", p.lineno(1))

    def p_error(slef, p):
        if p:
            print(
                f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'"
            )
        else:
            print("Syntax error: Unexpected end of input")

    # You might want to raise an exception or handle the error in some other way

    def p_func1_rtype_error(self, p):
        """func1_rtype : FN ID LPAREN flist RPAREN LESS_THAN error GREATER_THAN LCURLYEBR body RCURLYEBR"""
        print(
            "missing or invalid return type for function "
            + p[2].value
            + " at line "
            + (p.lineno(1)).__str__()
        )
        p[0] = FunctionDef(
            rettype=p[7], name=p[2], params=p[4], body=p[10], position=p.lineno(1)
        )

    def p_func2_rtype_error(self, p):
        """func2_rtype :  FN ID LPAREN flist RPAREN LESS_THAN error GREATER_THAN EQ GREATER_THAN return_is"""
        print(
            "missing or invalid return type for function "
            + p[2].value
            + " at line "
            + (p.lineno(1)).__str__()
        )
        p[0] = FunctionDef(
            rettype=p[7], name=p[2], params=p[4], return_fn=p[11], position=p.lineno(1)
        )

    def p_func_flist_error(self, p):
        """func_flist : FN ID LPAREN error RPAREN  LCURLYEBR body RCURLYEBR"""
        print("invalid arguments for function " + p[3] + "at line: " + (p.lineno(1)))
        p[0] = FunctionDef(
            rettype=p[2], name=p[3], params=None, body=p[8], position=p.lineno(1)
        )

    def p_else_if_error(self, p):
        """else_if : IF DOUBLE_LSQUAREBR error DOUBLE_RSQUAREBR stmt ELSE stmt"""
        print("invalid statement for else if at line " + p.lineno(1))

    def p_for_loop_error(self, p):
        """for_loop : FOR LPAREN ID EQ error TO expr RPAREN stmt
        | FOR LPAREN ID EQ expr TO error RPAREN stmt
        | FOR LPAREN ID EQ error TO error RPAREN stmt"""
        print("invalid expression(s) for 'for' at line " + p.lineno(1))

    def p_defvar_type_error(self, p):
        """defvar_type : ID DBL_COLON error
        | ID DBL_COLON error EQ expr"""
        print("invalid type for 'def var' at line " + p.lineno(1))
        if len(p) == 4:
            p[0] = VariableDecl(id=p[1], type=p[3], position=p.lineno(1), expr=None)
        elif len(p) == 6:
            p[0] = VariableDecl(id=p[1], type=p[3], position=p.lineno(1), expr=p[5])

    def p_flist_type_error(self, p):
        """flist : ID AS error
        | ID AS error COMMA flist"""
        print("invalid type for argument list in line: " + p.lineno(1))
        if len(p) == 3:
            p[0] = ParametersList(parameters=[Parameter(type=p[3], id=p[1])])
        if len(p) == 5:
            p[0] = ParametersList(
                parameters=p[5].parameters + [Parameter(type=p[3], id=p[1])]
            )

    def p_flist_iden_error(self, p):
        """flist : error AS type
        | error AS type COMMA flist"""
        print("invalid id for argument list in line: " + (p.lineno(1)))
        if len(p) == 3:
            p[0] = ParametersList(parameters=[Parameter(type=p[3], id=p[1])])
        if len(p) == 5:
            p[0] = ParametersList(
                parameters=p[5].parameters + [Parameter(type=p[3], id=p[1])]
            )

    def p_flist_flist_error(self, p):
        """flist : ID AS type COMMA error"""
        print("invalid flist for argument list in line: " + p.lineno(1))
        if len(p) == 3:
            p[0] = ParametersList(parameters=[Parameter(type=p[3], id=p[1])])
        if len(p) == 5:
            p[0] = ParametersList(
                parameters=p[5].parameters + [Parameter(type=p[3], id=p[1])]
            )
