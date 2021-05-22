# Luis Alberto Pérez Chapa
# A01282564

# GROOT LANGUAGE
# LEXER / PARSER

# IMPORTS

import ply.lex as lex
import ply.yacc as yacc
import sys

from collections import deque

from CuboSemantico import *
from Cuadruplo import *

############### GLOBAL VARIABLES ###############

progName = ''

currFuncName = ''
currFuncType = ''

currVarName = ''
currVarType = ''

# Memorias

memoriaGEntero = 1000
memoriaGFlotante = 2000
memoriaGCaracter = 3000

memoriaLEntero = 4000
memoriaLFlotante = 5000
memoriaLCaracter = 6000

memoriaCEntero = 7000
memoriaCFlotante = 8000
memoriaCCaracter = 9000

varsStack = deque()

pilaOperadores = deque()
pilaTerminos = deque()
pilaTipos = deque()

# Diccionario que contendra las variables (y funciones) y las constantes junto con sus tipos
tabla_variables = {}
tabla_constantes = {'Entero': {}, 'Flotante': {}, 'Caracter': {}}

# Arreglo que se llenará con objetos tipo Cuadruplo
cuadruplos = []

# Arreglo que se llenará con los errores
errores = []

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
    'MENORQUE',     # <
    'MAYORQUE',     # >
    'MENORIGUALQUE',    # <=
    'MAYORIGUALQUE',    # >=
    'DIFQUE',       # !=
    'IGUALQUE',     # ==

    # Tokens complejos
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
t_COLOR = r'Color'      # (i)
t_GROSOR = r'Grosor'    # (i)
t_LINEA = r'Linea'      # (x1,y1,x2,y2)
t_PUNTOXY = r'PuntoXY'  # (x,y)
t_ARCO = r'Arco'        # (i)
t_PENUP = r'PenUp'      # ()
t_PENDOWN = r'PenDown'  # ()

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

# Funcion para probar el escaner lexico 
# def pruebaLex():
#     lexer.input("Programa Variables Funcion Principal Regresa Leer Escribir Si Hacer Sino Mientras Hacer Desde Hasta ; , : . { } ( ) [ ] = + - * / < > <= >= != == 1 101 10.5 'a' \"Hola\" Entero Flotante Caracter Void Circulo Color Grosor Linea PuntoXY Arco PenUp PenDown cantCrayones")
#     #lexer.input("PROGRAMA groot;")
#     while True:
#         tok = lexer.token()
#         if not tok:
#             break
#         print(tok)

# pruebaLex()

############### PARSER ###############

def p_programa(p):
    '''
    program : PROGRAMA ID neu_programa PUNTOYCOMA variables funciones PRINCIPAL neu_principal L_PAR R_PAR bloque empty
    '''
    p[0] = None

def p_variales(p):
    '''
    variables : VARIABLES variablesU
              | empty

    variablesU : variablesD
               | empty

    variablesD : ID neu_addVariableAStack COMA variablesD
               | ID DOSPUNTOS tipo_var neu_addVariable PUNTOYCOMA variablesU
    '''
    p[0] = None

def p_funciones(p):
    '''
    funciones : funcionesU
              | empty
    
    funcionesU : tipo_funcion FUNCION ID neu_addFuncion L_PAR recibir_parametros R_PAR variables bloque neu_endFuncion funcionesD
    
    funcionesD : funciones
               | empty
    '''
    p[0] = None

def p_tipo_funcion(p):
    '''
    tipo_funcion : ENTERO empty
                 | FLOTANTE empty
                 | CARACTER empty
                 | VOID empty
    '''
    p[0] = p[1]

def p_tipo_var(p):
    '''
    tipo_var : ENTERO empty
             | FLOTANTE empty
             | CARACTER empty
    '''
    p[0] = p[1]

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

    bloqueU : estatuto bloqueD neu_vaciarPilas empty
            | empty

    bloqueD : bloqueU empty
            | empty
    '''
    p[0] = None

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
    asignacion : ID neu_addID IGUAL neu_addOperador hiper_exp neu_asignacion empty
    '''
    p[0] = None

