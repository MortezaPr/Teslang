class Tokens(object):
    # Reserved words
    reserved = {
        "int": "INT",
        "str": "STRING",
        "bool": "BOOLEAN",
        "null": "NULL",
        "false": "FALSE",
        'auto': 'AUTO',
        'break': 'BREAK',
        'case': 'CASE',
        "true": "TRUE",
        "vector": "VECTOR",
        "if": "IF",
        "elseif": "ELSEIF",
        'continue': 'CONTINUE',
        "else": "ELSE",
        "while": "WHILE",
        "for": "FOR",
        "to": "TO",
        "begin": "BEGIN",
        "end": "END",
        "scan": "SCAN",
        "print": "PRINT",
        "list": "LIST",
        "length": "LENGTH",
        "exit": "EXIT",
        "fn": "FN",
        "as": "AS",
        "return": "RETURN",
    }

    # List of token names.
    tokens = [
                 "ID",
                 "LESS_THAN",
                 "EQ",
                 "GREATER_THAN",
                 "PLUS",
                 "MINUS",
                 "TIMES",
                 "DIVIDE",
                 "NUMBER",
                 "SEMI_COLON",
                 "DBL_COLON",
                 "LPAREN",
                 "RPAREN",
                 "LCURLYEBR",
                 "RCURLYEBR",
                 "LSQUAREBR",
                 "RSQUAREBR",
             ] + list(reserved.values())

    # Regular expression rules for simple tokens
    t_PLUS = r"\+"
    t_MINUS = r"-"
    t_TIMES = r"\*"
    t_DIVIDE = r"/"
    t_LESS_THAN = r"<"
    t_GREATER_THAN = r">"
    t_EQ = r"="
    t_LPAREN = r"\("
    t_RPAREN = r"\)"
    t_LCURLYEBR = r"\{"
    t_RCURLYEBR = r"\}"
    t_LSQUAREBR = r"\["
    t_RSQUAREBR = r"\]"
    t_SEMI_COLON = r";"
    t_DBL_COLON = r"::"

    # A regular expression rule with some action code
    def t_ID(self, t):
        r"[a-zA-Z_][a-zA-Z_0-9]*"
        t.type = self.reserved.get(t.value, "ID")  # Check for reserved words
        return t

    def t_NUMBER(self, t):
        r"\d+"
        t.value = int(t.value)
        return t

    def t_STRING(self, t):
        r"\"[^\"]*\" "
        t.value = t.value[1:-1]
        return t

    def t_COMMENT(self, t):
        r"\<%[\s\S]*?%\>"
        t.lexer.lineno += t.value.count('\n')
        pass

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r"\n+"
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore = " \t"

    # Error handling rule
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
