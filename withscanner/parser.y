%{
#include <stdio.h>
#include <stdlib.h>
void yyerror(char *s);
int yylex();
%}

%token NUMBER

%%
expr: expr '+' expr   { printf("Addition\n"); }
    | expr '-' expr   { printf("Subtraction\n"); }
    | expr '*' expr   { printf("Multiplication\n"); }
    | expr '/' expr   { printf("Division\n"); }
    | NUMBER
    ;
%%

int main() {
    printf("Enter expression: ");
    yyparse();
    return 0;
}

void yyerror(char *s){
    printf("Invalid expression\n");
}
