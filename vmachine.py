# Luis Alberto Pérez Chapa
# A01282564

# GROOT LANGUAGE
# MAQUINA VIRTUAL

#IMPORTS
import sys
import re

import lexer_parser
from Cuadruplo import *

# VARIABLES GLOBALES
currCuadruplo = 0
corriendo = 1
operador = 'OP'
currFunc = '...'
pilaLlamadas = []
currParametros = []

# Obtener cuadruplos, tabla de variables y tabla de constantes
data = lexer_parser.correrMV()

cuadruplos = data['cuadruplos']
tabla_variables = data['tabla_variables']
tabla_constantes = data['tabla_constantes']
progName = data['progName']
parametrosFuncion = data['parametrosFuncion']

variablesLocales = []
dic_tabla_locales = {}

super_tabla_variables = {}
super_tabla_constantes = {}

maxEntero = 1000
minEntero = 2001
for var in tabla_variables[progName]['variables']:
    if tabla_variables[progName]['variables'][var]['tipo'] == 'Entero':
        if tabla_variables[progName]['variables'][var]['memoria'] > maxEntero:
            maxEntero = tabla_variables[progName]['variables'][var]['memoria']
        
        if tabla_variables[progName]['variables'][var]['memoria'] < minEntero:
            minEntero = tabla_variables[progName]['variables'][var]['memoria']

while minEntero <= maxEntero:
    super_tabla_variables[minEntero] = None
    minEntero += 1

maxFlotante = 2000
minFlotante = 3001
for var in tabla_variables[progName]['variables']:
    if tabla_variables[progName]['variables'][var]['tipo'] == 'Flotante':
        if tabla_variables[progName]['variables'][var]['memoria'] > maxFlotante:
            maxFlotante = tabla_variables[progName]['variables'][var]['memoria']
        
        if tabla_variables[progName]['variables'][var]['memoria'] < minFlotante:
            minFlotante = tabla_variables[progName]['variables'][var]['memoria']

while minFlotante <= maxFlotante:
    super_tabla_variables[minFlotante] = None
    minFlotante += 1

maxCaracter = 3000
minCaracter = 4001
for var in tabla_variables[progName]['variables']:
    if tabla_variables[progName]['variables'][var]['tipo'] == 'Caracter':
        if tabla_variables[progName]['variables'][var]['memoria'] > maxCaracter:
            maxCaracter = tabla_variables[progName]['variables'][var]['memoria']
        
        if tabla_variables[progName]['variables'][var]['memoria'] < minCaracter:
            minCaracter = tabla_variables[progName]['variables'][var]['memoria']

while minCaracter <= maxCaracter:
    super_tabla_variables[minCaracter] = None
    minCaracter += 1

super_tabla_constantes = {}
for tipo in tabla_constantes:
    for var in tabla_constantes[tipo]:
        super_tabla_constantes[tabla_constantes[tipo][var]['memoria']] = var

# SUPER TABLA
st = {**super_tabla_variables , **super_tabla_constantes}
# print(st)

# HELPERS
def notifError(errorText):
    print("\n! ERROR - " + errorText + "\n")
    sys.exit()

def getType(memoria):

    if re.match("\(\d+\)", str(memoria)):
        memoria = getType(int(memoria[1:-1]))

    memoria = int(memoria)

    # ENTERO
    if 1001 <= memoria <= 2000 or 4001 <= memoria <= 5000 or 7001 <= memoria <= 8000:
        if 4001 <= memoria <= 5000:
            return int(variablesLocales[-1][memoria])
        else:
            return int(st[memoria])
    # FLOTANTE
    elif 2001 <= memoria <= 3000 or 5001 <= memoria <= 6000 or 8001 <= memoria <= 9000:
        if 5001 <= memoria <= 6000:
            return float(variablesLocales[-1][memoria])
        else:
            return float(st[memoria])
    # CARACTERES
    elif 3001 <= memoria <= 4000 or 6001 <= memoria <= 7000 or 9001 <= memoria <= 10000:
        if 6001 <= memoria <= 7000:
            return variablesLocales[-1][memoria]
        else:
            return st[memoria]
    # LETREROS
    elif 10001 <= memoria <= 11000:
        text = st[memoria]
        tam = len(text)
        return text[1:tam-1]
    else:
        notifError("ERROR EN OPERACIÓN")

def startMemoriaLocal(funcName):
    global dic_tabla_locales
    dic_tabla_locales.clear()
    # Asignar memoria a variables locales
    for localvar in tabla_variables[funcName]['variables']:
        dic_tabla_locales[tabla_variables[funcName]['variables'][localvar]['memoria']] = None

