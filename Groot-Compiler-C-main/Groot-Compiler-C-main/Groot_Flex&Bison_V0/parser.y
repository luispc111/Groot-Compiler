
/*** RANGER LANG 2021 - VERSION 0.4 ***/

/*** LUIS ADRIAN GARTNER LOPEZ - A00227224 ***/
/*** LUIS ALBERTO PÉREZ CHAPA - A01282564 ***/

/*** Declaraciones de bibliotecas  RECONOCEDOR DE LINEAS, APERTURA DE ARCHIVOS, Y CAPTURA DE ERROR***/
%{

        
  // Analisis semantico
  #include "semantica.c"

  // Tabla de variables
  #include "vartab.c"

  // Manejo del arbol de semantica abstracta
  #include "asa.h"
  #include "asa.c"
  

  #include <stdio.h>
  #include <stdlib.h>
  #include <string.h>
  #include <math.h>
 


  extern char *yytext;
  extern int linea;

  extern FILE *yyin;
  extern FILE *yyout;
  
  extern int yylex();
  void yyerror();
   
   // para las declaraciones de variables
   void sum_a_nombres(list_t *entrada);
   list_t **names;
   int nc = 0;

   // Para las decisiones
   void add_elseif(AST_Node *elsif); 
   AST_Node **elsifs;
   int elseif_count = 0;

%}

// Union de variables
%union{

        // Valores diferentes
        Value val;

        // Nodo de arbol sintatico abstracto
        AST_Node* node;
        
        // Tabla de variables
        list_t* symtab_item;

        // Para declaraciones de datos y constantes
        int data_type;
        int const_type;

}


/*** Tipo de datos SIMPLES ***/ 
%token <val> ENTERO 
%token <val> FLOTANTE 
%token <val> CHAR
%token <symtab_item> ID
%token <symtab_item> CLASSID

%token <val> ENTEROVAR
%token <val> FLOTANTEVAR
%token <val> CHARVAR

%token LETRERO

/*** Operadores aritmeticos ***/ 
%token <val> MAS
%token <val> MENOS
%token <val> IGUAL
%token <val> POR
%token <val> DIV
%token <val> MOD

/*** Separadores ***/ 
%token <val> COMA
%token <val> PNTOCOMA
%token <val> DOBLEPUNTO
%token <val> PUNTO

/*** Corchos, parentesis y llaves ***/ 
%token <val> BRI
%token <val> BRD
%token <val> PARI
%token <val> PARD
%token <val> LLI
%token <val> LLD

/*** Comparadores ***/ 
%token <val> MAYORQUE MAYORIGUALQUE 
%token <val> MENORQUE MENORIGUALQUE
%token <val> DIFFQUE
%token <val> IGUALQUE

/*** Operadores binarios ***/ 
%token <val> AND
%token <val> OR
%token <val> NOT

/*** Palabras reservadas / indicadores ***/

%token <val> PROGRAM 
%token <val> PRINCIPAL
%token <val> CLASE
%token <val> HEREDA
%token <val> ATRIBUTOS
%token <val> METODOS
%token <val> VARIABLES
%token <val> VOID 
%token <val> FUNCION
%token <val> REGRESA
%token <val> LEE
%token <val> ESCRIBE
%token <val> SI
%token <val> SINO
%token <val> ENTONCES
%token <val> MIENTRAS
%token <val> HACER
%token <val> DESDE
%token <val> HASTA

/*** precedencias aritmeticas ***/ 

%left MAS MENOS   /* AQUI COLOCAMOS PARA EL MAS Y MENOS */
%left POR DIV  /* AQUI COLOCAMOS PARA LA MULTIPLICACION Y DIVISION */
%right MOD    /* EL MODULO ES ASOCIATIVO ALA DERECHA */
%left PARI PARD BRI BRD
%left IGUALQUE
%left AND
%left OR
%left COMA

/*** precedencia de asignación ***/ 
%right IGUAL 

/* definiciones de reglas */
%type <node> program
//%type <symtab_item> variablesu
%type <data_type> tipovar
%type <node> variablesu

%start program

%% 

program: PROGRAM ID PNTOCOMA classes var funciones PRINCIPAL PARI PARD bloque { printf("Código Apropiado \n"); } 
        ;

classes: /* empty */
        | class classes
        ;

class: { printf("Se crea clase \n"); } CLASE CLASSID classu BRI atributos metodos BRD PNTOCOMA 
     ;

classu: /* empty */
       | MENORQUE HEREDA CLASSID MAYORQUE PNTOCOMA  { printf("  Existe herencia \n"); } 
       ;

variables: VARIABLES variablesu {
         printf("Seccion de variables \n"); 
} 
          ;

variablesu: ID {/* declare = 0; */} variablesd DOBLEPUNTO tipodeclarar {/* declare = 1; */} PNTOCOMA variablest { printf("  Declaracion de variables \n"); 
 	{ /*
                sum_a_nombres($1);
		int i;
		$$ = new_ast_decl_node($4, names, nc);
		nc = 0;
		AST_Node_Decl *temp = (AST_Node_Decl*) $$;
		
		// Declarar los tipos de variables
		for(i=0; i < temp->names_count; i++){
			// Variables
			if(temp->names[i]->st_tipo == UNDEF){
				set_type(temp->names[i]->st_name, temp->data_type, UNDEF);
			}
		}
		ast_traversal($$); 
          */
	}
       ;
       } 
          ;

