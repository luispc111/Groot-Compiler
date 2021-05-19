# Luis Alberto Pérez Chapa
# A01282564

# GROOT LANGUAGE
# LEXER / PARSER

import ply.lex as lex
import ply.yacc as yacc
import sys

############### LEXER ###############

# TOKENS
tokens = [

    # Palabras reservadas
    'PROGRAMA',     # Programa
    'VARIABLES',    # variables
    'FUNCION',     # Funcion
    'PRINCIPAL',    # Principal
    'REGRESA',      # Regresa
    
    # Read / Write
    'LEER',         # Leer
    'ESCRIBIR',     # Escribir

    # If condition
    'SI',           # si
    'ENTONCES',     # entonces
    'SINO',         # sino

    # While loop
    'MIENTRAS',     # Mientras
    'HACER',        # Hacer

    # For loop
    'DESDE',        # Desde
    'HASTA',        # Hasta
    #'HACER' (ya declarado)

    # Signos
    'PUNTOYCOMA',   # ;
    'COMA',         # ,
    'DOSPUNTOS',    # :
    'PUNTO',        # .

    # Separadores
    'L_LLAVE',      # {
    'R_LLAVE',      # }
    'L_PAR',        # (
    'R_PAR',        # )
    'L_CORCHETE',   # [
    'R_CORCHETE',   # ]

    # Operadores
    'IGUAL',        # =
    'MAS',          # +
    'MENOS',        # -
    'MULT',         # *
    'DIV',          # /
    'AND',          # &
    'OR',           # |
    'MENORQUE',        # <
    'MAYORQUE',        # >
    'MENORIGUALQUE',     # <=
    'MAYORIGUALQUE',     # >=
    'DIFQUE',       # !=
    'IGUALQUE',      # ==

    # Tokens complejos
    #'DIGITO',
    'ENTEROVAL',
    'FLOTANTEVAL',
    'CARACTERVAL',
    'LETRERO',

    # Tipos
    'ENTERO',       # entero
    'FLOTANTE',     # flotante
    'CARACTER',     # caracter
    'VOID',         # void

    # Funciones reservadas
    'CIRCULO',      # Circulo
    'COLOR',        # Color
    'GROSOR',       # Grosor
    'LINEA',        # Linea
    'PUNTOXY',      # PuntoXY
    'ARCO',         # Arco
    'PENUP',        # PenUp
    'PENDOWN',      # PenDown

    'ID',           # id
]

# DEFINICIONES

# Palabras reservadas
t_PROGRAMA = r'Programa'
t_VARIABLES = r'Variables'
t_FUNCION = r'Funcion'
t_PRINCIPAL = r'Principal'
t_REGRESA = r'Regresa'

# Read / Write
t_LEER = r'Leer'
t_ESCRIBIR = r'Escribir'

# If condition
t_SI = r'Si'
t_ENTONCES = r'Entonces'
t_SINO = r'Sino'

# While loop
t_MIENTRAS = r'Mientras'
t_HACER = r'Hacer'

# For loop
t_DESDE = r'Desde'
t_HASTA = r'Hasta'
# t_HACER (ya declarado)

# Signos
t_PUNTOYCOMA = r'\;'
t_COMA = r'\,'
t_DOSPUNTOS = r'\:'
t_PUNTO = r'\.'

# Separadores
t_L_LLAVE = r'\{'
t_R_LLAVE = r'\}'
t_L_PAR = r'\('
t_R_PAR = r'\)'
t_L_CORCHETE = r'\['
t_R_CORCHETE = r'\]'

# Operadores
t_IGUAL = r'\='
t_MAS = r'\+'
t_MENOS = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'
t_AND = r'\&'
t_OR = r'\|'
t_MENORQUE = r'\<'
t_MAYORQUE = r'\>'
t_MENORIGUALQUE = r'\<\='
t_MAYORIGUALQUE = r'\>\='
t_DIFQUE = r'\!\='
t_IGUALQUE = r'\=\='

# Tokens complejos
#t_DIGITO = r'[0-9]'
t_ENTEROVAL  = r'[-]?[0-9]+'
t_FLOTANTEVAL = r'[-]?[0-9]+([.][0-9]+)'
t_CARACTERVAL = r'(\'[^\']\')'
t_LETRERO = r'\"[\w\d\s\,. ]*\"'

