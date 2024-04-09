import ply.lex as lex
from prettytable import PrettyTable

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


def t_STRING(t):
    r"\"[^\"]*\" "
    t.value = t.value[1:-1]
    return t


def t_COMMENT(t):
    r"\<%.*%\>"
    pass


# Define a rule so we can track line numbers
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


# Function to find the column of a token
def find_column(input, token):
    last_cr = input.rfind("\n", 0, token.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = token.lexpos - last_cr
    return column


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
    j :: int = 0;
    x :: boolean = false;
    "sda"
    result :: int = 0;
    for (i = 0 to length(numlist))
        begin
            result = result + numlist[i];
        end
    if x < 0
        begin
            return 0;
        end
    elseif x = 0
        begin
            return result;
        end
    else
        begin
            return result;
        end
    
    return result;    
}
"""

# Give the lexer some input
lexer.input(data)

# Create a table with headers
table = PrettyTable(["Token", "Value", "Line", "Column"])

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    column = find_column(data, tok)

    # Add row to the table
    table.add_row([tok.type, tok.value, tok.lineno - 1, column])

# Print the table
print(table)
