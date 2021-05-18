/* Tamaño maximo de la tabla de hash - 200 variables */
#define SIZE 200
 
/* Tamaño maximo de nuestro tokens */
#define MAXTOKENLEN 40
 
/* Como se manda el token - por valor o por referencia - CONSIDERANDO POINTERS??? */
#define BY_VALUE 1
#define BY_REFER 2
 
typedef union Value{
	int ival;
	double fval;
	char cval;
	char *sval; // EN EL CASO QUE SI QUERAMOS MANEJAR STRINGS
}Value;


/* Struct de parametro */
typedef struct Param{
  int par_tipo;
  char param_name[MAXTOKENLEN];

  // para guardar el parametro
  Value val;
  int passing; // valor o referencia

}Param;
 
/* Una lista encadenada de referencias ( y su lineas de referencia (por cada vez que se encuentran))*/
typedef struct RefList{ 
  int lineno;
  struct RefList *next;
  int type;
}RefList;
 
// Nodo de lista - "TABLA DE VARIABLES - LISTAS"
typedef struct list_t{
  char st_name[MAXTOKENLEN];
  int st_tamano;
  int scope;
  RefList *lines;

  // Para insertar valores y alguna otra informacion 
  int st_ival; double st_fval; char *st_sval;

  // Tipo de dato
  int st_tipo;

  // Para manejo de arrays (su tipo de array o tipo de regreso en funciones)
  int inf_type;
    
  // Valores y caracteristicas del array
  Value *vals;
  int array_size;

  // Parametros de una funcion, asi como numero de parametros
  Param *parameters;
  int num_of_pars;

  // Pointer para el siguiente elemento de nuestra lista
  struct list_t *next;

}list_t;
 

 /* Fila de identificadores a vistar */
typedef struct revisit_queue{
	// nombre del identificador
	char *st_name;
	
	// tipo de revisita
	int revisit_type;
	
  // Siguiente en la lista
	struct revisit_queue *next;

}revisit_queue;

/* revisit types */
#define PARAM_CHECK 1 /* Check parameters of function call when functions gets declared */

/* TABLA DE HASH - DIRECTORIO DE SCOPES / FUNCIONES  Y LA FILA DE REVISION */
static list_t **hash_table;
static revisit_queue *queue;

// inicializar la tabla de hash
void init_hash_table(); 

// Creacion de la hash function
unsigned int hash(char *key); 

//------- Metodos para inserción (PUT) y Consulta (GET) de la tabla de hash ----------//

// Insertar -    ID  -  TAMAÑO  -  TIPO  - LINEA DE CODIGO 
void insert(char *nombre, int tamano, int tipo, int lineno); 

// Consultar -    ID  
list_t *lookup(char *nombre);

// Funciones de tipo
void set_type(char *name, int st_type, int inf_type); // Para declaraciones
int get_type(char *name); // Conseguir el tipo de una funcion

// Consultar scope / Nivel en el programa -     ID
list_t *lookup_scope(char *nombre, int scope);

// Cubre un scope especifico
void hide_scope();

// Incrementa el nivel del scope actual
void incr_scope();

// DUMP - Para impresion de la tabla y su analisis
void symtab_dump(FILE *of);