def p_llamada(p):
    '''
    llamada : ID neu_llamada_era L_PAR mandar_parametros R_PAR neu_llamada_gosub empty
    '''
    p[0] = None

def p_retorno(p):
    '''
    retorno : REGRESA L_PAR ID R_PAR empty
    '''

def p_lectura(p):
    '''
    lectura : LEER L_PAR ID neu_lectura R_PAR empty
    '''
    p[0] = None

def p_escritura(p):
    '''
    escritura : ESCRIBIR L_PAR escrituraD R_PAR empty

    escrituraD : hiper_exp empty
               | LETRERO empty
    '''
    p[0] = None

def p_decision(p):
    '''
    decision : SI L_PAR hiper_exp R_PAR ENTONCES bloque decisionU empty

    decisionU : SINO bloque empty
              | empty
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
    operadorA : MAS neu_addOperador empty
              | MENOS neu_addOperador empty
    '''
    p[0] = None

def p_operadorT(p): 
    '''
    operadorT : MULT neu_addOperador empty
              | DIV neu_addOperador empty
    '''
    p[0] = None

def p_operadorL(p): 
    '''
    operadorL : OR neu_addOperador empty
              | AND neu_addOperador empty
    '''
    p[0] = None

def p_operadorR(p): 
    '''
    operadorR : MENORQUE neu_addOperador empty
              | MAYORQUE neu_addOperador empty
              | MENORIGUALQUE neu_addOperador empty
              | MAYORIGUALQUE neu_addOperador empty
              | IGUALQUE neu_addOperador empty
              | DIFQUE neu_addOperador empty
    '''
    p[0] = None

# EXPRESIONES

def p_hiper_exp(p):
    '''
    hiper_exp : super_exp neu_hacerHiperExp hiper_expU

    hiper_expU : operadorL hiper_exp empty 
               | empty
    '''

def p_super_exp(p):
    '''
    super_exp : exp neu_hacerSuperExp super_expU

    super_expU : operadorR super_exp empty 
               | empty
    '''

def p_exp(p):
    '''
    exp : termino neu_hacerExp expU

    expU : operadorA exp
         | empty
    '''

def p_termino(p):
    '''
    termino : factor neu_hacerTermino terminoU

    terminoU : operadorT termino 
             | empty
    '''

def p_factor(p):
    '''
    factor : varcte empty
           | llamada empty
           | L_PAR hiper_exp R_PAR empty
    '''

def p_varcte(p):
    '''
    varcte  : ID neu_addID empty
            | ENTEROVAL neu_addConstanteEntero empty
            | FLOTANTEVAL neu_addConstanteFlotante empty
            | CARACTERVAL neu_addConstanteCaracter empty
    '''
    p[0] = None

# ERROR / EMPTY

def p_error(p):
    print("Syntax error found at line %d." % (lexer.lineno))

def p_empty(p):
    '''
    empty : 
    '''

############### PUNTOS NEURALGICOS ###############

# PUNTOS PARA INDICAR CUANDO EMPIEZA EL PROGRAMA, LAS FUNCIONES Y PRINCIPAL

# Punto Neuralgico - Inicia el programa
def p_neu_programa(p):
    'neu_programa : '
    global progName, currFuncName
    progName = p[-1]
    currFuncName = p[-1]

    tabla_variables[progName] = {'tipo': progName, 'variables': {}}
    cuadruplos.append(Cuadruplo('GOTO', None, None, progName))

