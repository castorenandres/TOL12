from sly import Parser
from theOnlyLonelyLexer import TheOnlyLonelyLexer
from collections import deque
from funcAndVarTable import FuncTable
from funcAndVarTable import VarTable

class TheOnlyLonelyParser(Parser):
    tokens = TheOnlyLonelyLexer.tokens
    idStack = deque()
    sizeStack = deque()
    funcTypeTemp = 0
    # funcTableID = 0

    # Grammar rules

    @_('PROGRAM programa4 ";" programa2 programa3 principal')
    def programa(self, p):
        print("entra programa")
        print("ids: " + str(len(self.idStack)))
        print("size: " + str(len(self.sizeStack)))
        for x in range(len(self.sizeStack)):
            print(self.sizeStack.pop())
        pass

    @_('ID')
    def programa4(self, p):
        print("entra programa4")
        functTable.addFunc(p.ID, 3)
        print("func table: ")
        functTable.show(0)
        pass

    @_('vars', '')
    def programa2(self, p):
        print("entra programa2")
        pass

    @_('func', '')
    def programa3(self, p):
        print("entra programa3")
        pass

    @_('func2 FUNCTION func5 "(" parametro ")" ";" func3 bloque func4')
    def func(self, p):
        # funcTable = FuncTable()
        # print("id func")
        # print(p.ID)
        # funcTable.addFunc(p.ID, 1)
        # # funcTable.show(0)
        # print(funcTable)
        print("entra func")
        
        pass

    @_('ID')
    def func5(self, p):
        print("entra func5")
        functTable.addFunc(p.ID,self.funcTypeTemp)

    @_('tiposimple', 'VOID')
    def func2(self, p):
        print("entra func2")

        if p[0] == "void":
            self.funcTypeTemp = 3
        else:
            if p.tiposimple[1] == "int":
                self.funcTypeTemp = 1
            else:
                self.funcTypeTemp = 2
            
        print("func type: ", self.funcTypeTemp)
        pass

    @_('vars', '')
    def func3(self, p):
        print("entra func3")
        pass

    @_('func', '')
    def func4(self, p):
        print("entra func4")
        pass

    @_('VARIABLES vars2')
    def vars(self, p):
        # varTable = VarTable()
        # varTable.addVar("x", 1, 0, 4)
        # varTable.show(0)
        print("entra vars")
        pass

    @_('vars3 ":" vars5 ";" vars6')
    def vars2(self, p):
        print("entra vars2")
        print(p.vars3)
        
        pass

    @_('ID "[" CTEI "]" vars4', 'ID vars4')
    def vars3(self, p):
        print("entra vars3")
        print("len de vars3: " + str(len(p)))
        
        if len(p) == 2:
            self.idStack.append(p.ID)
            self.sizeStack.append(0)
            print(p.ID)
        elif len(p) == 5:
            self.idStack.append(p.ID)
            self.sizeStack.append(p.CTEI)
        return p

    @_('"," vars3', '')
    def vars4(self, p):
        print("entra vars4")
        pass

    @_('tiposimple')
    def vars5(self, p):
        print("entra vars5")
        print("Tiposimple: ")
        if p.tiposimple[1] == 'int':
            for x in range(len(self.idStack)):
                varTable.addVar(self.idStack.pop(), 1, self.sizeStack.pop(), None)
                # print(self.idStack.pop(), 'int', self.sizeStack.pop())
        elif p.tiposimple[1] == 'float':
            for x in range(len(self.idStack)):
                varTable.addVar(self.idStack.pop(), 2, self.sizeStack.pop(), None)
                # print(self.idStack.pop(), 'float', self.sizeStack.pop())
        functTable.show(0)
        print(p.tiposimple)
        return p

    @_('vars2', '')
    def vars6(self, p):
        print("entra vars6")
        pass

    @_('PRINCIPAL "(" ")" bloque')
    def principal(self, p):
        print("entra principal")
        pass

    @_('tiposimple ID parametro2')
    def parametro(self, p):
        print("entra parametro")

        if p.tiposimple[1] == 'int':
            varTable.addVar(p.ID, 1, 0, None)
        elif p.tiposimple[1] == 'float':
            varTable.addVar(p.ID, 2, 0, None)

        pass

    @_('"," parametro', '')
    def parametro2(self, p):
        print("entra parametro2")
        pass

    @_('INT', 'FLOAT')
    def tiposimple(self, p):
        print("entra tipo")
        return p

    @_('"{" bloque2 "}"')
    def bloque(self, p):
        print("entra bloque")
        pass

    @_('estatuto bloque2', '')
    def bloque2(self, p):
        print("entra bloque2")
        pass

    @_('asignacion', 'llamada', 'retorno', 'lectura', 'escritura', 'condicion', 'ciclow', 'ciclof', 'funcEspecial')
    def estatuto(self, p):
        print("entra estatuto")
        pass

    @_('ID varibale2')
    def variable(self, p):
        print("entra variable")
        pass

    @_('"[" expresion "]"', '')
    def varibale2(self, p):
        print("entra variable2")
        pass

    @_('variable ASSIGN expresion ";"')
    def asignacion(self, p):
        print("entra asignacion")
        pass

    @_('ID "(" expresion llamada2 ")" ";"')
    def llamada(self, p):
        print("entra llamada")
        pass

    @_('"," expresion llamada2', '')
    def llamada2(self, p):
        print("entra llamada2")
        pass

    @_('RETURN "(" expresion ")" ";"')
    def retorno(self, p):
        print("entra retorno")
        pass

    @_('READ "(" variable ")" ";"')
    def lectura(self, p):
        print("entra lectura")
        pass

    @_('WRITE "(" escritura2 ")" ";"')
    def escritura(self, p):
        print("entra escritura")
        pass

    @_('expresion', 'CTESTRING')
    def escritura2(self, p):
        print("entra escritura2")
        pass

    @_('IF "(" expresion ")" THEN bloque condicion2')
    def condicion(self, p):
        print("entra condicion")
        pass

    @_('ELSE bloque', '')
    def condicion2(self, p):
        print("entra condicion2")
        pass

    @_('WHILE "(" expresion ")" DO bloque')
    def ciclow(self, p):
        print("entra ciclow")
        pass

    @_('FROM variable EQ expresion TO expresion DO bloque')
    def ciclof(self, p):
        print("entra ciclof")
        pass

    @_('punto', 'linea', 'circulo', 'arco', 'penup', 'pendown', 'color', 'grosor', 'limpiar')
    def funcEspecial(self, p):
        print("entra funcEspecial")
        pass

    @_('POINT "(" expresion "," expresion ")" ";"')
    def punto(self, p):
        print("entra punto")
        pass

    @_('CIRCLE "(" expresion ")" ";"')
    def circulo(self, p):
        print("entra circulo")
        pass

    @_('LINE "(" expresion "," linea2 ")" ";"')
    def linea(self, p):
        print("entra linea")
        pass

    @_('VERTICAL', 'HORIZONTAL')
    def linea2(self, p):
        print("entra linea2")
        pass

    @_('ARC "(" expresion "," expresion ")" ";"')
    def arco(self, p):
        print("entra arco")
        pass

    @_('PENUP "(" ")" ";"')
    def penup(self, p):
        print("entra penup")
        pass

    @_('PENDOWN "(" ")" ";"')
    def pendown(self, p):
        print("entra pendown")
        pass

    @_('COLOR "(" expresion "," expresion "," expresion ")" ";"')
    def color(self, p):
        print("entra color")
        pass

    @_('WIDTH "(" expresion ")" ";"')
    def grosor(self, p):
        print("entra grosor")
        pass

    @_('CLEAR "(" ")" ";"')
    def limpiar(self, p):
        print("entra limpiar")
        pass

    @_('expresion2 expresion3')
    def expresion(self, p):
        print("entra expresion")
        pass

    @_('exp')
    def expresion2(self, p):
        print("entra expresion2")
        pass

    @_('expresion4 expresion', '')
    def expresion3(self, p):
        print("entra expresion3")
        pass

    @_('OR')
    def expresion4(self, p):
        print("entra expresion4")
        pass

    @_('exp2 exp3')
    def exp(self, p):
        print("entra exp")
        pass

    @_('expA')
    def exp2(self, p):
        print("entra exp2")
        pass

    @_('exp4 exp', '')
    def exp3(self, p):
        print("entra exp3")
        pass

    @_('AND')
    def exp4(self, p):
        print("entra exp4")
        pass

    @_('expA2 expA3')
    def expA(self, p):
        print("entra expA")
        pass

    @_('expB')
    def expA2(self, p):
        print("entra expA2")
        pass

    @_('expA4 expB', '')
    def expA3(self, p):
        print("entra expA3")
        pass

    @_('LT', 'GT', 'EQ', 'NEQ')
    def expA4(self, p):
        print("entra expA4")
        pass

    @_('expB2 expB3')
    def expB(self, p):
        print("entra expB")
        pass

    @_('termino')
    def expB2(self, p):
        print("entra expB2")
        pass

    @_('expB4 expB', '')
    def expB3(self, p):
        print("entra expB3")
        pass

    @_('PLUS', 'MINUS')
    def expB4(self, p):
        print("entra expB4")
        pass

    @_('termino2 termino3')
    def termino(self, p):
        print("entra termino")
        pass

    @_('factor')
    def termino2(self, p):
        print("entra termino2")
        pass

    @_('termino4 termino', '')
    def termino3(self, p):
        print("entra termino3")
        pass

    @_('MULTIPLY', 'DIVIDE')
    def termino4(self, p):
        print("entra termino4")
        pass

    @_('factor2', 'factor7', 'factor8', 'factor9', 'factor10')
    def factor(self, p):
        print("entra factor")
        pass

    @_('factor3 factor4')
    def factor2(self, p):
        print("entra factor2")
        pass

    @_('"("')
    def factor3(self, p):
        print("entra factor3")
        pass

    @_('factor5 factor6')
    def factor4(self, p):
        print("entra factor4")
        pass

    @_('expresion')
    def factor5(self, p):
        print("entra factor5")
        pass

    @_('")"')
    def factor6(self, p):
        print("entra factor6")
        pass

    @_('CTEI')
    def factor7(self, p):
        print("entra factor7")
        pass

    @_('CTEF')
    def factor8(self, p):
        print("entra factor8")
        pass

    @_('variable')
    def factor9(self, p):
        print("entra factor9")
        pass

    @_('llamada')
    def factor10(self, p):
        print("entra factor10")
        pass

# main
if __name__ == '__main__':
    file = open("prueba.txt", 'r')

    allLines = ""
    for line in file:
        allLines = allLines + line.strip()
    
    lexer = TheOnlyLonelyLexer()
    parser = TheOnlyLonelyParser()

    functTable = FuncTable()
    varTable = VarTable()

    result = parser.parse(lexer.tokenize(allLines))
    print(result)

    file.close()