def deleteMemoriaLocal():
    global variablesLocales
    # Borrar memoria local
    variablesLocales.pop()

def checarExistenciaST(memoria):
    if memoria in st.keys():
        if st[memoria] != None:
            return st[memoria]
    return None

def checarExistenciaLocal(memoria):
    if memoria in (variablesLocales[-1]).keys():
        if (variablesLocales[-1])[memoria] != None:
            return (variablesLocales[-1])[memoria]
    return None

def esLocal(memoria):
    if re.match("\(\d+\)", str(memoria)):
        memoria = getType(int(memoria[1:-1]))

    if 4001 <= memoria <= 7000:
        return True
    else:
        return False

def comparadorHelper(booleano, memoria):
    global currCuadruplo
    if esLocal(memoria):
        if booleano == False:
            variablesLocales[-1][memoria] = 0
        else:
            variablesLocales[-1][memoria] = 1
    else:
        if booleano == False:
            st[memoria] = 0
        else:
            st[memoria] = 1
    currCuadruplo += 1

def lecturaCaster(value, memoria):
    if re.match("[-]?[0-9]+([.][0-9]+)", value):
        if 2001 <= memoria <= 3000 or 5001 <= memoria <= 6000 or 8001 <= memoria <= 9000:
            return float(value)
        else:
            notifError("El valor proporcionado no coincide con el tipo de la variable")
    elif re.match("[-]?[0-9]+", value):
        if 1001 <= memoria <= 2000 or 4001 <= memoria <= 5000 or 7001 <= memoria <= 8000:
            return int(value)
        else:
            notifError("El valor proporcionado no coincide con el tipo de la variable")
    elif re.match("([^\'])", value):
        if 3001 <= memoria <= 4000 or 6001 <= memoria <= 7000 or 9001 <= memoria <= 10000:
            return value
        else:
            notifError("El valor proporcionado no coincide con el tipo de la variable")
    else:
        notifError("El valor que se leyó no se puede asignar a la variable")

