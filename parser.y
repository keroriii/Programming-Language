%{
#include <stdio.h>
#include <stdlib.h>

void yyerror(const char *s);
int yylex(void);
%}

%union {
    int num;
}

%token <num> NUMBER
%token PLUS MINUS

%type <num> expression  // Declare the type of expression

%left PLUS MINUS  // Define precedence for left-associative operators

%%

expression:
    expression PLUS expression  { $$ = $1 + $3; printf("Result: %d\n", $$); }
  | expression MINUS expression { $$ = $1 - $3; printf("Result: %d\n", $$); }
  | NUMBER                      { $$ = $1; }
  ;

%%

int main() {
    printf("Enter an expression (e.g., 5 + 3): ");
    yyparse();
    return 0;
}

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}