variablesd: /* empty */
           | COMA ID variablesd
           ;

variablest: /* empty */
          | variablesu
          ; 

var: /* empty */
    | variables
    ;


atributos: /* empty */
          | ATRIBUTOS variablesu
          ;

metodos: /* empty */
        | { printf("  Declaracion de métodos \n"); }  METODOS funcion funciones 
        ;


funcion: { incr_scope(); } funcionu FUNCION ID PARI params PARD var bloque
         ;

funcionu: tipovar 
         | VOID
         ;

funciones: /* empty */
          | funcion funciones
          ;


tipovar: ENTERO  {/* $$= INT_TYPE; */}
        | FLOTANTE {/* $$ = FLOAT_TYPE; */}
        | CHAR {/* $$ = CHAR_TYPE; */ }
        ;

tipodeclarar: tipovar
            | CLASSID
            ;

params: /* empty */
       | param
       ;

param: ID DOBLEPUNTO tipovar paramu
      ;

paramu: /* empty */
       | COMA param
       ;

bloque: BRI bloqueu BRD
       ;

bloqueu: /* empty */
        | { printf("  Estatuto \n"); } estatuto bloqueu
        ;

estatuto: asignacion PNTOCOMA
         | lectura
         | escritura
         | decision
         | condicional
         | ncondicional
         | llamada PNTOCOMA
         | return
         ;

asignacion: id IGUAL h_exp { printf("    Asignación exitosa \n"); }
           ;

lectura: LEE PARI lecturau PARD PNTOCOMA { printf("    Lectura exitosa \n"); }
        ;

lecturau: ID lecturad
         ;

lecturad: /* empty */
         | COMA lecturau
         ;

escritura: ESCRIBE PARI escriturau PARD PNTOCOMA { printf("    Escritura exitosa \n"); }
          ;

escriturau: LETRERO escriturad
           | h_exp escriturad
           ;

escriturad: /* empty */
           | COMA escriturau
           ;

decision: SI PARI h_exp PARD ENTONCES bloque decisionu { printf("    Decisión exitosa \n"); }
         ;

decisionu: /* empty */
         | SINO bloque 
         ;

condicional: MIENTRAS PARI h_exp PARD HACER bloque { printf("    Condicional exitosa \n"); }
            ;

ncondicional: DESDE asignacion HASTA h_exp HACER bloque { printf("    NCondicional exitosa \n"); }
             ;

llamada: id PARI llamadau PARD { printf("    Llamada exitosa \n"); }
        ;

llamadau: /* empty */
         | factor llamadad
         ;

llamadad: COMA llamadau
         ;


return: REGRESA PARI h_exp PARD PNTOCOMA { printf("    Regresa exitoso \n"); }
       ;

exp: termino expu
    ;

expu: /* empty */
     | operadorA exp 
     ;

operadorA: MAS
         { 
	          /*Creacion de nodo aritmetico*/ 
	}
         | MENOS
         { 
	         /*Creacion de nodo aritmetico*/
	}
         ;

operadorT: POR
         {
	         /*Creacion de nodo aritmetico*/
	}
         | DIV
         {
		/*Creacion de nodo aritmetico*/
	}
         | MOD
         {
               /*Creacion de nodo aritmetico*/
         }
         ;

operadorL: OR
         | AND
         ;

operadorR: MENORQUE 
         | MAYORQUE
         | DIFFQUE
         | IGUALQUE
         ;

termino: factor terminou
       ;

terminou: /* empty */
        | operadorT termino
        ;

factor: id 
        | llamada
        | ENTEROVAR 
        | FLOTANTEVAR
        | CHARVAR
        | PARI h_exp PARD
        ;

s_exp: exp s_expu
     ;

s_expu: /* empty */
      | operadorR exp
      ;

h_exp: s_exp h_expu
     ;

h_expu: /* empty */
      | operadorL h_exp
      ;

id: ID idu
   ;

idu: /* empty */ 
    | LLI h_exp idd LLD
    | PUNTO id
    ;

idd: /* empty */
    | COMA h_exp
    ;
    
%%

/*** En caso de un error imprimir el mensaje y el caracter ***/
void yyerror()
{
  printf("Error sintactico en linea %d \n", linea);  
}
/* 
void sum_a_nombres(list_t *entrada){

	if(nc == 0){
		nc = 1;
		names = (list_t **) malloc( 1 * sizeof(list_t *));
		names[0] = entrada;
	}
	else{
		nc++;
		names = (list_t **) realloc(names, nc * sizeof(list_t *));
		names[nc - 1] = entrada;		
	}
}
 */

/*** Rutina de lectura de archivo para su parsing ***/
int main(int argc,char *argv[])
{ 
        // inicializar la tabla de variables
        init_hash_table();

        // parseo
        int bandera;
        yyin = fopen("prueba.txt","r");
        bandera = yyparse();
        fclose(yyin);

        printf("Parseo terminado ! \n");
        
        // Generar tabla de variables
        yyout = fopen("tabla_variables.txt", "w");
        symtab_dump(yyout);
        fclose(yyout);

        return bandera;
}