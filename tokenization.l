%{
#include <stdio.h>
%}

%%
[0-9]+        { printf("%s -> NUMBER\n", yytext); }
[a-zA-Z]+     { printf("%s -> IDENTIFIER\n", yytext); }
[+\-*/=]      { printf("%s -> OPERATOR\n", yytext); }
[ \t\n]       ; 
.             { printf("%s -> UNKNOWN\n", yytext); }
%%

int main()
{
    printf("Enter expression: ");
    yylex();
    return 0;
}

int yywrap()
{
    return 1;
}
