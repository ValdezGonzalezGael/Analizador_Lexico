import lex as lex

reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'True' : 'TRUE',
    'False' : 'FALSE',
    'None' : 'NONE',
    'class' : 'CLASS',
    'break' : 'BREAK',
    'for' : 'FOR',
    'return' : 'RETURN',
    'try' : 'TRY',
    'as' : 'AS',
    'and' : 'AND',
    'async' : 'ASYNC'
 }

# List of token names.   This is always required

tokens = [
    'PALAB',
    'NUMERO',
    'MAS',
    'MENOS',
    'BARRA_INV',
    'BARRA_VER',
    'PUNTO',
    'INTERRO',
    'ASTERISCO',
    'DIV',
    'PARENT_APER',
    'PARENT_CIERRE',
    'LLAVE_APER',
    'LLAVE_CIERRE',
] + list(reserved.values())

# Regular expression rules for simple tokens
t_PALAB = r'[a-zA-Z_][a-zA-Z_]*'
t_MAS = r'\+'
t_MENOS = r'-'
t_BARRA_INV = r'\\'
t_BARRA_VER = r'\|'
t_PUNTO = r'\.'
t_INTERRO = r'\?'
t_ASTERISCO = r'\*'
t_DIV = r'/'
t_PARENT_APER = r'\('
t_PARENT_CIERRE = r'\)'
t_LLAVE_APER = r'\{'
t_LLAVE_CIERRE = r'\}'


# A regular expression rule with some action code
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# String
def t_ccode_string(t):
    r'\"([^\\\n]|(\\.))*?\"'

def t_COMMENT(t):
     r'\#.*'
     pass
     # No return value. Token discarded

# Error handling rule
def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Function read file 
# Test it out
file = open ('content.txt')

data = file.read()

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break  # No more input 
    print(tok)
