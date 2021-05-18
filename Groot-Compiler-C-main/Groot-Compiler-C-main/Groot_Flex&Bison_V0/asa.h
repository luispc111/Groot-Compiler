
/* ---------------------TIPOS DE NODOS-------------------------- */

typedef enum Node_Type {
	BASIC_NODE,  // EL ROOT
    
	// DECLARACIONES
	DECL_NODE,   // NUEVA VARIABLE
	CONST_NODE,  // CONSTANTE

	// ESTATUTOS 
	STATEMENTS,  // AGRUPADOR DE ESTATUTOS
	IF_NODE,     // ESTATUTO SI
	ELSIF_NODE,  // ESTATUTO SINO
	FOR_NODE,    // DESDE - HASTA 
	WHILE_NODE,  // MIENTRAS
	ASSIGN_NODE, // ASIGNACION
	SIMPLE_NODE, // CONTINUAR O ROMPER (PARA DETENER CICLOS)
	INCR_NODE,   // INCREMENTAR, DECREMENTAR
	FUNC_CALL,   // LLAMADA DE FUNCION
	PRINT_NODE,  // ESCRIBE
	WRITE_NODE,  // LECTURA

	// EXPRESIONES 
	ARITHM_NODE, // TODAS NUESTRAS EXPRESIONES ARITMETICAS
	BOOL_NODE,   // BOOLEANAS (MANEJANDO ENTEROS) 
	REL_NODE,    // RELACIONALES 
	EQU_NODE,    // DE IGUALDAD

}Node_Type;

/* --------------------TIPOS DE OPERADOR----------------------- */

typedef enum Arithm_op{
	SUM,  // + 
	RES,  // - 
	MUL,  // * o
	DIVI , // / 
    MODU,  // % operador
	INC, // ++
	DEC, // --
}Arithm_op;

typedef enum Bool_op{
	OR_OPE,  // || 
	AND_OPE, // && 
	NOT_OPE  // ! 
}Bool_op;

typedef enum Rel_op{
	MAYOR,        // >
	MENOR,           // < 
	MAYOR_IGUAL,  // >= 
	MENOR_IGUAL    // <= 
}Rel_op;

typedef enum Equ_op{
	IGUALADO,    // ==
	NO_IGUALADO // != 
}Equ_op;


/* -----------------------NODOS ASA------------------------- */

/* NODO BASICO */
typedef struct AST_Node{
    
	enum Node_Type type; // TIPO DE NODO
	struct AST_Node *left;  // HIJO IZQUIERDO
	struct AST_Node *right; // HIJO DERECHO

}AST_Node;

/* Declaraciones */
typedef struct AST_Node_Decl{
	enum Node_Type type; // TIPO DE NODO
	
	// tipo de dato
	int data_type;
	
	// Entradas de la tabla de variables

	list_t **names;
	int names_count;

}AST_Node_Decl;

/* ESTATUTOS */
typedef struct AST_Node_Statements{
	enum Node_Type type; 
	
	struct AST_Node **statements;
	int statement_count;
}AST_Node_Statements;

typedef struct AST_Node_If{
	enum Node_Type type; 
	
	struct AST_Node *condition;
	
	struct AST_Node *if_branch;
	
	struct AST_Node **elsif_branches;
	int elseif_count;
	
	struct AST_Node *else_branch;
}AST_Node_If;

typedef struct AST_Node_Elsif{
	enum Node_Type type; 
	
	struct AST_Node *condition;
	
	struct AST_Node *elsif_branch;
}AST_Node_Elsif;

typedef struct AST_Node_For{
	enum Node_Type type; 
	
	struct AST_Node *initialize;

	struct AST_Node *condition;
	
	struct AST_Node *increment;
	
	struct AST_Node *for_branch;
	list_t *counter;

}AST_Node_For;

typedef struct AST_Node_While{
	enum Node_Type type; 

	struct AST_Node *condition;

	struct AST_Node *while_branch;
}AST_Node_While;