# Punto Neuralgico - Al iniciar una función
def p_neu_addFuncion(p):
    'neu_addFuncion : '
    global currFuncName, currFuncType, progName, memoriaLEntero, memoriaLFlotante, memoriaLCaracter
    
    # Asignar el nombre de la función y su tipo a las variables globales
    currFuncName = p[-1]
    currFuncType = p[-3]

    # Se crea la función en la tabla de variables si no hay otra con el mismo nombre
    if currFuncName not in tabla_variables.keys():
        tabla_variables[currFuncName] = {'tipo': currFuncType, 'variables': {}}

        # Resetear la memoria local para funciones
        memoriaLEntero = 4000
        memoriaLFlotante = 5000
        memoriaLCaracter = 6000
    else:
        errores.append(str(lexer.lineno) + " - La función " + currFuncName + " ya se declaró con anterioridad")

# Punto Neuralgico - Al terminar una función
def p_neu_endFuncion(p):
    'neu_endFuncion : '
    cuadruplos.append(Cuadruplo('ENDFUNC', None, None, None))

# Punto Neuralgico - Al inicial principal()
def p_neu_principal(p):
    'neu_principal : '
    global progName, currFuncName
    currFuncName = progName

# AÑADIR VARIABLES

# Punto Neuralgico - Añade variables a la tabla de variables
def p_neu_addVariable(p):
    'neu_addVariable : '
    global currFuncName, currVarName, currVarType, progName
    currVarType = p[-1]
    currVarName = p[-3]

    # Meter las variables acumuladas, es decir "a" y "b" en "a, b, c : Entero" 
    while varsStack:
        if varsStack[0] not in tabla_variables[currFuncName]['variables'].keys() and varsStack[0] not in tabla_variables[progName]['variables'].keys():
            memoria = p_getMemoriaForID(currVarType)
            tabla_variables[currFuncName]['variables'][varsStack[0]] = {'tipo': currVarType, 'memoria': memoria}
            varsStack.popleft()
        else:
            errores.append(str(lexer.lineno) + " - La variable " + varsStack[0] + " ya se declaró anteriormente")

    # Meter la variable más cercana al tipo, es decir "c" en "a, b, c : Entero"
    if currVarName not in tabla_variables[currFuncName]['variables'].keys() and currVarName not in tabla_variables[progName]['variables'].keys():
        memoria = p_getMemoriaForID(currVarType)
        tabla_variables[currFuncName]['variables'][currVarName] = {'tipo': currVarType, 'memoria': memoria}
    else:
        errores.append(str(lexer.lineno) + " - La variable " + currVarName + " ya se declaró anteriormente")  

def p_neu_addVariableAStack(p):
    'neu_addVariableAStack : '
    global varsStack
    currVarName = p[-1]
    varsStack.append(currVarName)

# Añado un ID a mi pila de terminos y su tipo a la pila de tipos (SE USA PARA EXPRESIONES)
def p_neu_addID(p):
    'neu_addID : '
    global currFuncName
    if p[-1] in tabla_variables[currFuncName]['variables'].keys():
        pilaTerminos.append(tabla_variables[currFuncName]['variables'][p[-1]]['memoria'])
        pilaTipos.append(tabla_variables[currFuncName]['variables'][p[-1]]['tipo'])
    elif p[-1] in tabla_variables[progName]['variables'].keys():
        pilaTerminos.append(tabla_variables[progName]['variables'][p[-1]]['memoria'])
        pilaTipos.append(tabla_variables[progName]['variables'][p[-1]]['tipo'])
    else:
        errores.append(str(lexer.lineno) + " - No se declaró la variable " + p[-1])

# Añado una constante ENTERO a la tabla de constantes
def p_neu_addConstanteEntero(p):
    'neu_addConstanteEntero : '
    if p[-1] not in tabla_constantes['Entero'].keys():
        memoria = p_getCMemoria('Entero')
        tabla_constantes['Entero'][p[-1]] = {'tipo': 'Entero', 'memoria': memoria}
    pilaTerminos.append(tabla_constantes['Entero'][p[-1]]['memoria'])
    pilaTipos.append('Entero')

