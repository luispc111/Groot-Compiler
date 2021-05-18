#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// Semantica
#include "semantica.h"

// Header
#include "vartab.h"

/* scope actual */
int cur_scope = 0;
int declare = 0;


/* CREACIÓN DE LA TABLA HASH */
void init_hash_table(){
  int i; 
  // Asignamos tamaño de la tabla
  hash_table = malloc(SIZE * sizeof(list_t*));
  // Inicializar nuestra tabla de variables en NULL
  for(i = 0; i < SIZE; i++) 
    hash_table[i] = NULL;
}

// Funcion de hash 
unsigned int hash(char *key){
  unsigned int hashval = 0;
  for(;*key!='\0';key++) hashval += *key;
  hashval += key[0] % 11 + (key[0] << 3) - key[0];
  return hashval % SIZE;
}

/* INSERTA UN ID EN LA HASH TABLE */
void insert(char *nombre, int tamano, int tipo, int lineno){

  unsigned int hashval = hash(nombre);
  list_t *l = hash_table[hashval];
    
  while ((l != NULL) && (strcmp(nombre,l->st_name) != 0)) l = l->next;
    
  /* cuando la variable no está en la tabla hash */
  if (l == NULL){
    l = (list_t*) malloc(sizeof(list_t));
    strncpy(l->st_name, nombre, tamano);  

    /* añadir a la tabla hash */
    l->st_tipo = tipo;
    l->scope = cur_scope;
	// Aqui añadimos ala lista la linea de referencia encontrada
    l->lines = (RefList*) malloc(sizeof(RefList));
    l->lines->lineno = lineno;
    l->lines->next = NULL;

    /* push ala tabla */
    l->next = hash_table[hashval];
    hash_table[hashval] = l;

    /* checar errores */
    printf("Se insertó %s en linea %d!\n", nombre, lineno);
  }
  /* se encontró en la tabla */
  else{
    // Solo añade el numero de linea en el que se encontro
		if(declare == 0){
			/* Encuentra la ultima referencia */
			RefList *t = l->lines;
			while (t->next != NULL) t = t->next;
			
			/* Suma el numero ala lista de referencias */
			t->next = (RefList*) malloc(sizeof(RefList));
			t->next->lineno = lineno;
			t->next->next = NULL;
			printf("Se econtro %s de nuevo en la linea %d!\n", nombre, lineno);
  }
  else{
			/* En el caso que se haya declarado multiples veces en el mismo nivel de scope - da un warning */
			if(l->scope == cur_scope){
				fprintf(stderr, "Una declaracion multiple de variable %s en la linea %d\n", nombre, lineno);
 				exit(1);
			}
			/* Si esta en otro scope - registro nuevo*/
			else{
				/* Crea una entrada */
				l = (list_t*) malloc(sizeof(list_t));
				strncpy(l->st_name, nombre, tamano);  
				l->st_tipo = tipo;
				l->scope = cur_scope;
				l->lines = (RefList*) malloc(sizeof(RefList));
				l->lines->lineno = lineno;
				l->lines->next = NULL;
				
				/* Metelo ala tabla de hash - tabla de variables */
				l->next = hash_table[hashval];
				hash_table[hashval] = l; 
				printf("Se inserto %s para un nuevo scope en la linea %d!\n", nombre, lineno);
			}	
		}		
  }

}
 
/* Esta funcion regresa el símbolo/NULL que se encontró */
list_t *lookup(char *nombre){
  unsigned int hashval = hash(nombre);
  list_t *l = hash_table[hashval];

  while ((l != NULL) && (strcmp(nombre,l->st_name) != 0)) 
    l = l->next;

  /* cuando encuentre NULL */
  return l;
}
 
/* BUSCA UN ID DENTRO DE UN NIVEL DE SCOPE */
list_t *lookup_scope(char *nombre, int scope){
  
  unsigned int hashval = hash(nombre);
  list_t *l = hash_table[hashval];
  
  while ((l != NULL) && (strcmp(nombre,l->st_name) != 0) && (scope != l->scope)) 
    l = l->next;
  
  /* cuando encuentre NULL */ 
  return l;
}

