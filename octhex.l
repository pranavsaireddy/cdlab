%{
#include <stdio.h>
%}

%%
0[xX][0-9a-fA-F]+    { printf("Hexadecimal number\n"); }
0[0-7]+              { printf("Octal number\n"); }
[0-9]+               { printf("Decimal number\n"); }
[ \t]+               ; 
\n                   return 0;
.                    { printf("Invalid input\n"); }
%%

int main(){
    printf("Enter a number: ");
    yylex();
    return 0;
}

int yywrap(){
    return 1;
}