# Añado una constante FLOTANTE a la tabla de constantes
def p_neu_addConstanteFlotante(p):
    'neu_addConstanteFlotante : '
    if p[-1] not in tabla_constantes['Flotante'].keys():
        memoria = p_getCMemoria('Flotante')
        tabla_constantes['Flotante'][p[-1]] = {'tipo': 'Flotante', 'memoria': memoria}
    pilaTerminos.append(tabla_constantes['Flotante'][p[-1]]['memoria'])
    pilaTipos.append('Flotante')

# Añado una constante CARACTER a la tabla de constantes
def p_neu_addConstanteCaracter(p):
    'neu_addConstanteCaracter : '
    if p[-1] not in tabla_constantes['Caracter'].keys():
        memoria = p_getCMemoria('Caracter')
        tabla_constantes['Caracter'][p[-1]] = {'tipo': 'Caracter', 'memoria': memoria}
    pilaTerminos.append(tabla_constantes['Caracter'][p[-1]]['memoria'])
    pilaTipos.append('Caracter')


def p_neu_addTermino(p):
    'neu_addTermino : '
    pilaTerminos.append(tabla_variables[currFuncName]['variables'][p[-1]]['memoria'])

# INSTRUCCIONES

# Punto Neuralgico - Llamada ERA
def p_neu_llamada_era(p):
    'neu_llamada_era : '
    if p[-1] in tabla_variables.keys():
        cuadruplos.append(Cuadruplo('ERA', None, None, p[-1]))
    else:
        errores.append(str(lexer.lineno) + " - No se declaró la función " + p[-1])
        
# Punto Neuralgico - Llamada GOSUB
def p_neu_llamada_gosub(p):
    'neu_llamada_gosub : '
    cuadruplos.append(Cuadruplo('GOSUB', None, None, p[-5]))

# Punto Neuralgico - ...
def p_neu_addOperador(p):
    'neu_addOperador : '
    pilaOperadores.append(p[-1])

# OBTENER MEMORIA

def p_getMemoriaForID(tipo):
    if currFuncName == progName:
        return p_getGMemoria(tipo)
    else:
        return p_getLMemoria(tipo)

# Global
def p_getGMemoria(tipo):
    'getGMemoria : '
    global memoriaGEntero, memoriaGFlotante, memoriaGCaracter
    if tipo == 'Entero':
        if memoriaGEntero < 2000:
            memoriaGEntero = memoriaGEntero + 1
            return memoriaGEntero
        else:
            errores.append(str(lexer.lineno) + " - Stack Overflow en declaración de variables enteras")
    elif tipo == 'Flotante':
        if memoriaGFlotante < 3000:
            memoriaGFlotante = memoriaGFlotante + 1
            return memoriaGFlotante
        else:
            errores.append(str(lexer.lineno) + " - Stack Overflow en declaración de variables flotantes")
    elif tipo == 'Caracter':
        if memoriaGCaracter < 4000:
            memoriaGCaracter = memoriaGCaracter + 1
            return memoriaGCaracter
        else:
            errores.append(str(lexer.lineno) + " - Stack Overflow en declaración de caracteres")

# Local
def p_getLMemoria(tipo):
    'getLMemoria : '
    global memoriaLEntero, memoriaLFlotante, memoriaLCaracter
    if tipo == 'Entero':
        if memoriaLEntero < 5000:
            memoriaLEntero = memoriaLEntero + 1
            return memoriaLEntero
        else:
            errores.append(str(lexer.lineno) + " - Stack Overflow en declaración de variables enteras")
    elif tipo == 'Flotante':
        if memoriaLFlotante < 6000:
            memoriaLFlotante = memoriaLFlotante + 1
            return memoriaLFlotante
        else:
            errores.append(str(lexer.lineno) + " - Stack Overflow en declaración de variables flotantes")
    elif tipo == 'Caracter':
        if memoriaLCaracter < 7000:
            memoriaLCaracter = memoriaLCaracter + 1
            return memoriaLCaracter
        else:
            errores.append(str(lexer.lineno) + " - Stack Overflow en declaración de caracteres")

