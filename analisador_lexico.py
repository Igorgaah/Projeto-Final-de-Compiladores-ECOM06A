import ply.lex as lex

# Lista de tokens
tokens = [
    'ID', 'INT_CONST', 'FLOAT_CONST', 'STRING',
    'GALO', 'BOI', 'SUB', 'MUL', 'DIV', 'MOD',
    'GT', 'LT', 'EQ'
]

# Palavras reservadas (selos)
reserved = {
    'Tigre': 'TIGRE',
    'Cobra': 'COBRA',
    'Rato': 'RATO',
    'Dragao': 'DRAGAO',
    'Cavalo': 'CAVALO',
    'Carneiro': 'CARNEIRO',
    'Macaco': 'MACACO',
    'Cao': 'CAO'
}

tokens += list(reserved.values())

# Ignora espaços e tabulações
t_ignore = ' \t'

# Tokens definidos como funções
def t_GALO(t):
    r'Galo'
    return t

def t_BOI(t):
    r'Boi'
    return t

def t_SUB(t):
    r'-'
    return t

def t_MUL(t):
    r'\*'
    return t

def t_DIV(t):
    r'/'
    return t

def t_MOD(t):
    r'%'
    return t

def t_GT(t):
    r'>'
    return t

def t_LT(t):
    r'<'
    return t

def t_EQ(t):
    r'=='
    return t

def t_FLOAT_CONST(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT_CONST(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"[^"\n]*"'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comment(t):
    r'\/\/.*'
    pass

def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Símbolos usados diretamente no parser
literals = [';', '{', '}', '(', ')']

# Cria o analisador léxico
lexer = lex.lex()
