%{
#include <stdio.h>
#include <ctype.h>

int yylex();
void yyerror(char *s);
%}

%%
expr: expr '+' expr { printf("Addition\n"); }
    | expr '-' expr { printf("Subtraction\n"); }
    | expr '*' expr { printf("Multiplication\n"); }
    | expr '/' expr { printf("Division\n"); }
    | NUMBER
    ;

NUMBER: NUMBER DIGIT
      | DIGIT
      ;

DIGIT: '0' | '1' | '2' | '3' | '4'
     | '5' | '6' | '7' | '8' | '9'
     ;
%%

int yylex(){
    int c = getchar();
    if(isdigit(c)) return DIGIT;
    return c;
}

int main(){
    printf("Enter expression: ");
    yyparse();
}

void yyerror(char *s){
    printf("Invalid expression\n");
}