# Constante
def p_getCMemoria(tipo):
    'getCMemoria : '
    global memoriaCEntero, memoriaCFlotante, memoriaCCaracter
    if tipo == 'Entero':
        if memoriaCEntero < 8000:
            memoriaCEntero = memoriaCEntero + 1
            return memoriaCEntero
        else:
            errores.append(str(lexer.lineno) + " - Stack Overflow en declaración de variables enteras")
    elif tipo == 'Flotante':
        if memoriaCFlotante < 9000:
            memoriaCFlotante = memoriaCFlotante + 1
            return memoriaCFlotante
        else:
            errores.append(str(lexer.lineno) + " - Stack Overflow en declaración de variables flotantes")
    elif tipo == 'Caracter':
        if memoriaCCaracter < 10000:
            memoriaCCaracter = memoriaCCaracter + 1
            return memoriaCCaracter
        else:
            errores.append(str(lexer.lineno) + " - Stack Overflow en declaración de caracteres")

# REALIZAR OPERACIONES

# * /
def p_neu_hacerTermino(p):
    'neu_hacerTermino : '
    global pilaOperadores, pilaTerminos, currFuncName
    if(pilaOperadores[-1] == '*' or pilaOperadores[-1] == '/'):
        ladoDer = pilaTerminos.pop()
        ladoIzq = pilaTerminos.pop()
        ladoDerTipo = pilaTipos.pop()
        ladoIzqTipo = pilaTipos.pop()
        operador = pilaOperadores.pop()

        tipoResultado = CuboSemantico.getTipoCubo(ladoIzqTipo, ladoDerTipo, operador)
        if currFuncName == progName:
            memoriaResultado = p_getGMemoria(tipoResultado) 
        else:
            memoriaResultado = p_getLMemoria(tipoResultado)

        if tipoResultado != 'Error':
            cuadruplos.append(Cuadruplo(operador, ladoIzq, ladoDer, memoriaResultado))
            pilaTerminos.append(memoriaResultado)
            pilaTipos.append(tipoResultado)
        else:
            errores.append(str(lexer.lineno) + " - Error en operaciones de tipos")

# + -
def p_neu_hacerExp(p):
    'neu_hacerExp : '
    global pilaOperadores, pilaTerminos, currFuncName
    if(pilaOperadores[-1] == '+' or pilaOperadores[-1] == '-'):
        ladoDer = pilaTerminos.pop()
        ladoIzq = pilaTerminos.pop()
        ladoDerTipo = pilaTipos.pop()
        ladoIzqTipo = pilaTipos.pop()
        operador = pilaOperadores.pop()

        tipoResultado = CuboSemantico.getTipoCubo(ladoIzqTipo, ladoDerTipo, operador)
        if currFuncName == progName:
            memoriaResultado = p_getGMemoria(tipoResultado) 
        else:
            memoriaResultado = p_getLMemoria(tipoResultado)
        
        if tipoResultado != 'Error':
            cuadruplos.append(Cuadruplo(operador, ladoIzq, ladoDer, memoriaResultado))
            pilaTerminos.append(memoriaResultado)
            pilaTipos.append(tipoResultado)
        else:
            errores.append(str(lexer.lineno) + " - Error en operaciones de tipos")

