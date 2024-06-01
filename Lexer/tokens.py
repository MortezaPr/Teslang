class Tokens(object):
    # Reserved words
    reserved = {
        "int": "INT",
        "str": "STRING",
        "boolean": "BOOLEAN",
        "false": "FALSE",
        "true": "TRUE",
        "vector": "VECTOR",
        "if": "IF",
        "elseif": "ELSEIF",
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
        "null": "NULL",
        "do": "DO"
    }

    # List of token names.
    tokens = [
        "ID",
        "LESS_THAN",
        "LESS_THAN_EQ",
        "EQ",
        "GREATER_THAN",
        "GREATER_THAN_EQ",
        "PLUS",
        "MINUS",
        "TIMES",
        "DIVIDE",
        "NUMBER",
        "SEMI_COLON",
        "COMMA",
        "DBL_COLON",
        "COLON",
        "LPAREN",
        "RPAREN",
        "LCURLYEBR",
        "RCURLYEBR",
        "LSQUAREBR",
        "DOUBLE_LSQUAREBR",
        "DOUBLE_RSQUAREBR",
        "RSQUAREBR",
        "QUESTION_MARK",
        "AND",
        "OR",
        "DOUBLE_EQ",
        "NOT_EQ",
        "NOT"
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
    t_LESS_THAN_EQ = r"<="
    t_GREATER_THAN_EQ = r">="
    t_COMMA = r","
    t_COLON = r":"
    t_DOUBLE_LSQUAREBR = r"\[\["
    t_DOUBLE_RSQUAREBR = r"\]\]"
    t_QUESTION_MARK = r"\?"
    t_AND = r"&&"
    t_OR = r"\|\|"
    t_DOUBLE_EQ = r"=="
    t_NOT_EQ = r"!="
    t_NOT = r"!"

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
        r"\"([^\\\n]|(\\.))*?\"|'([^\\\n]|(\\.))*?'"
        t.value = t.value[1:-1].encode().decode('unicode_escape')  # Handle escape sequences
        return t

    def t_COMMENT(self, t):
        r"\<%[\s\S]*?%\>"
        t.lexer.lineno += t.value.count("\n")
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