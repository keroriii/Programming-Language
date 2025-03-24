%{
#include "parser.tab.h"  // Include Bison's header file
%}

%%

[0-9]+  { yylval.num = atoi(yytext); return NUMBER; }  // Use yylval.num
[\t ]+   ;  // Ignore spaces and tabs
"+"      { return PLUS; }  // Recognize '+'
"-"      { return MINUS; } // Recognize '-'
\n       { return 0; }  // End of input
.        { return yytext[0]; }  // Catch-all for unknown characters

%%

int yywrap() { return 1; }
