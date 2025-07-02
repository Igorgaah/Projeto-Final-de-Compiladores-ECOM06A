import ply.yacc as yacc
from analisador_lexico import tokens

# Classe para representar nós da árvore sintática
class Node:
    def __init__(self, type, children=None, value=None):
        self.type = type
        self.children = children or []
        self.value = value

    def __repr__(self):
        return f'{self.type}({self.value})' if self.value else f'{self.type}({self.children})'


# Regra inicial
def p_programa(p):
    'programa : decls comandos'
    p[0] = Node("programa", [p[1], p[2]])


# Declarações
def p_decls_mult(p):
    'decls : decl ";" decls'
    p[0] = Node("decls", [p[1]] + p[3].children)

def p_decls_empty(p):
    'decls : '
    p[0] = Node("decls", [])


# Declaração com ou sem atribuição
def p_decl(p):
    '''decl : tipo ID
            | tipo ID GALO expr'''
    if len(p) == 3:
        p[0] = Node("decl", value=(p[1], p[2]))
    else:
        tipo = p[1]
        nome = p[2]
        valor = p[4]
        p[0] = Node("decl_assign", [
            Node("decl", value=(tipo, nome)),
            Node("assign", [valor], nome)
        ])


def p_tipo(p):
    '''tipo : CARNEIRO
            | MACACO
            | CAO'''
    p[0] = p[1]


# Comandos
def p_comandos_mult(p):
    'comandos : comando ";" comandos'
    p[0] = Node("comandos", [p[1]] + p[3].children)

def p_comandos_empty(p):
    'comandos : '
    p[0] = Node("comandos", [])

def p_comando_print(p):
    'comando : TIGRE expr'
    p[0] = Node("print", [p[2]])

def p_comando_input(p):
    'comando : COBRA ID'
    p[0] = Node("input", value=p[2])

def p_comando_atribuicao(p):
    'comando : ID GALO expr'
    p[0] = Node("assign", [p[3]], p[1])

def p_comando_if_else(p):
    'comando : RATO expr "{" comandos "}" DRAGAO "{" comandos "}"'
    p[0] = Node("if_else", [p[2], p[4], p[8]])

def p_comando_while(p):
    'comando : CAVALO expr "{" comandos "}"'
    p[0] = Node("while", [p[2], p[4]])


# Expressões
def p_expr_binop(p):
    '''expr : expr BOI expr
            | expr SUB expr
            | expr MUL expr
            | expr DIV expr
            | expr MOD expr
            | expr GT expr
            | expr LT expr
            | expr EQ expr'''
    p[0] = Node("binop", [p[1], p[3]], p[2])

def p_expr_group(p):
    'expr : "(" expr ")"'
    p[0] = p[2]

def p_expr_const(p):
    '''expr : INT_CONST
            | FLOAT_CONST
            | STRING'''
    p[0] = Node("const", value=p[1])

def p_expr_id(p):
    'expr : ID'
    p[0] = Node("id", value=p[1])


# Literais utilizados diretamente no parser
literals = [';', '{', '}', '(', ')']


# Tratamento de erro sintático
def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno}: token inesperado '{p.value}'")
    else:
        print("Erro de sintaxe: fim de arquivo inesperado")


# Construção do parser
parser = yacc.yacc()
