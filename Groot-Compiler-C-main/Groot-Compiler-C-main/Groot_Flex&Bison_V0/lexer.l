/*** RANGER LANG 2021 - VERSION 0.5 ***/

/** CAMBIOS ALA VERSION ANTERIOR : SE AÑADIO SOPORTE AL ARBOL ABSTRACTO DE SINTAXIS PARA EL MANEJO DE EXPRESIONES BOOLEANAS, DECISIONES, CONDICIONALES, NO CONCIDICIONALES**/

/*** LUIS ADRIAN GARTNER LOPEZ - A00227224 ***/
/*** LUIS ALBERTO PÉREZ CHAPA - A01282564 ***/

/*** Declaraciones de bibliotecas ***/

%option noyywrap

%{
  #include <stdio.h>
  #include <stdlib.h>
  #include <string.h>

  // Tabla de simbolos
  #include "vartab.h"
  
  // Reglas de semantica 
  #include "semantica.h"

  // Arbol de sintaxis abstracto
  #include "asa.h"
  
  // Archivo que necesita Bison para funcionar
  #include "parser.tab.h"
  
  
  int linea=1;
  
  extern FILE *yyin;
  extern FILE *yyout;

  // Para la impresion de tokes - meramente para pruebas
  void ret_print(char *token_type);
  void yyerror();

%}

%x COMENTARIO

/*** EXPRESIONES REGULARES ***/
DIGITO [0-9]
ENTEROVAR [-]?{DIGITO}+
FLOTANTEVAR [-]?{DIGITO}+([.]?{DIGITO}+)?
CHAR \'([^\\"|^\\'])\'
LETRERO \"([^\\"|^\\'])*\"
ID ([a-z][a-zA-Z0-9]*)

/*** REGLAS ***/

%%

"Programa"    {return(PROGRAM);}
"principal"   {return(PRINCIPAL);}
"variables"   {return(VARIABLES);}
"void"        {return(VOID);}
"funcion"     {return(FUNCION);}
"regresa"     {return(REGRESA);}
"lee"         {return(LEE);}
"escribe"     {return(ESCRIBE);}
"si"          {return(SI);}
"entonces"    {return(ENTONCES);}
"sino"        {return(SINO);}
"mientras"    {return(MIENTRAS);}
"hacer"       {return(HACER);}
"desde"       {return(DESDE);}
"hasta"       {return(HASTA);}
"entero"      {return(ENTERO);}
"flotante"    {return(FLOTANTE);}
"char"        {return(CHAR);}

{ID}        {
                 // Mete la variable en la tabla de variables
				         	insert(yytext, strlen(yytext), UNDEF, linea);
							yylval.symtab_item = lookup(yytext);
			        		return(ID);
            }

{ENTEROVAR} { yylval.val.ival  = atoi(yytext); return (ENTEROVAR);}
{FLOTANTEVAR} { yylval.val.fval = atof(yytext); return (FLOTANTEVAR);}
{CHAR}      { yylval.val.cval   = yytext[0];    return (CHAR); }
{LETRERO}   {return(LETRERO);}

"%%".*        {printf("Comerse el comentario en la linea %d ", linea);}

"="         {return(IGUAL);}

"+"         {yylval.val.ival = SUM; return(MAS);}
"-"         {yylval.val.ival = RES; return(MENOS);}
"%"         {yylval.val.ival = MODU; return(MOD);}
"*"         {yylval.val.ival = MUL; return(POR);}
"/"         {yylval.val.ival = DIVI; return(DIV);}

"["         {return(LLI);}
"]"         {return(LLD);}
"{"         {return(BRI);}
"}"         {return(BRD);}
"("         {return(PARI);}
")"         {return(PARD);}

"<"         {yylval.val.ival = MENOR; return(MENORQUE);}
">"         {yylval.val.ival = MAYOR; return(MAYORQUE);}
">="        {yylval.val.ival = MAYOR_IGUAL; return(MAYORIGUALQUE);}
"<="        {yylval.val.ival = MENOR_IGUAL; return(MENORIGUALQUE);}

"!="        {yylval.val.ival = NO_IGUALADO; return(DIFFQUE);}
"=="        {yylval.val.ival = IGUALADO; return(IGUALQUE);}
":"         {return(DOBLEPUNTO);}
";"         {return(PNTOCOMA);}
","         {return(COMA);}
"."         {return(PUNTO);}

"||"         {yylval.val.ival = OR_OPE; return(OR);}
"&&"         {yylval.val.ival = AND_OPE; return(AND);}
"!"          {yylval.val.ival = NOT_OPE; return(NOT);}

"\n"        {linea++;}
[ \t\r\f]     /* Comerse espacios en blanco */
.           { yyerror("Caracter no reconocido");}

%%
/*
void return(char *token_type){
	printf("yytext: %s\ttoken: %s\tlineno: %d\n", yytext, token_type, linea);
}

void yyerror(char *message){
	printf("Error: \"%s\" en linea %d. Token = %s\n", message, linea, yytext);
	exit(1);
}

int main(int argc, char *argv[]){

	// inicializar la tabla de variables
	init_hash_table();

	// abre el input file
	yyin = fopen("prueba.txt", "r");
	
	// Analisis lexico
	yylex();
	fclose(yyin);
	
	
	// symbol table dump
	yyout = fopen("symtab_dump.out", "w");
	symtab_dump(yyout);
	fclose(yyout);	
	
	return 0;
}
*/