while corriendo:
    cuadruplo = Cuadruplo.getCuadruplo(cuadruplos[currCuadruplo])
    operador = cuadruplo[0]

    # GOTOs
    if operador == 'GOTO':
        currCuadruplo = cuadruplo[3]
    
    elif operador == 'GOTOF':
        if getType(cuadruplo[1]) == 0 or getType(cuadruplo[1]) == 0.0:
            currCuadruplo = cuadruplo[3]
        else:
            currCuadruplo += 1
    
    # ASIGNACIÓN
    elif operador == '=':
        # a = b
        a = cuadruplo[3]
        b = getType(cuadruplo[1])

        if re.match("\(\d+\)", str(a)):
            a = getType(int(a[1:-1]))

        if esLocal(a):
            variablesLocales[-1][a] = b
        else:
            st[a] = b
        currCuadruplo += 1

    # OPERACIONES
    elif operador == '+':
        if esLocal(cuadruplo[3]):
            (variablesLocales[-1])[cuadruplo[3]] = getType(cuadruplo[1]) + getType(cuadruplo[2])
        else:
            st[cuadruplo[3]] = getType(cuadruplo[1]) + getType(cuadruplo[2])
        currCuadruplo += 1
        
    elif operador == '-':
        if esLocal(cuadruplo[3]):
            (variablesLocales[-1])[cuadruplo[3]] = getType(cuadruplo[1]) - getType(cuadruplo[2])
        else:
            st[cuadruplo[3]] = getType(cuadruplo[1]) - getType(cuadruplo[2])
        currCuadruplo += 1

    elif operador == '*':
        if esLocal(cuadruplo[3]):
            (variablesLocales[-1])[cuadruplo[3]] = getType(cuadruplo[1]) * getType(cuadruplo[2])
        else:
            st[cuadruplo[3]] = getType(cuadruplo[1]) * getType(cuadruplo[2])
        currCuadruplo += 1

    elif operador == '/':
        
        # División entre 0
        if getType(cuadruplo[2]) == 0:
            notifError("Se está realizando una división entre 0")

        if esLocal(cuadruplo[3]):
            (variablesLocales[-1])[cuadruplo[3]] = getType(cuadruplo[1]) / getType(cuadruplo[2])
        else:
            st[cuadruplo[3]] = getType(cuadruplo[1]) / getType(cuadruplo[2])
        currCuadruplo += 1

    # COMPARADORES
    elif operador == '<':
        res = getType(cuadruplo[1]) < getType(cuadruplo[2])
        comparadorHelper(res, cuadruplo[3])
    
    elif operador == '>':
        res = getType(cuadruplo[1]) > getType(cuadruplo[2])
        comparadorHelper(res, cuadruplo[3])

    elif operador == '<=':
        res = getType(cuadruplo[1]) <= getType(cuadruplo[2])
        comparadorHelper(res, cuadruplo[3])

    elif operador == '>=':
        res = getType(cuadruplo[1]) >= getType(cuadruplo[2])
        comparadorHelper(res, cuadruplo[3])

    elif operador == '==':
        res = getType(cuadruplo[1]) == getType(cuadruplo[2])
        comparadorHelper(res, cuadruplo[3])

    elif operador == '!=':
        res = getType(cuadruplo[1]) != getType(cuadruplo[2])
        comparadorHelper(res, cuadruplo[3])

    elif operador == '&':
        res1 = 0
        res2 = 0
        if getType(cuadruplo[1]) != 0:
            res1 = 1
        else:
            res1 = 0
        
        if getType(cuadruplo[2]) != 0:
            res2 = 1
        else:
            res2 = 0
        
        if esLocal(memoria):
            if res1 + res2 == 2:
                variablesLocales[-1][memoria] = 1
            else:
                variablesLocales[-1][memoria] = 0
        else:
            if res1 + res2 == 2:
                st[memoria] = 1
            else:
                st[memoria] = 0
        
        currCuadruplo += 1

    elif operador == '|':
        res1 = 0
        res2 = 0
        if getType(cuadruplo[1]) != 0:
            res1 = 1
        else:
            res1 = 0
        
        if getType(cuadruplo[2]) != 0:
            res2 = 1
        else:
            res2 = 0
        
        if esLocal(memoria):
            if res1 + res2 == 0:
                variablesLocales[-1][memoria] = 0
            else:
                variablesLocales[-1][memoria] = 1
        else:
            if res1 + res2 == 0:
                st[memoria] = 0
            else:
                st[memoria] = 1
        
        currCuadruplo += 1

    # ESCRITURA
    elif operador == 'WRITE':
        print(getType(cuadruplo[3]))
        currCuadruplo += 1
    
    # LECTURA
    elif operador == 'READ':
        var = input("> ")
        if esLocal(cuadruplo[3]):
            variablesLocales[-1][cuadruplo[3]] = lecturaCaster(var)
        else:
            st[cuadruplo[3]] = lecturaCaster(var, cuadruplo[3])
        currCuadruplo += 1
    
    # FUNCIONES
    elif operador == 'ERA':
        startMemoriaLocal(cuadruplo[1])
        currFunc = cuadruplo[1]
        currParametros = list(tabla_variables[currFunc]['variables'])
        currCuadruplo += 1
    
    elif operador == 'PARAM':
        index = int((cuadruplo[3])[5]) - 1
        if esLocal(cuadruplo[1]):
            dic_tabla_locales[tabla_variables[currFunc]['variables'][currParametros[index]]['memoria']] = variablesLocales[-1][cuadruplo[1]]
        else:
            dic_tabla_locales[tabla_variables[currFunc]['variables'][currParametros[index]]['memoria']] = st[cuadruplo[1]]
        currCuadruplo += 1

    elif operador == 'GOSUB':
        pilaLlamadas.append(currCuadruplo)
        variablesLocales.append(dic_tabla_locales)
        dic_tabla_locales = {}
        currCuadruplo = tabla_variables[cuadruplo[1]]['numCuadruplo']

    elif operador == 'RETURN':
        memoria = tabla_variables[progName]['variables'][currFunc]['memoria']
        st[memoria] = getType(cuadruplo[3])
        deleteMemoriaLocal()
        currCuadruplo = int(pilaLlamadas.pop()) + 1
    
    elif operador == 'ENDFUNC':
        deleteMemoriaLocal()
        currCuadruplo = int(pilaLlamadas.pop()) + 1
    
    # ARREGLOS
    elif operador == 'VER':
        if int(cuadruplo[2]) <= int(getType(cuadruplo[1])) < int(cuadruplo[3]):
            pass
        else:
            notifError("El index para un arreglo/matriz no es válido")
        currCuadruplo += 1  
    
    elif operador == 'SUMABASE':
        if esLocal(int(cuadruplo[1]) + getType(cuadruplo[2])):
            variablesLocales[-1][cuadruplo[3]] = int(cuadruplo[1]) + getType(cuadruplo[2])
        else:
            st[cuadruplo[3]] = int(cuadruplo[1]) + getType(cuadruplo[2])
        currCuadruplo += 1
    
    # END
    elif operador == 'END':
        corriendo = 0
    
    else:
        print("********* ERROR")
        print(currCuadruplo)
        corriendo = 0
