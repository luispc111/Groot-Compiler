/* Tipos de datos - token */
#define UNDEF 0
#define INT_TYPE 1
#define FLOAT_TYPE 2
#define CHAR_TYPE 3
#define ARRAY_TYPE 4
#define FUNCTION_TYPE 5
#define VOID_TYPE 6
#define CLASS_TYPE 7

/* Tipos de operador */
#define NONE 0		// Solo para checar 
#define ARITHM_OP 1 // SUMA, MULTIPLICACION, DIVISIÓN, MODULO
#define INCR_OP 2   // INCREMENTAR DECREMENTAR (++ --)
#define BOOL_OP 3   // AND Y OR
#define NOT_OP 4    // NOT
#define REL_OP 5    // RELACIONAL (<=, >=, >, <)
#define EQU_OP 6    // IGUALACION (==, !=)

// Declaracion de funciones

/* Chequeo de nuestros operadores CON el operando (ACCEDER AL CUBO SEMANTICO)*/
int get_result_type (int type_1, int type_2, int op_type); 

/* Imprimimos el TIPO de error para cada caso */
void type_error(int type_1, int type_2, int op_type);      