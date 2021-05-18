#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "semantica.h"

// MANEJO DEL CUBO SEMANTICO

// Los tipos de datos basicos : INT_TYPE, FLOAT_TYPE y CHAR_TYPE

// Checar con el cubo semantico nuestras operaciones
int get_result_type(int type_1, int type_2, int op_type){ 
	switch(op_type){
		case NONE: /* Aqui vemos quienes se llevan con quienes, devolvemos 1 cuando sean compatibles */
		
			if(type_1 == INT_TYPE){
				
				if(type_2 == INT_TYPE || type_2 == CHAR_TYPE){
					return 1;
				}
				else{
					type_error(type_1, type_2, op_type);
				}
			}
			
			else if(type_1 == FLOAT_TYPE){
			
				if(type_2 == INT_TYPE || type_2 == FLOAT_TYPE || type_2 == CHAR_TYPE){
					return 1;
				}
				else{
					type_error(type_1, type_2, op_type);
				}
			}
			
			else if(type_1 == CHAR_TYPE){
				
				if(type_2 == INT_TYPE || type_2 == CHAR_TYPE){
					return 1;
				}
				else{
					type_error(type_1, type_2, op_type);
				}
			}
			break;

		/* ---------------------------------------------------------- */
		case ARITHM_OP: /* OPERADORES ARITMETICOS */
			// INT
			if(type_1 == INT_TYPE){
				// INT or CHAR
				if(type_2 == INT_TYPE || type_2 == CHAR_TYPE){
					return INT_TYPE;
				}
				// FLOAT
				else if(type_2 == FLOAT_TYPE){
					return FLOAT_TYPE;
				}
				else{
					type_error(type_1, type_2, op_type);
				}
			}
			// FLOAT
			else if(type_1 == FLOAT_TYPE){
				// INT, FLOAT o CHAR
				if(type_2 == INT_TYPE || type_2 == FLOAT_TYPE || type_2 == CHAR_TYPE){
					return FLOAT_TYPE;
				}
				else{
					type_error(type_1, type_2, op_type);
				}
			}
			// CHAR
			else if(type_1 == CHAR_TYPE){
				// INT o CHAR
				if(type_2 == INT_TYPE || type_2 == CHAR_TYPE){
					return CHAR_TYPE;
				}
				// FLOAT
				else if(type_2 == FLOAT_TYPE){
					return FLOAT_TYPE;
				}
				else{
					type_error(type_1, type_2, op_type);
				}
			}
			else{
				type_error(type_1, type_2, op_type);
			}
			break;
		/* ---------------------------------------------------------- */
		case INCR_OP: /* CASO ESPECIAL PARA EL INCREMENTO O DECREMENTO POR 1 */
			// INT
			if(type_1 == INT_TYPE){
				return INT_TYPE;
			}
			// FLOAT
			else if(type_1 == FLOAT_TYPE){
				return FLOAT_TYPE;
			}
			// CHAR
			else if(type_1 == CHAR_TYPE){
				return CHAR_TYPE;
			}
			else{
				type_error(type_1, type_2, op_type);
			}
			break;
		/* ---------------------------------------------------------- */
		case BOOL_OP: /* OPERACIONES BOOLEANAS (SE MANEJA LOGICA DE ENTEROS) */
			// INT
			if(type_1 == INT_TYPE){
				// INT o CHAR
				if(type_2 == INT_TYPE || type_2 == CHAR_TYPE){
					return INT_TYPE;
				}
				else{
					type_error(type_1, type_2, op_type);
				}
			}
			// CHAR
			else if(type_1 == CHAR_TYPE){
				// INT o CHAR
				if(type_2 == INT_TYPE || type_2 == CHAR_TYPE){
					return CHAR_TYPE;
				}
				else{
					type_error(type_1, type_2, op_type);
				}
			}
			else{
				type_error(type_1, type_2, op_type);
			}
			break;
		/* ---------------------------------------------------------- */
		case NOT_OP: /* CASO ESPECIAL DE NO OPERACION */
			// INT
			if(type_1 == INT_TYPE){
				return INT_TYPE;
			}
			// CHAR
			else if(type_1 == CHAR_TYPE){
				return INT_TYPE;
			}
			else{
				type_error(type_1, type_2, op_type);
			}
			break;
		/* ---------------------------------------------------------- */
		case REL_OP: /* Operaciones Relacionales */
			// INT
			if(type_1 == INT_TYPE){
				// INT, REAL o CHAR
				if(type_2 == INT_TYPE || type_2 == FLOAT_TYPE || type_2 == CHAR_TYPE){
					return INT_TYPE;
				}
				else{
					type_error(type_1, type_2, op_type);
				}
			}
			else if(type_1 == FLOAT_TYPE){
				// INT, REAL o CHAR
				if(type_2 == INT_TYPE || type_2 == FLOAT_TYPE || type_2 == CHAR_TYPE){
					return INT_TYPE;
				}
				else{
					type_error(type_1, type_2, op_type);
				}
			}
			// CHAR
			else if(type_1 == CHAR_TYPE){
				// INT, REAL o CHAR
				if(type_2 == INT_TYPE || type_2 == FLOAT_TYPE || type_2 == CHAR_TYPE){
					return INT_TYPE;
				}
				else{
					type_error(type_1, type_2, op_type);
				}
			}
			else{
				type_error(type_1, type_2, op_type);
			}
			break;
		/* ---------------------------------------------------------- */
		case EQU_OP: /* Operadores de Igualdad */
			// INT
			if(type_1 == INT_TYPE){
				// INT or CHAR
				if(type_2 == INT_TYPE || type_2 == CHAR_TYPE){
					return INT_TYPE;
				}
				else{
					type_error(type_1, type_2, op_type);
				}
			}
			else if(type_1 == FLOAT_TYPE){
				// FLOAT
				if(type_2 == FLOAT_TYPE){
					return INT_TYPE;
				}
				else{
					type_error(type_1, type_2, op_type);
				}
			}
			// CHAR
			else if(type_1 == CHAR_TYPE){
				// INT o CHAR
				if(type_2 == INT_TYPE || type_2 == CHAR_TYPE){
					return INT_TYPE;
				}
				else{
					type_error(type_1, type_2, op_type);
				}
			}
			else{
				type_error(type_1, type_2, op_type);
			}
			break;
		/* ---------------------------------------------------------- */
		default: /* Caso default */
			fprintf(stderr, "Error en seleccion de operador!\n");
			exit(1);
	}
}

/* Imprimir el tipo de error */
void type_error(int type_1, int type_2, int op_type){ 
	fprintf(stderr, "Conflicto de datos entre %d y %d usando el operador del tipo %d\n", type_1, type_2, op_type);
	exit(1);
}