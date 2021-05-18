#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/* ------------------MANEJO DEL NODO ASA-------------------- */

/* NODO BASICO */
AST_Node *new_ast_node(Node_Type type, AST_Node *left, AST_Node *right){
	// ALOCAR MEMORIA
	AST_Node *v = malloc (sizeof (AST_Node));
	
	v->type = type;
	v->left = left;
	v->right = right;

	// DEVUELVE EL RESULTADO
	return v;
}

/* DECLARACIONES */
AST_Node *new_ast_decl_node(int data_type, list_t **names, int names_count){
	// ALOCAR MEMORIA
	AST_Node_Decl *v = malloc (sizeof (AST_Node_Decl));
	
	// set entries
	v->type = DECL_NODE;
	v->data_type = data_type;
	v->names = names;
	v->names_count = names_count;
	
	// DEVOLVER EL NODO CASTEADO
	return (struct AST_Node *) v;
}

/* CONSTANTE */
AST_Node *new_ast_const_node(int const_type, Value val){
	// ALOCAR MEMORIA
	AST_Node_Const *v = malloc (sizeof (AST_Node_Const));
	
	v->type = CONST_NODE;
	v->const_type = const_type;
	v->val = val;
	
	// DEUVELVE EL NODO CASTEADO
	return (struct AST_Node *) v;
}
 
/* EXPRESIONES */
AST_Node *new_ast_arithm_node(enum Arithm_op op, AST_Node *left, AST_Node *right){
	// ALOCAR MEMORIA
	AST_Node_Arithm *v = malloc (sizeof (AST_Node_Arithm));
	
	v->type = ARITHM_NODE;
	v->op = op;
	v->left = left;
	v->right = right;
	
	// DEVUELVE EL NODO CASTEADO
	return (struct AST_Node *) v;
}


AST_Node *new_ast_bool_node(enum Bool_op op, AST_Node *left, AST_Node *right){
	// ALOCAR MEMORIA
	AST_Node_Bool *v = malloc (sizeof (AST_Node_Bool));
	
	v->type = BOOL_NODE;
	v->op = op;
	v->left = left;
	v->right = right;
	
	// DEVOLVER EL NODO CASTEADO
	return (struct AST_Node *) v;
}

AST_Node *new_ast_rel_node(enum Rel_op op, AST_Node *left, AST_Node *right){
	// ALOCAR MEMORIA
	AST_Node_Rel *v = malloc (sizeof (AST_Node_Rel));
	
	v->type = REL_NODE;
	v->op = op;
	v->left = left;
	v->right = right;
	
	// DEVOLVER EL NODO CASTEADO
	return (struct AST_Node *) v;
}

AST_Node *new_ast_equ_node(enum Equ_op op, AST_Node *left, AST_Node *right){
	// ALOCAR MEMORIA
	AST_Node_Equ *v = malloc (sizeof (AST_Node_Equ));
	
	v->type = EQU_NODE;
	v->op = op;
	v->left = left;
	v->right = right;
	
	// DEVOLVER EL NODO CASTEADO
	return (struct AST_Node *) v;	
}