typedef struct AST_Node_Assign{
	enum Node_Type type;
	
	list_t *entry;
	
	int ref; 

	struct AST_Node *assign_val;
}AST_Node_Assign;

typedef struct AST_Node_Simple{
	enum Node_Type type; 
	int statement_type;
}AST_Node_Simple;

typedef struct AST_Node_Incr{
	enum Node_Type type; 
	
	list_t *entry;
	
	int incr_type;
	
	int pf_type; 
}AST_Node_Incr;

typedef struct AST_Node_Const{
	enum Node_Type type; // TIPO DE NODO
	
	// TIPO DE DATO
	int const_type;
	
	// Su valor constante
	Value val;
}AST_Node_Const;

/* EXPRESIONES */

// ARITMETICAS
typedef struct AST_Node_Arithm{
	enum Node_Type type; // Tipo de nodo
	
	// Operador
	enum Arithm_op op;
	
	struct AST_Node *left;  // Hijo izquierdo
	struct AST_Node *right; // Hijo derecho

}AST_Node_Arithm;

// BOOLEANAS
typedef struct AST_Node_Bool{
	enum Node_Type type; 

	enum Bool_op op;
	
	struct AST_Node *left;  
	struct AST_Node *right; 
}AST_Node_Bool;

// RELACIONALES
typedef struct AST_Node_Rel{
	enum Node_Type type; 
	
	enum Rel_op op;
	
	struct AST_Node *left;  
	struct AST_Node *right; 
}AST_Node_Rel;

// IGUALADORES
typedef struct AST_Node_Equ{
	enum Node_Type type; 
	
	enum Equ_op op;
	
	struct AST_Node *left;  
	struct AST_Node *right; 
}AST_Node_Equ;



/* ------------------MANEJO DEL NODO ASA-------------------- */

/* NODO BASICO (RAIZ) */
AST_Node *new_ast_node(Node_Type type, AST_Node *left, AST_Node *right);   

/* DECLARACIONES */
AST_Node *new_ast_decl_node(int data_type, list_t **names, int names_count); // DECLARACIÓN
AST_Node *new_ast_const_node(int const_type, Value val);					 // CONSTANTE

/* ESTATUTOS */
AST_Node *new_statements_node(AST_Node **statements, int statement_count, AST_Node *statement); // ESTATUTOS
AST_Node *new_ast_if_node(AST_Node *condition, AST_Node *if_branch, AST_Node **elsif_branches,int elseif_count, AST_Node *else_branch); // SI                                 
AST_Node *new_ast_elsif_node(AST_Node *condition, AST_Node *elsif_branch);    // SINO
AST_Node *new_ast_for_node(AST_Node *initialize, AST_Node *condition, AST_Node *increment, AST_Node *for_branch); // DESDE
void set_loop_counter(AST_Node *node);                                       // CONTADOR 
AST_Node *new_ast_while_node(AST_Node *condition, AST_Node *while_branch);   // MIENTRAS
AST_Node *new_ast_assign_node(list_t *entry, int ref, AST_Node *assign_val); // ASIGNACIÓN
AST_Node *new_ast_simple_node(int statement_type);							 // CONTINUE O BREAK
AST_Node *new_ast_incr_node(list_t *entry, int incr_type, int pf_type);      // INCREMENTAR DECREMENTAR

/* EXPRESIONES */
AST_Node *new_ast_arithm_node(enum Arithm_op op, AST_Node *left, AST_Node *right); // ARITMETICA
AST_Node *new_ast_bool_node(enum Bool_op op, AST_Node *left, AST_Node *right); // BOOLEANA
AST_Node *new_ast_rel_node(enum Rel_op op, AST_Node *left, AST_Node *right); // RELACIONAL
AST_Node *new_ast_equ_node(enum Equ_op op, AST_Node *left, AST_Node *right); // IGUALDADES

/* IMPRIMIR INFORMACION DEL NODO */
void ast_print_node(AST_Node *node);

/* MOVERNOS POR EL NODO EN PREFIJO */
void ast_traversal(AST_Node *node);		