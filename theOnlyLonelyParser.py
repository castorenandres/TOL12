from sly import Parser
from theOnlyLonelyLexer import TheOnlyLonelyLexer
from collections import deque
from funcAndVarTable import FuncTable
from funcAndVarTable import VarTable

class TheOnlyLonelyParser(Parser):
    tokens = TheOnlyLonelyLexer.tokens
    funcTypeTemp = 0
    quadCount = 1
    # scopeFunc = 0
    currFuncName = ''
    quadruples = {}
    idStack = deque()
    sizeStack = deque()
    poper = deque()
    pilaO = deque()
    pTypes = deque()
    pJumps = deque()

    # contadores para memorias

    # siguiendo el codigo para tipos: int -> 1, float -> 2
    # siguiendo el codigo para operadores : 
        # 1 -> +
        # 2 -> -
        # 3 -> *
        # 4 -> /
        # 5 -> ==
        # 6 -> !=
        # 7 -> >
        # 8 -> <
        # 9 -> &
        # 10 -> |
    # cuando no se puede hacer la operacion se tiene un -1
    semCube = {
        1: {
            1: {
                1: 1,
                2: 1,
                3: 1,
                4: 1,
                5: 1,
                6: 1,
                7: 1,
                8: 1,
                9: 1,
                10: 1,
                11: 1
            },
            2: {
                1: 2,
                2: 2,
                3: 2,
                4: 2,
                5: 1,
                6: 1,
                7: 1,
                8: 1,
                9: -1,
                10: -1,
                11: -1
            }
        },
        2: {
            1: {
                1: 2,
                2: 2,
                3: 2,
                4: 2,
                5: 1,
                6: 1,
                7: 1,
                8: 1,
                9: -1,
                10: -1,
                11: 2
            },
            2: {
                1: 2,
                2: 2,
                3: 2,
                4: 2,
                5: 1,
                6: 1,
                7: 1,
                8: 1,
                9: -1,
                10: -1,
                11: 2
            }
        }
    }
    
    def semantics (self, t_left, t_right, op):
        return self.semCube[t_left][t_right][op]

    def generateQuad (self, op, left, right, res):
        self.quadCount = self.quadCount + 1
        tempQuad = {
            "op": op,
            "left": left,
            "right": right,
            "res": res
        }
        self.quadruples[self.quadCount-1] = tempQuad

    # Grammar rules

    @_('PROGRAM programa4 ";" programa2 programa3 principal')
    def programa(self, p):
        print("entra programa")
        print("ids: " + str(len(self.idStack)))
        print("size: " + str(len(self.sizeStack)))
        print(functTable.show())
        print("ptypes: ", self.pTypes)
        print(self.quadruples)
        pass

    @_('ID')
    def programa4(self, p):
        print("entra programa4")
        functTable.addFunc(p.ID, 3)
        self.currFuncName = p.ID
        print("func table: ")
        functTable.show()
        return p

    @_('vars', '')
    def programa2(self, p):
        print("entra programa2")
        return p

    @_('func', '')
    def programa3(self, p):
        print("entra programa3")
        return p

    @_('func2 FUNCTION func5 "(" parametro ")" ";" func3 bloque func4')
    def func(self, p):
        # funcTable = FuncTable()
        # print("id func")
        # print(p.ID)
        # funcTable.addFunc(p.ID, 1)
        # # funcTable.show(0)
        # print(funcTable)
        print("entra func")
        
        return p

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
        return p

    @_('vars', '')
    def func3(self, p):
        print("entra func3")
        return p

    @_('func', '')
    def func4(self, p):
        print("entra func4")
        return p

    @_('VARIABLES vars2')
    def vars(self, p):
        # varTable = VarTable()
        # varTable.addVar("x", 1, 0, 4)
        # varTable.show(0)
        print("entra vars")
        return p

    @_('vars3 ":" vars5 ";" vars6')
    def vars2(self, p):
        print("entra vars2")
        print(p.vars3)
        
        return p

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
        return p

    @_('tiposimple')
    def vars5(self, p):
        print("entra vars5")
        print("Tiposimple: ")
        if p.tiposimple[1] == 'int':
            for x in range(len(self.idStack)):
                varTable.addVar(self.idStack.pop(), 1, self.sizeStack.pop())
                # print(self.idStack.pop(), 'int', self.sizeStack.pop())
        elif p.tiposimple[1] == 'float':
            for x in range(len(self.idStack)):
                varTable.addVar(self.idStack.pop(), 2, self.sizeStack.pop())
                # print(self.idStack.pop(), 'float', self.sizeStack.pop())
        functTable.show()
        print(p.tiposimple)
        return p

    @_('vars2', '')
    def vars6(self, p):
        print("entra vars6")
        return p

    @_('PRINCIPAL "(" ")" bloque')
    def principal(self, p):
        print("entra principal")
        return p

    @_('tiposimple ID parametro2')
    def parametro(self, p):
        print("entra parametro")

        if p.tiposimple[1] == 'int':
            varTable.addVar(p.ID, 1, 0)
        elif p.tiposimple[1] == 'float':
            varTable.addVar(p.ID, 2, 0)

        return p

    @_('"," parametro', '')
    def parametro2(self, p):
        print("entra parametro2")
        return p

    @_('INT', 'FLOAT')
    def tiposimple(self, p):
        print("entra tipo")
        return p

    @_('"{" bloque2 "}"')
    def bloque(self, p):
        print("entra bloque")
        return p

    @_('estatuto bloque2', '')
    def bloque2(self, p):
        print("entra bloque2")
        return p

    @_('asignacion', 'llamada', 'retorno', 'lectura', 'escritura', 'condicion', 'ciclow', 'ciclof', 'funcEspecial')
    def estatuto(self, p):
        print("entra estatuto")
        return p

    @_('ID varibale2')
    def variable(self, p):
        print("entra variable")
        return p

    @_('"[" expresion "]"', '')
    def varibale2(self, p):
        print("entra variable2")
        return p

    @_('asignacion2 asignacion3 expresion ";"')
    def asignacion(self, p):
        print("entra asignacion")
        if len(self.poper) > 0:
            top = self.poper[len(self.poper)-1]
            print("top: ", top)
            # codes: 11 -> =
            if top == 11:
                print("yep=")
                right = self.pilaO.pop()
                t_right = self.pTypes.pop()
                res = self.pilaO.pop()
                t_res = self.pTypes.pop()
                op = self.poper.pop()
                t_asign = self.semantics(t_res, t_right, op)
                print(t_asign)
                print("op: ", op)
                print("res: ", t_res)
                print("right: ", t_right)
                print("asign: ", t_asign)
                if t_asign != -1:
                    self.generateQuad(op, right, None, res)
                    print(self.quadruples)
                    self.pilaO.append(res)
                    self.pTypes.append(t_res)
                else:
                    raise TypeError("type mismatch")
        return p

    @_('variable')
    def asignacion2(self, p):
        print("entra asignacion2")
        tempType = varTable.searchVar(p.variable[1], self.currFuncName)
        self.pilaO.append(p.variable[1])
        self.pTypes.append(tempType)
        return p

    @_('ASSIGN')
    def asignacion3(self, p):
        print("entra asignacion3")
        # codes: 11 -> =
        self.poper.append(11)
        return p

    @_('llamada2 llamada3 llamada4 llamada7 ";"')
    def llamada(self, p):
        print("entra llamada")
        return p

    @_('ID')
    def llamada2(self, p):
        print("entra llamada2")
        return p

    @_('"("')
    def llamada3(self, p):
        print("entra llamada3")
        return p

    @_('expresion llamada5')
    def llamada4(self, p):
        print("entra llamada4")
        return p

    @_('llamada6 llamada4', '')
    def llamada5(self, p):
        print("entra llamada5")
        return p

    @_('","')
    def llamada6(self, p):
        print("entra llamada6")
        return p

    @_('")"')
    def llamada7(self, p):
        print("entra llamada7")
        return p

    @_('RETURN "(" expresion ")" ";"')
    def retorno(self, p):
        print("entra retorno")
        res = self.pilaO.pop()
        # self.pTypes.pop()
        # print(self.pTypes)
        self.generateQuad(100, None, None, res)
        return p

    @_('READ "(" variable ")" ";"')
    def lectura(self, p):
        print("entra lectura")
        tempType = varTable.searchVar(p.variable[1], self.scopeFunc)
        self.generateQuad(101, None, None, p.variable[1])
        return p

    @_('WRITE "(" escritura2 ")" ";"')
    def escritura(self, p):
        print("entra escritura")
        return p

    @_('expresion', 'CTESTRING')
    def escritura2(self, p):
        print("entra escritura2")
        if p[0] == 'CTESTRING':
            self.generateQuad(102, None, None, p[0])
        else:
            res = self.pilaO.pop()
            # self.pTypes.pop()
            # print(self.pTypes)
            self.generateQuad(102, None, None, res)
        return p

    @_('IF condicion2 THEN bloque condicion3')
    def condicion(self, p):
        print("entra condicion")
        end = self.pJumps.pop()
        # codes: 33 -> fill
        self.generateQuad(33, end, self.quadCount + 1, None)
        return p

    @_('"(" expresion ")"')
    def condicion2(self, p):
        print("entra condicion2")
        t_exp = self.pTypes.pop()
        if t_exp != 1:
            raise TypeError("type mismatch")
        else:
            res = self.pilaO.pop()
            # codes: 31 -> gotoF
            self.generateQuad(31, res, None, None)
            self.pJumps.append(self.quadCount - 1)
            print(self.pJumps)
        return p

    @_('condicion4 bloque', '')
    def condicion3(self, p):
        print("entra condicion3")
        return p

    @_('ELSE')
    def condicion4(self, p):
        print("entra condicion4")
        # codes: 30 -> goto
        self.generateQuad(30, None, None, None)
        false_stm = self.pJumps.pop()
        self.pJumps.append(self.quadCount - 1)
        # codes: 33 -> fill
        self.generateQuad(33, false_stm, self.quadCount + 1, None)
        return p

    @_('ciclow2 ciclow3 DO bloque')
    def ciclow(self, p):
        print("entra ciclow")
        end = self.pJumps.pop()
        ret = self.pJumps.pop()
        # codes: 30 -> goto
        self.generateQuad(30, ret, None, None)
        # codes: 33 -> fill
        self.generateQuad(33, end, self.quadCount + 1, None)
        return p

    @_('WHILE')
    def ciclow2(self, p):
        print("entra ciclow2")
        self.pJumps.append(self.quadCount)
        print(self.quadCount)
        return p

    @_('"(" expresion ")"')
    def ciclow3(self, p):
        print("entra ciclow3")
        t_exp = self.pTypes.pop()
        if t_exp != 1:
            raise TypeError("type mismatch")
        else:
            res = self.pilaO.pop()
            # codes: 31 -> gotoF
            self.generateQuad(31, res, None, None)
            self.pJumps.append(self.quadCount - 1)
        return p

    @_('FROM ciclof2 ASSIGN ciclof3 ciclof4 bloque')
    def ciclof(self, p):
        print("entra ciclof")
        self.generateQuad(1, "vControl", 1, "una direccionY")
        end = self.pJumps.pop()
        ret = self.pJumps.pop()
        self.generateQuad(30, ret, None, None)
        self.generateQuad(33, end, self.quadCount + 1, None)
        return p

    @_('variable')
    def ciclof2(self, p):
        print("entra ciclof2")
        tempType = varTable.searchVar(p.variable[1], self.currFuncName)
        if tempType == 1:
            self.pilaO.append(p.variable[1])
            self.pTypes.append(tempType)
        else:
            raise TypeError("Type mismatch")
        return p

    @_('expresion TO')
    def ciclof3(self, p):
        print("entra ciclof3")
        t_exp = self.pTypes.pop()
        if t_exp != 1:
            raise TypeError("Type mismatch")
        else:
            exp = self.pilaO.pop()
            vControl = self.pilaO.pop()
            t_vControl = self.pTypes.pop()
            t_res = self.semantics(t_vControl, t_exp, 11)
            if t_res == -1:
                raise TypeError("Type mismatch")
            else:
                self.generateQuad(11, exp, None, vControl)
        return p

    @_('expresion DO')
    def ciclof4(self, p):
        print("entra ciclof4")
        t_exp = self.pTypes.pop()
        if t_exp != 1:
            raise TypeError("Type mismatch")
        else:
            exp = self.pilaO.pop()
            self.generateQuad(11, exp, None, "vFinal")
            self.generateQuad(8, "vControl", "vFinal", "una direccionX")
            self.pJumps.append(self.quadCount - 1)
            self.generateQuad(31, "una direccionX", None, None)
            self.pJumps.append(self.quadCount - 1)
        return p

    @_('punto', 'linea', 'circulo', 'arco', 'penup', 'pendown', 'color', 'grosor', 'limpiar')
    def funcEspecial(self, p):
        print("entra funcEspecial")
        return p

    @_('POINT "(" expresion "," expresion ")" ";"')
    def punto(self, p):
        print("entra punto")
        res2 = self.pilaO.pop()
        t_res2 = self.pTypes.pop()
        res1 = self.pilaO.pop()
        t_res1 = self.pTypes.pop()

        if (t_res2 == 1 or t_res2 == 2) and (t_res1 == 1 or t_res1 == 2):
            self.generateQuad(103, res1, res2, None)
        else:
            raise TypeError("Type mismatch")
        return p

    @_('CIRCLE "(" expresion ")" ";"')
    def circulo(self, p):
        print("entra circulo")
        res = self.pilaO.pop()
        t_res = self.pTypes.pop()
        if t_res == 1 or t_res == 2:
            self.generateQuad(104, res, None, None)
        else:
            raise TypeError("Type mismatch")
        return p

    @_('LINE "(" expresion "," linea2 ")" ";"')
    def linea(self, p):
        print("entra linea")
        print(p.linea2[1])
        res = self.pilaO.pop()
        t_res = self.pTypes.pop()
        if t_res == 1 or t_res == 2:
            self.generateQuad(105, res, p.linea2[1], None)
        else:
            raise TypeError("Type mismatch")
        return p

    @_('VERTICAL', 'HORIZONTAL')
    def linea2(self, p):
        print("entra linea2")
        return p

    @_('ARC "(" expresion "," expresion ")" ";"')
    def arco(self, p):
        print("entra arco")
        res2 = self.pilaO.pop()
        t_res2 = self.pTypes.pop()
        res1 = self.pilaO.pop()
        t_res1 = self.pTypes.pop()

        if (t_res2 == 1 or t_res2 == 2) and (t_res1 == 1 or t_res1 == 2):
            self.generateQuad(106, res1, res2, None)
        else:
            raise TypeError("Type mismatch")
        return p

    @_('PENUP "(" ")" ";"')
    def penup(self, p):
        print("entra penup")
        self.generateQuad(107, None, None, None)
        return p

    @_('PENDOWN "(" ")" ";"')
    def pendown(self, p):
        print("entra pendown")
        self.generateQuad(108, None, None, None)
        return p

    @_('COLOR "(" expresion "," expresion "," expresion ")" ";"')
    def color(self, p):
        print("entra color")
        res3 = self.pilaO.pop()
        t_res3 = self.pTypes.pop()
        res2 = self.pilaO.pop()
        t_res2 = self.pTypes.pop()
        res1 = self.pilaO.pop()
        t_res1 = self.pTypes.pop()

        if (t_res2 == 1 or t_res2 == 2) and (t_res1 == 1 or t_res1 == 2) and (t_res3 == 1 or t_res3 == 2):
            self.generateQuad(109, res1, res2, res3)
        else:
            raise TypeError("Type mismatch")
        return p

    @_('WIDTH "(" expresion ")" ";"')
    def grosor(self, p):
        print("entra grosor")
        res = self.pilaO.pop()
        t_res = self.pTypes.pop()
        if t_res == 1 or t_res == 2:
            self.generateQuad(110, res, None, None)
        else:
            raise TypeError("Type mismatch")
        return p

    @_('CLEAR "(" ")" ";"')
    def limpiar(self, p):
        print("entra limpiar")
        self.generateQuad(111, None, None, None)
        return p

    @_('expresion2 expresion3')
    def expresion(self, p):
        print("entra expresion")
        return p

    @_('exp')
    def expresion2(self, p):
        print("entra expresion2")
        if len(self.poper) > 0:
            top = self.poper[len(self.poper)-1]
            print("top: ", top)
            # codes: 10 -> |
            if top == 10:
                print("yep|")
                right = self.pilaO.pop()
                t_right = self.pTypes.pop()
                left = self.pilaO.pop()
                t_left = self.pTypes.pop()
                op = self.poper.pop()
                t_res = self.semantics(t_left, t_right, op)
                print(t_res)
                if t_res != -1:
                    res = "una direccion"
                    self.generateQuad(op, left, right, res)
                    print(self.quadruples)
                    self.pilaO.append(res)
                    self.pTypes.append(t_res)
                else:
                    raise TypeError("type mismatch")
        return p

    @_('expresion4 expresion', '')
    def expresion3(self, p):
        print("entra expresion3")
        return p

    @_('OR')
    def expresion4(self, p):
        print("entra expresion4")
        # codes: 10 -> |
        if p[0] == '|':
            print("added |")
            self.poper.append(10)
        return p

    @_('exp2 exp3')
    def exp(self, p):
        print("entra exp")
        return p

    @_('expA')
    def exp2(self, p):
        print("entra exp2")
        if len(self.poper) > 0:
            top = self.poper[len(self.poper)-1]
            print("top: ", top)
            # codes: 9 -> &
            if top == 9:
                print("yep&")
                right = self.pilaO.pop()
                t_right = self.pTypes.pop()
                left = self.pilaO.pop()
                t_left = self.pTypes.pop()
                op = self.poper.pop()
                t_res = self.semantics(t_left, t_right, op)
                print(t_res)
                if t_res != -1:
                    res = "una direccion"
                    self.generateQuad(op, left, right, res)
                    print(self.quadruples)
                    self.pilaO.append(res)
                    self.pTypes.append(t_res)
                else:
                    raise TypeError("type mismatch")
        return p

    @_('exp4 exp', '')
    def exp3(self, p):
        print("entra exp3")
        return p

    @_('AND')
    def exp4(self, p):
        print("entra exp4")
        # codes: 9 -> &
        if p[0] == '&':
            print("added &")
            self.poper.append(9)
        return p

    @_('expA2 expA3')
    def expA(self, p):
        print("entra expA")
        return p

    @_('expB')
    def expA2(self, p):
        print("entra expA2")
        if len(self.poper) > 0:
            top = self.poper[len(self.poper)-1]
            print("top: ", top)
            # codes: 5 -> == , 6 -> !=, 7 -> >, 8 -> <
            if top == 5 or top == 6 or top == 7 or top == 8:
                print("yep<>==!=")
                right = self.pilaO.pop()
                t_right = self.pTypes.pop()
                left = self.pilaO.pop()
                t_left = self.pTypes.pop()
                op = self.poper.pop()
                t_res = self.semantics(t_left, t_right, op)
                print(t_res)
                if t_res != -1:
                    res = "una direccion"
                    self.generateQuad(op, left, right, res)
                    print(self.quadruples)
                    self.pilaO.append(res)
                    self.pTypes.append(t_res)
                else:
                    raise TypeError("type mismatch")
        return p

    @_('expA4 expA', '')
    def expA3(self, p):
        print("entra expA3")
        return p

    @_('LT', 'GT', 'EQ', 'NEQ')
    def expA4(self, p):
        print("entra expA4")
        # codes: 5 -> == , 6 -> !=, 7 -> >, 8 -> <
        if p[0] == '>':
            print("added >")
            self.poper.append(7)
        elif p[0] == '<':
            print("added <")
            self.poper.append(8)
        elif p[0] == '==':
            print("added ==")
            self.poper.append(5)
        elif p[0] == '!=':
            print("added !=")
            self.poper.append(6)
        return p

    @_('expB2 expB3')
    def expB(self, p):
        print("entra expB")
        return p

    @_('termino')
    def expB2(self, p):
        print("entra expB2")
        if len(self.poper) > 0:
            top = self.poper[len(self.poper)-1]
            print("top: ", top)
            # codes: 1 -> +, 2 -> -
            if top == 1 or top == 2:
                print("yep+-")
                right = self.pilaO.pop()
                t_right = self.pTypes.pop()
                left = self.pilaO.pop()
                t_left = self.pTypes.pop()
                op = self.poper.pop()
                t_res = self.semantics(t_left, t_right, op)
                print(t_res)
                if t_res != -1:
                    res = "una direccion"
                    self.generateQuad(op, left, right, res)
                    print(self.quadruples)
                    self.pilaO.append(res)
                    self.pTypes.append(t_res)
                else:
                    raise TypeError("type mismatch")
        return p

    @_('expB4 expB', '')
    def expB3(self, p):
        print("entra expB3")
        return p

    @_('PLUS', 'MINUS')
    def expB4(self, p):
        print("entra expB4")
        # codes: 1 -> +, 2 -> -
        if p[0] == '+':
            print("added +")
            self.poper.append(1)
        elif p[0] == '-':
            print("added -")
            self.poper.append(2)
        return p

    @_('termino2 termino3')
    def termino(self, p):
        print("entra termino")
        return p

    @_('factor')
    def termino2(self, p):
        print("entra termino2")
        print("poper: ", self.poper)
        if len(self.poper) > 0:
            top = self.poper[len(self.poper)-1]
            print("top: ", top)
            # codes: 3 -> *, 4 -> /
            if top == 3 or top == 4:
                print("yep")
                right = self.pilaO.pop()
                t_right = self.pTypes.pop()
                left = self.pilaO.pop()
                t_left = self.pTypes.pop()
                op = self.poper.pop()
                t_res = self.semantics(t_left, t_right, op)
                print(t_res)
                if t_res != -1:
                    res = "una direccion"
                    self.generateQuad(op, left, right, res)
                    print(self.quadruples)
                    self.pilaO.append(res)
                    self.pTypes.append(t_res)
                else:
                    raise TypeError("type mismatch")
        else:
            print("poper vacio")
            
        return p

    @_('termino4 termino', '')
    def termino3(self, p):
        print("entra termino3")
        return p

    @_('MULTIPLY', 'DIVIDE')
    def termino4(self, p):
        print("entra termino4")
        # codes: 3 -> *, 4 -> /
        if p[0] == '*':
            print("added *")
            self.poper.append(3)
        elif p[0] == '/':
            print("added /")
            self.poper.append(4)
        return p

    @_('factor2', 'factor7', 'factor8', 'factor9', 'factor10')
    def factor(self, p):
        print("entra factor")
        return p

    @_('factor3 factor4')
    def factor2(self, p):
        print("entra factor2")
        return p

    @_('"("')
    def factor3(self, p):
        print("entra factor3")
        self.poper.append("(")
        return p

    @_('factor5 factor6')
    def factor4(self, p):
        print("entra factor4")
        return p

    @_('expresion')
    def factor5(self, p):
        print("entra factor5")
        return p

    @_('")"')
    def factor6(self, p):
        print("entra factor6")
        self.poper.pop()
        return p

    @_('CTEI')
    def factor7(self, p):
        print("entra factor7")
        self.pilaO.append(p.CTEI)
        self.pTypes.append(1)
        return p

    @_('CTEF')
    def factor8(self, p):
        print("entra factor8")
        self.pilaO.append(p.CTEF)
        self.pTypes.append(2)
        return p

    @_('variable')
    def factor9(self, p):
        print("entra factor9")
        tempType = varTable.searchVar(p.variable[1], self.currFuncName)
        self.pilaO.append(p.variable[1])
        self.pTypes.append(tempType)
        return p

    @_('llamada')
    def factor10(self, p):
        print("entra factor10")
        return p

# main
if __name__ == '__main__':
    file = open("pruebaEsp.txt", 'r')

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