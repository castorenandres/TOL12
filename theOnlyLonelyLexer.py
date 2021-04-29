from sly import Lexer

class TheOnlyLonelyLexer(Lexer):
    tokens = { PROGRAM, ID, CTESTRING, CTEI, CTEF, VARIABLES, INT, FLOAT, WRITE, \
        IF, ELSE, THEN, PLUS, MINUS, DIVIDE, MULTIPLY, LT, GT, EQ, NEQ, ASSIGN, FUNCTION, \
        PRINCIPAL, POINT, CIRCLE, LINE, ARC, PENUP, PENDOWN, COLOR, WIDTH, CLEAR, VERTICAL, \
        HORIZONTAL, VOID, RETURN, READ, WHILE, DO, FROM, TO, AND, OR}

    literals = { ':', ';', '[', ']', '{', '}', '(', ')', ',' }

    ignore = ' \t'

    # Tokens and regular expressions
    PRINCIPAL = r'principal'
    PROGRAM = r'program'
    VARIABLES = r'variables'
    FUNCTION = r'function'
    POINT = r'point'
    CIRCLE = r'circle'
    COLOR = r'color'
    CLEAR = r'clear'
    LINE = r'line'
    PENDOWN = r'pendown'
    PENUP = r'penup'
    RETURN = r'return'
    READ = r'read'
    HORIZONTAL = r'horizontal'
    VERTICAL = r'vertical'
    VOID = r'void'
    WHILE = r'while'
    WIDTH = r'width'
    FLOAT = r'float'
    WRITE = r'write'
    FROM = r'from'
    THEN = r'then'
    ELSE = r'else'
    ARC = r'arc'
    INT = r'int'
    IF = r'if'
    DO = r'do'
    TO = r'to'
    AND = r'&'
    OR = r'\|'
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    LT = r'<'
    GT = r'>'
    EQ = r'=='
    NEQ = r'!='
    ASSIGN = r'='
    CTEF = r'\d+\.\d+'
    CTEI = r'\d+'
    PLUS = r'\+'
    MINUS = r'-'
    DIVIDE = r'/'
    MULTIPLY = r'\*'
    CTESTRING = r'\".*?\"'