# Tipos
t_ENTERO = r'Entero'
t_FLOTANTE = r'Flotante'
t_CARACTER = r'Caracter'
t_VOID = r'Void'

# Funciones especiales
t_CIRCULO = r'Circulo'  # (radio)
t_COLOR = r'Color'      # (r,g,b)
t_GROSOR = r'Grosor'    # (pixeles)
t_LINEA = r'Linea'      # (x1,y1,x2,y2)
t_PUNTOXY = r'PuntoXY'  # (x,y)
t_ARCO = r'Arco'
t_PENUP = r'PenUp'
t_PENDOWN = r'PenDown'

t_ID = r'([a-z][a-zA-Z0-9]*)'

# Tabs
t_ignore = ' \t'

# REFERENCIA: https://www.dabeaz.com/ply/ply.html#ply_nn12
# Contar lineas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# REFERENCIA: https://www.dabeaz.com/ply/ply.html#ply_nn12
# Errores de lexer
def t_error(t):
    print("Illegal character '%s' at line '%d'" % (t.value[0], t.lexer.lineno))
    t.lexer.skip(1)
    #sys.exit("Illegal character '%s'" % t.value[0])

lexer = lex.lex()

#Funcion para probar el escaner lexico 
# def pruebaLex():
#     #lexer.input("Programa Variables Funcion Principal Regresa Leer Escribir Si Hacer Sino Mientras Hacer Desde Hasta ; , : . { } ( ) [ ] = + - * / < > <= >= != == 1 101 10.5 'a' \"Hola\" Entero Flotante Caracter Void Circulo Color Grosor Linea PuntoXY Arco PenUp PenDown cantCrayones")
#     lexer.input("PROGRAMA groot;")
#     while True:
#         tok = lexer.token()
#         if not tok:
#             break
#         print(tok)

# pruebaLex()

############### PARSER ###############

def p_programa(p):
    '''
    program : PROGRAMA ID PUNTOYCOMA variables funciones PRINCIPAL L_PAR R_PAR bloque empty
    '''

def p_variales(p):
    '''
    variables : VARIABLES variablesU
              | empty

    variablesU : variablesD
               | empty
    
    variablesD : ID COMA variablesD
               | ID DOSPUNTOS tipo_var PUNTOYCOMA variablesU
    '''

def p_funciones(p):
    '''
    funciones : funcionesU
              | empty
    
    funcionesU : tipo_funcion FUNCION ID L_PAR recibir_parametros R_PAR variables bloque funcionesD
    
    funcionesD : funciones
               | empty
    '''

def p_tipo_funcion(p):
    '''
    tipo_funcion : ENTERO empty
                 | FLOTANTE empty
                 | CARACTER empty
                 | VOID empty
    '''

def p_tipo_var(p):
    '''
    tipo_var : ENTERO empty
             | FLOTANTE empty
             | CARACTER empty
    '''

def p_recibir_parametros(p):
    '''
    recibir_parametros : ID DOSPUNTOS tipo_var recibir_parametrosD empty
                       | empty

    recibir_parametrosD : COMA recibir_parametros empty
                       | empty
    '''

def p_mandar_parametros(p):
    '''
    mandar_parametros : ID mandar_parametrosD empty
                      | empty

    mandar_parametrosD : COMA mandar_parametros empty
                       | empty
    '''

# BLOQUE Y EXPRESIONES

def p_bloque(p):
    '''
    bloque : L_LLAVE bloqueU R_LLAVE empty

    bloqueU : estatuto bloqueD empty
            | empty

    bloqueD : bloqueU empty
            | empty
    '''

def p_estatuto(p):
    '''
    estatuto : asignacion PUNTOYCOMA empty
             | llamada PUNTOYCOMA empty
             | retorno PUNTOYCOMA empty
             | lectura PUNTOYCOMA empty
             | escritura PUNTOYCOMA empty
             | decision empty
             | condicional empty
             | no_condicional empty
             | funciones_especiales PUNTOYCOMA empty
             | empty
    '''