/* esconder bloque */
void hide_scope(){
	list_t *l;
	int i;
	printf("Ocultando el scope \'%d\':\n", cur_scope);
	/* Para todas las tablas */
	for (i = 0; i < SIZE; i++){
		if(hash_table[i] != NULL){
			l = hash_table[i];
			/* Encuentra el primer elemento de otro scupe */
			while(l != NULL && l->scope == cur_scope){
				printf("Ocultando %s..\n", l->st_name);
				l = l->next;
			}
			/* Set the list equal to that item */
			hash_table[i] = l;
		}
	}
	cur_scope--;
}

// Tipos de funciones
void set_type(char *name, int st_tipo, int inf_type){ // Para declaraciones
	/* Encuentra el nombre de la variable */
	list_t *l = lookup(name);
	
	/* Convierte su tipo al que debe ser */
	l->st_tipo = st_tipo;	
	
	/* Si es un array o funcion */
	if(inf_type != UNDEF){
		l->inf_type = inf_type;
	}	

}

int get_type(char *name){ // Obten el tipo de una variable
	/* lookup */
	list_t *l = lookup(name);
	
	/* Si es de nuestros tipos BASICOS */
	if(l->st_tipo == INT_TYPE || l->st_tipo == FLOAT_TYPE || l->st_tipo == CHAR_TYPE){
		return l->st_tipo;
	}
	/* Si es un array o funcion */
	else{
		return l->inf_type;
	}
}

/* Sube el nivel del scope (esto para cuando entremos a
 bloques condicionales, no condicionales o funciones */

void incr_scope(){
  cur_scope++;
}
 
/* IMPRESIÓN DE REGISTROS - DUMPFILE */ 
void symtab_dump(FILE * of){  
  int i;
  fprintf(of,"------------ ------ ------ ------------\n");
  fprintf(of,"Nombre        Tipo   Nivel  Lineas de referencia\n");
  fprintf(of,"------------ ------ ------ ------------\n");
  for (i=0; i < SIZE; ++i){ 
	if (hash_table[i] != NULL){ 
		list_t *l = hash_table[i];
		while (l != NULL){ 
			RefList *t = l->lines;
			fprintf(of,"%-12s ",l->st_name);
			if (l->st_tipo == INT_TYPE) fprintf(of,"%-7s","int");
			else if (l->st_tipo == FLOAT_TYPE) fprintf(of,"%-7s","float");
			else if (l->st_tipo == CHAR_TYPE) fprintf(of,"%-7s","char");
			else if (l->st_tipo == ARRAY_TYPE){
				fprintf(of,"array de ");
				if (l->inf_type == INT_TYPE) 		   fprintf(of,"%-7s","int");
				else if (l->inf_type  == FLOAT_TYPE)    fprintf(of,"%-7s","float");
				else if (l->inf_type  == CHAR_TYPE) 	   fprintf(of,"%-7s","char");
				else fprintf(of,"%-7s","undef");
			}
			else if (l->st_tipo == FUNCTION_TYPE){
				fprintf(of,"%-7s %s","funcion devuelve ");
				if (l->inf_type == INT_TYPE) 		   fprintf(of,"%-7s","int");
				else if (l->inf_type  == FLOAT_TYPE)    fprintf(of,"%-7s","float");
				else if (l->inf_type  == CHAR_TYPE) 	   fprintf(of,"%-7s","char");
				else fprintf(of,"%-7s","undef");
			}
			else fprintf(of,"%-7s","undef");
			fprintf(of,"  %d  ",l->scope);
			while (t != NULL){
				fprintf(of,"%4d ",t->lineno);
			t = t->next;
			}
			fprintf(of,"\n");
			l = l->next;
		}
    }
  }
}