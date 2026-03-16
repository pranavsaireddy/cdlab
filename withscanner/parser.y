%{
#include <stdio.h>
#include <stdlib.h>
void yyerror(char *s);
int yylex();
%}
%token NUMBER
%left '+' '-'
%left '*' '/'
%%
input: expr { printf("Result = %d\n", $1); }
     ;
expr: expr '+' expr { $$ = $1 + $3; }
    | expr '-' expr { $$ = $1 - $3; }
    | expr '*' expr { $$ = $1 * $3; }
    | expr '/' expr { $$ = $1 / $3; }
    | '(' expr ')'  { $$ = $2; }
    | NUMBER        { $$ = $1; }
    ;
%%
int main(){
    printf("Enter expression: ");
    yyparse();
    return 0;
}
void yyerror(char *s){
    printf("Invalid input\n");
}