# < > >= >= != ==
def p_neu_hacerSuperExp(p):
    'neu_hacerSuperExp : '
    global pilaOperadores, pilaTerminos, currFuncName
    if(pilaOperadores[-1] == '<' or pilaOperadores[-1] == '>' or pilaOperadores[-1] == '<=' or pilaOperadores[-1] == '>=' or pilaOperadores[-1] == '!=' or pilaOperadores[-1] == '=='):
        ladoDer = pilaTerminos.pop()
        ladoIzq = pilaTerminos.pop()
        ladoDerTipo = pilaTipos.pop()
        ladoIzqTipo = pilaTipos.pop()
        operador = pilaOperadores.pop()

        tipoResultado = CuboSemantico.getTipoCubo(ladoIzqTipo, ladoDerTipo, operador)
        if currFuncName == progName:
            memoriaResultado = p_getGMemoria(tipoResultado) 
        else:
            memoriaResultado = p_getLMemoria(tipoResultado)
        
        if tipoResultado != 'Error':
            cuadruplos.append(Cuadruplo(operador, ladoIzq, ladoDer, memoriaResultado))
            pilaTerminos.append(memoriaResultado)
            pilaTipos.append(tipoResultado)
        else:
            errores.append(str(lexer.lineno) + " - Error en operaciones de tipos")

# & |
def p_neu_hacerHiperExp(p):
    'neu_hacerHiperExp : '
    global pilaOperadores, pilaTerminos, currFuncName
    if(pilaOperadores[-1] == '&' or pilaOperadores[-1] == '|'):
        ladoDer = pilaTerminos.pop()
        ladoIzq = pilaTerminos.pop()
        ladoDerTipo = pilaTipos.pop()
        ladoIzqTipo = pilaTipos.pop()
        operador = pilaOperadores.pop()

        tipoResultado = CuboSemantico.getTipoCubo(ladoIzqTipo, ladoDerTipo, operador)
        if currFuncName == progName:
            memoriaResultado = p_getGMemoria(tipoResultado) 
        else:
            memoriaResultado = p_getLMemoria(tipoResultado)
        
        if tipoResultado != 'Error':
            cuadruplos.append(Cuadruplo(operador, ladoIzq, ladoDer, memoriaResultado))
            pilaTerminos.append(memoriaResultado)
            pilaTipos.append(tipoResultado)
        else:
            errores.append(str(lexer.lineno) + " - Error en operaciones de tipos")

def p_neu_asignacion(p):
    'neu_asignacion : '
    igual = pilaOperadores.pop()
    der = pilaTerminos.pop()
    izq = pilaTerminos.pop()
    cuadruplos.append(Cuadruplo(igual, izq, None, der))

def p_neu_lectura(p):
    'neu_lectura : '
    global currFuncName
    if p[-1] in tabla_variables[currFuncName]['variables'].keys():
        cuadruplos.append(Cuadruplo('READ', None, None, tabla_variables[currFuncName]['variables'][p[-1]]['memoria']))
    else:
        errores.append(str(lexer.lineno) + " - Se debe declarar la variable " + p[-1] + " antes de utilizarla")

# def p_neu_escritura(p):
#     'neu_escritura : '
#     global currFuncName
#     print("---------------------" + str(p[-1]))
#     if p[-1] in tabla_variables[currFuncName]['variables'].keys():
#         cuadruplos.append(Cuadruplo('WRITE', None, None, tabla_variables[currFuncName]['variables'][p[-1]]['memoria']))
#     else:
#         errores.append(str(lexer.lineno) + " - Se debe declarar la variable " + p[-1] + " antes de utilizarla")

def p_neu_vaciarPilas(p):
    'neu_vaciarPilas : '
    global pilaTerminos, pilaOperadores, pilaTipos
    pilaTerminos.clear()
    pilaOperadores.clear()
    pilaTipos.clear()

parser = yacc.yacc()

############### EJECUCIÓN ###############

try:
    text = input('Nombre de archivo txt: ')
    with open(text, 'r') as file:
        parser.parse(file.read())

        if errores:
            print("\n! " + str(len(errores)) + " ERROR(ES) ->")
            for item in errores:
                print("! Linea " + item)
        else:
            print("\nTABLA DE VARIABLES ->")
            print(tabla_variables)

            print("\nTABLA DE CONSTANTES ->")
            print(tabla_constantes)

            print("\nCUADRUPLOS ->")
            for item in cuadruplos:
                print(item.getCuadruplo())

except EOFError:
    print("Error")
