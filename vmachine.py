# MAQUINA VIRTUAL

#IMPORTS
import sys

import lexer_parser
from Cuadruplo import *
# from CuboSemantico import *

# VARIABLES GLOBALES
currCuadruplo = 0
corriendo = 1
operador = 'OP'

# Obtener cuadruplos, tabla de variables y tabla de constantes
data = lexer_parser.correrMV()

cuadruplos = data['cuadruplos']
tabla_variables = data['tabla_variables']
tabla_constantes = data['tabla_constantes']
progName = data['progName']

super_tabla_variables = {}
super_tabla_constantes = {}

for var in tabla_variables[progName]['variables']:
    super_tabla_variables[tabla_variables[progName]['variables'][var]['memoria']] = None
    
super_tabla_constantes = {}
for tipo in tabla_constantes:
    for var in tabla_constantes[tipo]:
        super_tabla_constantes[tabla_constantes[tipo][var]['memoria']] = var

# SUPER TABLA
st = {**super_tabla_variables , **super_tabla_constantes}
print(st)

# HELPERS
def notifError(errorText):
    print("\n! ERROR - " + errorText + "\n")
    sys.exit()

def getType(memoria):
    # ENTERO
    if 1001 <= memoria <= 2000 or 7001 <= memoria <= 8000:
        return int(st[memoria])
    elif 2001 <= memoria <= 3000 or 8001 <= memoria <= 9000:
        return float(st[memoria])

while corriendo:
    cuadruplo = Cuadruplo.getCuadruplo(cuadruplos[currCuadruplo])
    operador = cuadruplo[0]

    if operador == 'GOTO':
        currCuadruplo = cuadruplo[3]
    elif operador == 'GOTOF':
        if st[cuadruplo[1]] == None:
            notifError("Una evaluación no tiene valor")

        if getType(cuadruplo[1]) == 0 or getType(cuadruplo[1]) == 0.0:
            currCuadruplo = cuadruplo[3]
        else:
            currCuadruplo += 1
    elif operador == '=':
        if st[cuadruplo[1]] == None:
            notifError("Una variable en la asignación no tiene un valor asignado")

        st[cuadruplo[3]] = st[cuadruplo[1]]
        currCuadruplo += 1
    elif operador == '+':
        if st[cuadruplo[1]] == None or st[cuadruplo[2]] == None:
            notifError("Una variable en la suma no tiene valor asignado")

        st[cuadruplo[3]] = getType(cuadruplo[1]) + getType(cuadruplo[2])
        currCuadruplo += 1
    elif operador == '-':
        if st[cuadruplo[1]] == None or st[cuadruplo[2]] == None:
            notifError("Una variable en la resta no tiene valor asignado")

        st[cuadruplo[3]] = getType(cuadruplo[1]) - getType(cuadruplo[2])
        currCuadruplo += 1
    elif operador == '*':
        if st[cuadruplo[1]] == None or st[cuadruplo[2]] == None:
            notifError("Una variable en la multiplicación no tiene valor asignado")

        st[cuadruplo[3]] = getType(cuadruplo[1]) / getType(cuadruplo[2])
        currCuadruplo += 1
    ############ DIVISIÓN ############
    elif operador == '<':
        if st[cuadruplo[1]] == None or st[cuadruplo[2]] == None:
            notifError("Una variable en la comparación no tiene valor asignado")

        if getType(cuadruplo[1]) < getType(cuadruplo[2]):
            st[cuadruplo[3]] = 1
        else:
            st[cuadruplo[3]] = 0
        currCuadruplo += 1
    elif operador == '>':
        if st[cuadruplo[1]] == None or st[cuadruplo[2]] == None:
            notifError("Una variable en la comparación no tiene valor asignado")

        if getType(cuadruplo[1]) > getType(cuadruplo[2]):
            st[cuadruplo[3]] = 1
        else:
            st[cuadruplo[3]] = 0
        currCuadruplo += 1
    elif operador == '<=':
        if st[cuadruplo[1]] == None or st[cuadruplo[2]] == None:
            notifError("Una variable en la comparación no tiene valor asignado")

        if getType(cuadruplo[1]) <= getType(cuadruplo[2]):
            st[cuadruplo[3]] = 1
        else:
            st[cuadruplo[3]] = 0
        currCuadruplo += 1
    elif operador == '>=':
        if st[cuadruplo[1]] == None or st[cuadruplo[2]] == None:
            notifError("Una variable en la comparación no tiene valor asignado")

        if getType(cuadruplo[1]) >= getType(cuadruplo[2]):
            st[cuadruplo[3]] = 1
        else:
            st[cuadruplo[3]] = 0
        currCuadruplo += 1
    elif operador == '==':
        if st[cuadruplo[1]] == None or st[cuadruplo[2]] == None:
            notifError("Una variable en la comparación no tiene valor asignado")

        if getType(cuadruplo[1]) == getType(cuadruplo[2]):
            st[cuadruplo[3]] = 1
        else:
            st[cuadruplo[3]] = 0
        currCuadruplo += 1
    elif operador == '!=':
        if st[cuadruplo[1]] == None or st[cuadruplo[2]] == None:
            notifError("Una variable en la comparación no tiene valor asignado")

        if getType(cuadruplo[1]) != getType(cuadruplo[2]):
            st[cuadruplo[3]] = 1
        else:
            st[cuadruplo[3]] = 0
        currCuadruplo += 1
    elif operador == '&':
        if st[cuadruplo[1]] == None or st[cuadruplo[2]] == None:
            notifError("Una variable en la comparación no tiene valor asignado")

        if getType(cuadruplo[1]) != 0 and getType(cuadruplo[2]) != 0:
            st[cuadruplo[3]] = 1
        else:
            st[cuadruplo[3]] = 0
        currCuadruplo += 1
    elif operador == '|':
        if st[cuadruplo[1]] == None or st[cuadruplo[2]] == None:
            notifError("Una variable en la comparación no tiene valor asignado")

        if getType(cuadruplo[1]) == 0 and getType(cuadruplo[2]) == 0:
            st[cuadruplo[3]] = 0
        else:
            st[cuadruplo[3]] = 1
        currCuadruplo += 1
    elif operador == 'WRITE':
        print(st[cuadruplo[3]])
        currCuadruplo += 1
    elif operador == 'END':
        corriendo = 0
    else:
        print("********* ERROR")
        corriendo = 0