import ply.lex as lex

# Reserved words
reserved = {
    "if": "IF",
    "then": "THEN",
    "else": "ELSE",
    "while": "WHILE",
    "for": "FOR",
    "begin": "BEGIN",
    "end": "END",
    "to": "TO",
    "as": "AS",
    "len": "LEN",
    "return": "RETURN",
    "int": "INT",
    "vector": "VECTOR",
    "str": "STRING",
    "fn": "FN",
    "as": "AS",
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
def t_ID(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = reserved.get(t.value, "ID")  # Check for reserved words
    return t


def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_COMMENT(t):
    r"\<%.*%\>"
    pass


# Define a rule so we can track line numbers
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = " \t"


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()


# Test it out
data = """
fn sum(numlist as vector) <int> {
    <% This is a comment %>
    i :: int = 0;
    result :: int = 0;
    for (i = 0 to length(numlist))
        begin
            result = result + numlist[i];
        end
    return result;    
}
"""

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