/* IMPRIMIR EL NODO 
void ast_print_node(AST_Node *node){

	 NODOS TEMPORALES 
	AST_Node_Decl *temp_decl;
	AST_Node_Const *temp_const;
	AST_Node_Statements *temp_statements;
	AST_Node_If *temp_if;
	AST_Node_For *temp_for;
	AST_Node_Assign *temp_assign;
	AST_Node_Simple *temp_simple;
	AST_Node_Incr *temp_incr;
	AST_Node_Arithm *temp_arithm;
	AST_Node_Bool *temp_bool;
	AST_Node_Rel *temp_rel;
	AST_Node_Equ *temp_equ;
	
	switch(node->type){

		case BASIC_NODE:
			printf("Nodo basico\n");
			break;

		case DECL_NODE:
			temp_decl = (struct AST_Node_Decl *) node;
			printf("Declaracion de nodo del tipo %d de %d nombres\n",
				temp_decl->data_type, temp_decl->names_count);
			break;

		case CONST_NODE:
			temp_const = (struct AST_Node_Const *) node;
			printf("Nodo constante del tipo %d con valor", temp_const->const_type);
			switch(temp_const->const_type){
				case INT_TYPE:
					printf("%d\n", temp_const->val.ival);
					break;
				case FLOAT_TYPE:
					printf("%.2f\n", temp_const->val.fval);
					break;
				case CHAR_TYPE:
					printf("%c\n",  temp_const->val.cval);
					break;
			}
			break;
			case STATEMENTS:
			temp_statements = (struct AST_Node_Statements *) node;
			printf("Nodo de estatutos con %d estatutos\n", temp_statements->statement_count);
			break;
		case IF_NODE:
			temp_if = (struct AST_Node_If *) node;
			printf("Nodo Si con %d sinos y ", temp_if->elseif_count);
			if(temp_if->else_branch == NULL){
				printf("no mas sinos\n");
			}
			else{
				printf("sino\n");
			}			
			break;
		case ELSIF_NODE:
			printf("Nodo Sino\n");
			break;
		case FOR_NODE:
			temp_for = (struct AST_Node_For *) node;
			printf("Nodo desde con un contador %s\n", temp_for->counter->st_name);
			break;
		case WHILE_NODE:
			printf("Nodo mientras\n");
			break;
		case ASSIGN_NODE:
			temp_assign = (struct AST_Node_Assign *) node;
			printf("Nodo de asignacion con entrada %s\n", temp_assign->entry->st_name);
			break;
		case SIMPLE_NODE:
			temp_simple = (struct AST_Node_Simple *) node;
			printf("Nodo simple con estatuto %d\n", temp_simple->statement_type);
			break;
		case INCR_NODE:
			temp_incr = (struct AST_Node_Incr *) node;
			printf("Nodo de Incr/Decr con entrada %s siendo %d %d\n", 
			temp_incr->entry->st_name, temp_incr->incr_type, temp_incr->pf_type);
			break;
		case ARITHM_NODE:
			temp_arithm = (struct AST_Node_Arithm *) node;
			printf("Nodo aritmetico de operador %d\n", temp_arithm->op);
			break;
		case BOOL_NODE:
			temp_bool = (struct AST_Node_Bool *) node;
			printf("Nodo booleano con operador %d\n", temp_bool->op);
			break;
		case REL_NODE:
			temp_rel = (struct AST_Node_Rel *) node;
			printf("Nodo relacional con operador %d\n", temp_rel->op);
			break;
		case EQU_NODE:
			temp_equ = (struct AST_Node_Equ *) node;
			printf("Nodo de igualdad con operador %d\n", temp_equ->op);
			break;
		default: 
			fprintf(stderr, "ERROR EN SELECCION DE NODO!\n");
			exit(1);
	}
} */


/* MOVIENDONOS POR EL ARBOL
void ast_traversal(AST_Node *node){
	int i;
	
	if(node == NULL){
		return;
	}

	 LOS NODOS IZQUIERDOS Y DERECHOS - TIPOS BASICOS 
	if(node->type == BASIC_NODE || node->type == ARITHM_NODE || node->type == BOOL_NODE
	|| node->type == REL_NODE || node->type == EQU_NODE){
		ast_traversal(node->left);
		ast_traversal(node->right);
		ast_print_node(node); // postfix
	}
	 ESTATUTOS 
	else if(node->type == STATEMENTS){
		AST_Node_Statements *temp_statements = (struct AST_Node_Statements *) node;	
		ast_print_node(node);	
		for(i = 0; i < temp_statements->statement_count; i++){
			ast_traversal(temp_statements->statements[i]);
		}
	}
	 DECISION 
	else if(node->type == IF_NODE){
		AST_Node_If *temp_if = (struct AST_Node_If *) node;	
		ast_print_node(node);	
		printf("Condicion:\n");
		ast_traversal(temp_if->condition);
		
		printf("Branch condicional:\n");
		ast_traversal(temp_if->if_branch);
		
		if(temp_if->elseif_count > 0 ){
			printf("Branch sino:\n");
			for(i = 0; i < temp_if->elseif_count; i++){
				printf("Branch sino multiple%d:\n", i);
				ast_traversal(temp_if->elsif_branches[i]);
			}	
		}
	
		if(temp_if->else_branch != NULL){
			printf("Branch sino final:\n");
			ast_traversal(temp_if->else_branch);
		}
	}
	 SINO 
	else if(node->type == ELSIF_NODE){
		AST_Node_Elsif *temp_elsif = (struct AST_Node_Elsif *) node;
		ast_print_node(node);
		ast_traversal(temp_elsif->condition);
		ast_traversal(temp_elsif->elsif_branch);
	}
	DESDE HASTA 
	else if(node->type == FOR_NODE){
		AST_Node_For *temp_for = (struct AST_Node_For *) node;
		ast_print_node(node);
		printf("Inicializacion:\n");
		ast_traversal(temp_for->initialize);
		printf("Condicion:\n");
		ast_traversal(temp_for->condition);
		printf("Incremento:\n");
		ast_traversal(temp_for->increment);
		printf("Para branch:\n");
		ast_traversal(temp_for->for_branch);
	}
	 MIENTRAS 
	else if(node->type == WHILE_NODE){
		AST_Node_While *temp_while = (struct AST_Node_While *) node;
		ast_print_node(node);
		ast_traversal(temp_while->condition);
		ast_traversal(temp_while->while_branch);
	}
	 ASIGNACIONES 
	else if(node->type == ASSIGN_NODE){
		AST_Node_Assign *temp_assign = (struct AST_Node_Assign *) node;
		ast_print_node(node);
		printf("Asignando:\n");
		ast_traversal(temp_assign->assign_val);
	}
	
	OTROS 
	else{
		ast_print_node(node);
	}
}
*/