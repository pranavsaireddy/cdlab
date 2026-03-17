%{
#include <stdio.h>
#include <ctype.h>

int yylex();
void yyerror(char *s);
%}

%token DIGIT

%left '+' '-'
%left '*' '/'

%%
start: expr { printf("Result = %d\n", $1); }
     ;

expr: expr '+' expr { $$ = $1 + $3; }
    | expr '-' expr { $$ = $1 - $3; }
    | expr '*' expr { $$ = $1 * $3; }
    | expr '/' expr { $$ = $1 / $3; }
    | DIGIT         { $$ = $1; }
    ;
%%

int yylex() {
    int c = getchar();

    if (isdigit(c)) {
        yylval = c - '0';   // convert char → integer
        return DIGIT;
    }

    return c; // + - * / or newline
}

int main() {
    printf("Enter expression: ");
    yyparse();
    return 0;
}

void yyerror(char *s) {
    printf("Invalid expression\n");
}
