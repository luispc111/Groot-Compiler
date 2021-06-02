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

currCuadruplo = 0 # cuadruplo actual que se está analizando
corriendo = 1 # Bandera para indicar si hay más cuadruplos por revisar
operador = 'OP' # Se almacenaráel primer elemento de todos los cuadruplos
currFunc = '...' # Se almacenará el nombre de la función en ejecución
pilaLlamadas = [] # Se almacena una pila de llamadas a funciones para saber a donde dirigirse cuando se termine la ejecución
currParametros = [] # Pila que ayuda a realizar validaciones al momento de enviar parametros a una función
variablesLocales = [] # Pila que contendrá diccionarios de memorias locales, el diccionario en el top representa la memoria local actual
dic_tabla_locales = {}

# Obtener cuadruplos, tabla de variables y tabla de constantes
data = lexer_parser.correrMV()

cuadruplos = data['cuadruplos']
tabla_variables = data['tabla_variables']
tabla_constantes = data['tabla_constantes']
progName = data['progName']
parametrosFuncion = data['parametrosFuncion']

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
# Contendrá todos las variables globales y constantes
st = {**super_tabla_variables , **super_tabla_constantes}
# print(st)

# HELPERS
def notifError(errorText):
    print("\n! ERROR - " + errorText + "\n")
    sys.exit()

# Esta función transforma una memoria a un resultado casteado
# Recibe    -> dirección de memoria
# Retorna   -> valor almacenado enn la memoria, casteado a su tipo
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

# Esta función genera un diccionario que se terminará poniendo en la pila de variables locales
# Recibe    -> nombre de la función
# Genera    -> diccionario de variables locales
def startMemoriaLocal(funcName):
    global dic_tabla_locales
    dic_tabla_locales.clear()
    # Asignar memoria a variables locales
    for localvar in tabla_variables[funcName]['variables']:
        dic_tabla_locales[tabla_variables[funcName]['variables'][localvar]['memoria']] = None

# Esta función borra la memoria local.
# Se llamará a esta función cuando se termine la ejecución de una función
def deleteMemoriaLocal():
    global variablesLocales
    variablesLocales.pop()

# Recibo    -> dirección de memoria
# Retorna   -> booleando que indique si la memoria es local o global 
def esLocal(memoria):
    if re.match("\(\d+\)", str(memoria)):
        memoria = getType(int(memoria[1:-1]))

    if 4001 <= memoria <= 7000:
        return True
    else:
        return False

# Esta función me permite utilizar lógica entera al realizar comparaciones
# Recibo    -> un valor booleano y un espacio de memoria
# Genera    -> Asigna en memoria un 0 o 1 dependiendo del valor del booleano
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

# Esta funcion verifica que el input de un usuario coincida en regex con un tipo
# Y que ese tipo coincida con la variable a la que se le quiere asignar el valor
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

######## ANÁLISIS DE CUADRUPLOS ########

while corriendo:
    cuadruplo = Cuadruplo.getCuadruplo(cuadruplos[currCuadruplo])
    operador = cuadruplo[0]

    # GOTO / GOTOF
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
    # Para los comparadores, la función comparadorHelper ya cubre errores y añade 1 a currCuadruplo 
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
            variablesLocales[-1][cuadruplo[3]] = lecturaCaster(var, cuadruplo[3])
        else:
            st[cuadruplo[3]] = lecturaCaster(var, cuadruplo[3])
        currCuadruplo += 1
    
    # FUNCIONES
    elif operador == 'ERA':
        # Genera la memoria local
        startMemoriaLocal(cuadruplo[1])
        currFunc = cuadruplo[1]
        currParametros = list(tabla_variables[currFunc]['variables'])
        currCuadruplo += 1
    
    elif operador == 'PARAM':
        # Tomo el número del ultimo elemento del cuadruplo
        index = int((cuadruplo[3])[5]) - 1
        
        # Asigno los parametros como variables locales de la función que estoy llamando
        dic_tabla_locales[tabla_variables[currFunc]['variables'][currParametros[index]]['memoria']] = getType(cuadruplo[1])
        currCuadruplo += 1

    elif operador == 'GOSUB':
        # añado el cuadruplo actual a la pila de llamadas para poder regresar a continuar la ejecución
        pilaLlamadas.append(currCuadruplo)

        # Se añade a mi pila de variables locales, la memoria local
        variablesLocales.append(dic_tabla_locales)
        dic_tabla_locales = {}

        currCuadruplo = tabla_variables[cuadruplo[1]]['numCuadruplo']

    elif operador == 'RETURN':

        # Asignar el resultado del return a la variable global asignada para esta función
        memoria = tabla_variables[progName]['variables'][currFunc]['memoria']
        st[memoria] = getType(cuadruplo[3])

        # se borra la memoria local porque la función llegó al fin de su ejecución
        deleteMemoriaLocal()
        currCuadruplo = int(pilaLlamadas.pop()) + 1
    
    elif operador == 'ENDFUNC':
        # se borra la memoria local porque la función llegó al fin de su ejecución
        deleteMemoriaLocal()
        currCuadruplo = int(pilaLlamadas.pop()) + 1
    
    # ARREGLOS / MATRICES
    elif operador == 'VER':
        if int(cuadruplo[2]) <= int(getType(cuadruplo[1])) < int(cuadruplo[3]):
            pass
        else:
            notifError("El índice para un arreglo/matriz no es válido")
        currCuadruplo += 1  
    
    elif operador == 'SUMABASE':
        # Este nuevo operador indíca cuando debo sumarle la dirección base a algpun índice de un arreglo o matriz 
        if esLocal(int(cuadruplo[1]) + getType(cuadruplo[2])):
            variablesLocales[-1][cuadruplo[3]] = int(cuadruplo[1]) + getType(cuadruplo[2])
        else:
            st[cuadruplo[3]] = int(cuadruplo[1]) + getType(cuadruplo[2])
        currCuadruplo += 1
    
    # END
    elif operador == 'END':
        # Cancela la lectura de cuadruplos
        corriendo = 0
    else:
        # No se debería llegar a este else, pero lo dejo por si se llega a necesitar
        print("Error en los cuadruplos")
        corriendo = 0