def p_asignacion(p):
    '''
    asignacion : ID IGUAL hiper_exp empty
    '''

def p_llamada(p):
    '''
    llamada : ID L_PAR mandar_parametros R_PAR empty
    '''

def p_retorno(p):
    '''
    retorno : REGRESA L_PAR ID R_PAR empty
    '''

def p_lectura(p):
    '''
    lectura : LEER L_PAR ID R_PAR empty
    '''

def p_escritura(p):
    '''
    escritura : ESCRIBIR L_PAR escrituraD R_PAR empty

    escrituraD : hiper_exp empty
               | LETRERO empty
    '''

def p_decision(p):
    '''
    decision : SI L_PAR hiper_exp R_PAR ENTONCES bloque SINO bloque empty
    '''

def p_condicional(p):
    '''
    condicional : MIENTRAS L_PAR hiper_exp R_PAR HACER bloque empty
    '''

def p_no_condicional(p):
    '''
    no_condicional : DESDE L_PAR asignacion R_PAR HASTA hiper_exp HACER bloque empty
    '''

# FUNCIONES ESPECIALES

def p_funciones_especiales(p):
    '''
    funciones_especiales : circulo empty
                         | color empty
                         | grosor empty
                         | linea empty
                         | puntoxy empty
                         | arco empty
                         | penup empty
                         | pendown empty
                         | empty
    '''

def p_circulo(p):
    '''
    circulo : CIRCULO L_PAR hiper_exp R_PAR empty
    '''

def p_color(p):
    '''
    color : COLOR L_PAR hiper_exp R_PAR empty
    '''

def p_grosor(p):
    '''
    grosor : GROSOR L_PAR hiper_exp R_PAR empty
    '''

def p_linea(p):
    '''
    linea : LINEA L_PAR hiper_exp COMA hiper_exp COMA hiper_exp COMA hiper_exp R_PAR empty
    '''

def p_puntoxy(p):
    '''
    puntoxy : PUNTOXY L_PAR hiper_exp COMA hiper_exp R_PAR empty
    '''

def p_arco(p):
    '''
    arco : ARCO L_PAR hiper_exp R_PAR empty
    '''

def p_penup(p):
    '''
    penup : PENUP L_PAR hiper_exp R_PAR empty
    '''

def p_pendown(p):
    '''
    pendown : PENDOWN L_PAR hiper_exp R_PAR empty
    '''

# OPERADORES 

def p_operadorA(p): 
    '''
    operadorA : MAS empty
              | MENOS empty
    '''

def p_operadorT(p): 
    '''
    operadorT : MULT empty
              | DIV empty
    '''

def p_operadorL(p): 
    '''
    operadorL : OR empty
              | AND empty
    '''

def p_operadorR(p): 
    '''
    operadorR : MENORQUE empty
              | MAYORQUE empty
              | MENORIGUALQUE empty
              | MAYORIGUALQUE empty
              | IGUALQUE empty
              | DIFQUE empty
    '''

# EXPRESIONES

def hiper_exp():
    '''
    hiper_exp : super_exp hiper_expU

    hiper_expU : operadorL hiper_exp empty 
               | empty
    '''

def super_exp():
    '''
    super_exp : exp super_expU

    super_expU : operadorR exp empty 
               | empty
    '''

def exp():
    '''
    exp : termino expU

    expU : operadorA exp
         | empty
    '''

def termino():
    '''
    termino : factor terminoU

    terminoU : operadorT termino
             | empty
    '''

def factor():
    '''
    factor : varcte empty
           | llamada empty
           | L_PAR hiper_exp R_PAR empty
    '''

# VARCTE / ERROR / EMPTY

def p_varcte(p):
    '''
    varcte  : ID empty
            | ENTEROVAL empty
            | FLOTANTEVAL empty
            | CARACTERVAL empty
    '''

def p_error(p):
    print("Syntax error found at line %d." % (lexer.lineno))

def p_empty(p):
    '''
    empty : 
    '''

parser = yacc.yacc()

try:
        text = input('Prueba.txt: ')
        with open(text, 'r') as file:
            parser.parse(file.read())
except EOFError:
    print("Error")