from sly import Parser
from theOnlyLonelyLexer import TheOnlyLonelyLexer
from collections import deque
from funcAndVarTable import FuncTable
from funcAndVarTable import VarTable
from constantTable import ConstantTable

class TheOnlyLonelyParser(Parser):
    tokens = TheOnlyLonelyLexer.tokens
    programName = ''
    funcTypeTemp = 0
    paramTypeTemp = 0
    quadCount = 1
    currFuncName = ''
    tempFuncCall = ''
    contParami = 0
    contParamf = 0
    contVari = 0
    contVarf = 0
    contTempi = 0
    contTempf = 0
    paramPointer = 0
    vControl = 0
    vFinal = 0
    paramTypes = []
    quadruples = {}
    idStack = deque()
    sizeStack = deque()
    poper = deque()
    pilaO = deque()
    pTypes = deque()
    pJumps = deque()
    funcNames = deque()

    # contadores para direcciones
    # GLOBALES
        # intG:      1,000 - 1,999
        # tempiG:    2,000 - 2,999
        # floatG:    3,000 - 3,999
        # tempfG:    4,000 - 4,999
    
    intG = 1000
    tempiG = 2000
    floatG = 3000
    tempfG = 4000

    # LOCALES
        # intL:     5,000 - 5,999
        # tempiL:   6,000 - 6,999
        # floatL:   7,000 - 7,999
        # tempfL:   8,000 - 8,999
    
    intL = 5000
    tempiL = 6000
    floatL = 7000
    tempfL = 8000

    # CONSTANTES
        # intC:         9,000 - 9,999
        # floatC:       10,000 - 10,999
        # stringC:      11,000 - 11,999

    intC = 9000
    floatC = 10000
    stringC = 11000    

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

    # get type by memory address
    def getType (self, dir):
        if dir >= 7000 and dir < 9000:
            return 2
        elif dir >= 5000:
            return 1
        elif dir >= 3000:
            return 2
        elif dir >= 1000:
            return 1
        else:
            raise TypeError("Type does not exists for address")

    def fillQuadruple (self, toFill, fillWith):
        if toFill in self.quadruples:
            self.quadruples[toFill]["res"] = fillWith
        else:
            raise KeyError("No quadruple found")


    # Grammar rules

    @_('programa5 programa4 ";" programa2 programa3 principal')
    def programa(self, p):
        print("entra programa")
        fTable = functTable.getTable()
        print(fTable)
        print("\n")
        cTable = constantTable.getTable()
        print(cTable)
        print("\n")
        print(self.quadruples)
        pass

    @_('PROGRAM')
    def programa5(self, p):
        print("entra programa5")
        # codes 30 -> goto
        # goto Principal
        self.pJumps.append(self.quadCount)
        self.generateQuad(30, None, None, None)

    @_('ID')
    def programa4(self, p):
        print("entra programa4")
        functTable.addFunc(p.ID, 3)
        self.programName = p.ID
        self.currFuncName = p.ID
        return p

    @_('vars', '')
    def programa2(self, p):
        print("entra programa2")
        return p

    @_('func', '')
    def programa3(self, p):
        print("entra programa3")
        return p

    @_('func2 FUNCTION func5 "(" parametro ")" ";" func3 func6 func4')
    def func(self, p):
        print("entra func")
        return p

    @_('ID')
    def func5(self, p):
        print("entra func5")
        # add variable to keep result of a function with return
        if self.funcTypeTemp == 1 or self.funcTypeTemp == 2:
            name = p.ID + "Value"
            varTable.addFuncNameAsVar(name, self.funcTypeTemp, 0, self.intG, self.programName)
            self.intG = self.intG + 1
        
        functTable.addFunc(p.ID,self.funcTypeTemp)
        self.funcNames.append(self.currFuncName)
        self.currFuncName = p.ID
        self.contParami = 0
        self.contParamf = 0
        self.contVari = 0
        self.contVarf = 0
        self.contTempi = 0
        self.contTempf = 0

    @_('bloque')
    def func6(self, p):
        print("entra func6")
        functTable.delVarT(self.currFuncName)
        # codes: 36 -> EndFunc
        self.generateQuad(36, None, None, None)
        functTable.setFuncSize(self.currFuncName, self.contParami, self.contParamf, self.contVari, self.contVarf, self.contTempi, self.contTempf)
        self.currFuncName = self.funcNames.pop()
        return p


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
        return p

    @_('vars', '')
    def func3(self, p):
        print("entra func3")
        # meter direccion inicial de la funcion
        functTable.setDir(self.currFuncName, self.quadCount)
        return p

    @_('func', '')
    def func4(self, p):
        print("entra func4")
        return p

    @_('VARIABLES vars2')
    def vars(self, p):
        print("entra vars")
        return p

    @_('vars3 ":" vars5 ";" vars6')
    def vars2(self, p):
        print("entra vars2")
        return p

    @_('ID "[" CTEI "]" vars4', 'ID vars4')
    def vars3(self, p):
        print("entra vars3")
        if len(p) == 2:
            self.idStack.append(p.ID)
            self.sizeStack.append(0)
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
        if p.tiposimple[1] == 'int':
            for x in range(len(self.idStack)):
                # varTable.addVar(self.idStack.pop(), 1, self.sizeStack.pop())
                if len(self.funcNames) > 0:
                    varTable.addVar(self.idStack.pop(), 1, self.sizeStack.pop(), self.intL)
                    self.intL = self.intL + 1
                    self.contVari = self.contVari + 1
                else:
                    varTable.addVar(self.idStack.pop(), 1, self.sizeStack.pop(), self.intG)
                    self.intG = self.intG + 1
                    self.contVari = self.contVari + 1        
        elif p.tiposimple[1] == 'float':
            for x in range(len(self.idStack)):
                if len(self.funcNames) > 0:
                    varTable.addVar(self.idStack.pop(), 2, self.sizeStack.pop(), self.floatL)
                    self.floatL = self.floatL + 1
                    self.contVarf = self.contVarf + 1
                else:
                    varTable.addVar(self.idStack.pop(), 2, self.sizeStack.pop(), self.floatG)
                    self.floatG = self.floatG + 1
                    self.contVarf = self.contVarf + 1
        return p

    @_('vars2', '')
    def vars6(self, p):
        print("entra vars6")
        return p

    @_('principal2 "(" ")" bloque')
    def principal(self, p):
        print("entra principal")
        # codes: 37 -> End
        self.generateQuad(37, None, None, None)
        return p

    @_('PRINCIPAL')
    def principal2(self, p):
        print("entra principal2")
        first = self.pJumps.pop()
        self.fillQuadruple(first, self.quadCount)
        return p

    @_('parametro2 parametro3 parametro4', '')
    def parametro(self, p):
        print("entra parametro")
        return p

    @_('tiposimple')
    def parametro2(self, p):
        print("entra parametro2")
        if p.tiposimple[1] == 'int':
            self.paramTypeTemp = 1
        elif p.tiposimple[1] == 'float':
            self.paramTypeTemp = 2
        return p

    @_('ID')
    def parametro3(self, p):
        print("entra parametro3")
        if self.paramTypeTemp == 1:
            varTable.addVar(p.ID, self.paramTypeTemp, 0, self.intL)
            functTable.setParam(self.currFuncName, [self.paramTypeTemp])
            self.intL = self.intL + 1
            self.contParami = self.contParami + 1
        else:
            varTable.addVar(p.ID, self.paramTypeTemp, 0, self.floatL)
            functTable.setParam(self.currFuncName, [self.paramTypeTemp])
            self.floatL = self.floatL + 1
            self.contParamf = self.contParamf + 1
        return p

    @_('"," parametro', '')
    def parametro4(self, p):
        print("entra parametro4")
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
            # codes: 11 -> =
            if top == 11:
                right = self.pilaO.pop()
                t_right = self.pTypes.pop()
                res = self.pilaO.pop()
                t_res = self.pTypes.pop()
                op = self.poper.pop()
                t_asign = self.semantics(t_res, t_right, op)
                if t_asign != -1:
                    self.generateQuad(op, right, None, res)
                else:
                    raise TypeError("type mismatch")
        else:
            raise ValueError("No more operands to use")
        return p

    @_('variable')
    def asignacion2(self, p):
        print("entra asignacion2")
        isVar = varTable.searchVar(p.variable[1], self.currFuncName, self.programName)
        if isVar == 1:
            address = varTable.getDir(p.variable[1], self.currFuncName, self.programName)
            t_address = self.getType(address)
            self.pilaO.append(address)
            self.pTypes.append(t_address)
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
        # codes: 35 -> goSub
        self.generateQuad(35, None, None, self.tempFuncCall)
        return p

    @_('ID')
    def llamada2(self, p):
        print("entra llamada2")
        isFunc = functTable.searchFunc(p.ID)
        if isFunc == 1:
            self.paramTypes = functTable.getParam(p.ID)
            self.tempFuncCall = p.ID
        return p

    @_('"("')
    def llamada3(self, p):
        print("entra llamada3")
        # codes: 33 -> ERA
        self.generateQuad(33, None, None, self.tempFuncCall)
        self.paramPointer = 0
        return p

    @_('llamada8 llamada5', '')
    def llamada4(self, p):
        print("entra llamada4")
        return p

    @_('expresion')
    def llamada8(self, p):
        print("entra llamada8")
        argument = self.pilaO.pop()
        t_argument = self.pTypes.pop()
        t_params = self.paramTypes[self.paramPointer]
        if t_params == t_argument:
            # codes: 34 -> Param
            # paramPointer + 1 porque el indice inicial es 0 y el tamaño cuenta desde 1
            self.generateQuad(34, argument, None, self.paramPointer + 1)
        else:
            raise TypeError("Type mismatch")
        return p

    @_('llamada6 llamada4', '')
    def llamada5(self, p):
        print("entra llamada5")
        return p

    @_('","')
    def llamada6(self, p):
        print("entra llamada6")
        self.paramPointer = self.paramPointer + 1
        return p

    @_('")"')
    def llamada7(self, p):
        print("entra llamada7")
        if len(self.paramTypes) > 0:
            if self.paramPointer + 1 != len(self.paramTypes):
                raise IndexError("Number of parameters mismatch")
        return p

    @_('RETURN "(" expresion ")" ";"')
    def retorno(self, p):
        print("entra retorno")
        tempFuncType = functTable.getType(self.currFuncName)
        if (tempFuncType != 3):
            res = self.pilaO.pop()
            t_res = self.pTypes.pop()
            if (tempFuncType == 1):
                if (tempFuncType == t_res):
                    self.generateQuad(100, None, None, res)
                else:
                    raise TypeError("Type mismatch")
            else:
                self.generateQuad(100, None, None, res)
        else:
            raise TypeError("Void function does not use return")
            
        return p

    @_('READ "(" variable ")" ";"')
    def lectura(self, p):
        print("entra lectura")
        isVar = varTable.searchVar(p.variable[1], self.currFuncName, self.programName)
        if isVar == 1:
            address = varTable.getDir(p.variable[1], self.currFuncName, self.programName)
            self.generateQuad(101, None, None, address)
        return p

    @_('WRITE "(" escritura2 ")" ";"')
    def escritura(self, p):
        print("entra escritura")
        return p

    @_('expresion', 'CTESTRING')
    def escritura2(self, p):
        print("entra escritura2")
        if type(p[0]) == str:
            isConstant = constantTable.searchConstant(p[0])
            if isConstant == 0:
                constantTable.addConstant(p[0], self.stringC)
                self.generateQuad(102, None, None, self.stringC)
                self.stringC = self.stringC + 1
            elif isConstant == 1:
                dirC = constantTable.getDir(p[0])
                self.generateQuad(102, None, None, dirC)
        else:
            res = self.pilaO.pop()
            self.pTypes.pop()
            self.generateQuad(102, None, None, res)
        return p

    @_('IF condicion2 THEN bloque condicion3')
    def condicion(self, p):
        print("entra condicion")
        end = self.pJumps.pop()
        self.fillQuadruple(end, self.quadCount)
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
        self.fillQuadruple(false_stm, self.quadCount)
        return p

    @_('ciclow2 ciclow3 DO bloque')
    def ciclow(self, p):
        print("entra ciclow")
        end = self.pJumps.pop()
        ret = self.pJumps.pop()
        # codes: 30 -> goto
        self.generateQuad(30, ret, None, None)
        self.fillQuadruple(end, self.quadCount)
        return p

    @_('WHILE')
    def ciclow2(self, p):
        print("entra ciclow2")
        self.pJumps.append(self.quadCount)
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
        # codes: 1 -> +
        if len(self.funcNames) > 0:
            # Local
            self.generateQuad(1, self.vControl, 1, self.tempiL)
            self.tempiL = self.tempiL + 1
        else: # Global
            self.generateQuad(1, self.vControl, 1, self.tempiG)
            self.tempiG = self.tempiG + 1

        end = self.pJumps.pop()
        ret = self.pJumps.pop()
        # codes: 30 -> goto
        self.generateQuad(30,None, None, ret)
        self.fillQuadruple(end, self.quadCount)
        return p

    @_('variable')
    def ciclof2(self, p):
        print("entra ciclof2")
        isVar = varTable.searchVar(p.variable[1], self.currFuncName, self.programName)
        if isVar == 1:
            address = varTable.getDir(p.variable[1], self.currFuncName, self.programName)
            t_address = self.getType(address)
            if t_address != 1:
                raise TypeError("Type mismatch")
            else:
                self.pilaO.append(address)
                self.pTypes.append(t_address)
        else:
            raise NameError("Variable does not exists")
        return p

    @_('expresion TO')
    def ciclof3(self, p):
        print("entra ciclof3")
        t_exp = self.pTypes.pop()
        if t_exp != 1:
            raise TypeError("Type mismatch")
        else:
            exp = self.pilaO.pop()
            self.vControl = self.pilaO.pop()
            t_vControl = self.pTypes.pop()
            t_res = self.semantics(t_vControl, t_exp, 11)
            if t_res == -1:
                raise TypeError("Type mismatch")
            else:
                self.generateQuad(11, exp, None, self.vControl)
        return p

    @_('expresion DO')
    def ciclof4(self, p):
        print("entra ciclof4")
        t_exp = self.pTypes.pop()
        if t_exp != 1:
            raise TypeError("Type mismatch")
        else:
            self.vFinal = self.pilaO.pop()
            # codes 8 -> <
            if len(self.funcNames) > 0:
                self.generateQuad(8, self.vControl, self.vFinal, self.tempiL)
                self.pJumps.append(self.quadCount - 1)
                # codes 31 -> gotoF
                self.generateQuad(31, self.tempiL, None, None)
                self.pJumps.append(self.quadCount - 1)
                self.tempiL = self.tempiL + 1
            else: # Global
                self.generateQuad(8, self.vControl, self.vFinal, self.tempiG)
                self.pJumps.append(self.quadCount - 1)
                # codes 31 -> gotoF
                self.generateQuad(31, self.tempiG, None, None)
                self.pJumps.append(self.quadCount - 1)
                self.tempiG = self.tempiG + 1
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
            # codes: 10 -> |
            if top == 10:
                right = self.pilaO.pop()
                t_right = self.pTypes.pop()
                left = self.pilaO.pop()
                t_left = self.pTypes.pop()
                op = self.poper.pop()
                t_res = self.semantics(t_left, t_right, op)
                if t_res != -1:
                    #agregar temporal int
                    if len(self.funcNames) > 0:
                        res = self.tempiL
                        self.tempiL = self.tempiL + 1
                        self.contTempi = self.contTempi + 1
                    else:
                        res = self.tempiG
                        self.tempiG = self.tempiG + 1
                    
                    self.generateQuad(op, left, right, res)
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
            # codes: 9 -> &
            if top == 9:
                right = self.pilaO.pop()
                t_right = self.pTypes.pop()
                left = self.pilaO.pop()
                t_left = self.pTypes.pop()
                op = self.poper.pop()
                t_res = self.semantics(t_left, t_right, op)
                if t_res != -1:
                    #agregar temporal int
                    if len(self.funcNames) > 0:
                        res = self.tempiL
                        self.tempiL = self.tempiL + 1
                        self.contTempi = self.contTempi + 1
                    else:
                        res = self.tempiG
                        self.tempiG = self.tempiG + 1
    
                    self.generateQuad(op, left, right, res)
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
            # codes: 5 -> == , 6 -> !=, 7 -> >, 8 -> <
            if top == 5 or top == 6 or top == 7 or top == 8:
                right = self.pilaO.pop()
                t_right = self.pTypes.pop()
                left = self.pilaO.pop()
                t_left = self.pTypes.pop()
                op = self.poper.pop()
                t_res = self.semantics(t_left, t_right, op)
                if t_res != -1:
                    #agregar temporal int
                    if len(self.funcNames) > 0:
                        res = self.tempiL
                        self.tempiL = self.tempiL + 1
                        self.contTempi = self.contTempi + 1
                    else:
                        res = self.tempiG
                        self.tempiG = self.tempiG + 1

                    self.generateQuad(op, left, right, res)
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
            self.poper.append(7)
        elif p[0] == '<':
            self.poper.append(8)
        elif p[0] == '==':
            self.poper.append(5)
        elif p[0] == '!=':
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
            # codes: 1 -> +, 2 -> -
            if top == 1 or top == 2:
                right = self.pilaO.pop()
                t_right = self.pTypes.pop()
                left = self.pilaO.pop()
                t_left = self.pTypes.pop()
                op = self.poper.pop()
                t_res = self.semantics(t_left, t_right, op)
                if t_res != -1:
                    if t_res == 1:
                        #agregar temporal int
                        if len(self.funcNames) > 0:
                            res = self.tempiL
                            self.tempiL = self.tempiL + 1
                            self.contTempi = self.contTempi + 1
                        else:
                            res = self.tempiG
                            self.tempiG = self.tempiG + 1
                    else:
                        # agregar temporal float
                        if len(self.funcNames) > 0:
                            res = self.tempfL
                            self.tempfL = self.tempfL + 1
                            self.contTempf = self.contTempf + 1 
                        else:
                            res = self.tempfG
                            self.tempfG = self.tempfG + 1
                    
                    self.generateQuad(op, left, right, res)
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
            self.poper.append(1)
        elif p[0] == '-':
            self.poper.append(2)
        return p

    @_('termino2 termino3')
    def termino(self, p):
        print("entra termino")
        return p

    @_('factor')
    def termino2(self, p):
        print("entra termino2")
        if len(self.poper) > 0:
            top = self.poper[len(self.poper)-1]
            # codes: 3 -> *, 4 -> /
            if top == 3 or top == 4:
                right = self.pilaO.pop()
                t_right = self.pTypes.pop()
                left = self.pilaO.pop()
                t_left = self.pTypes.pop()
                op = self.poper.pop()
                t_res = self.semantics(t_left, t_right, op)
                if t_res != -1:
                    if t_res == 1:
                        #agregar temporal int
                        if len(self.funcNames) > 0:
                            res = self.tempiL
                            self.tempiL = self.tempiL + 1
                            self.contTempi = self.contTempi + 1
                        else:
                            res = self.tempiG
                            self.tempiG = self.tempiG + 1
                    else:
                        # agregar temporal float
                        if len(self.funcNames) > 0:
                            res = self.tempfL
                            self.tempfL = self.tempfL + 1
                            self.contTempf = self.contTempf + 1 
                        else:
                            res = self.tempfG
                            self.tempfG = self.tempfG + 1
                    
                    self.generateQuad(op, left, right, res)
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
            self.poper.append(3)
        elif p[0] == '/':
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
        isCTEI = constantTable.searchConstant(p.CTEI)
        if isCTEI == 0:
            constantTable.addConstant(p.CTEI, self.intC)
            self.pilaO.append(self.intC)
            self.pTypes.append(1)
            self.intC = self.intC + 1
        elif isCTEI == 1:
            dirC = constantTable.getDir(p.CTEI)
            self.pilaO.append(dirC)
            self.pTypes.append(1)
        
        return p

    @_('CTEF')
    def factor8(self, p):
        print("entra factor8")
        isCTEF = constantTable.searchConstant(p.CTEF)
        if isCTEF == 0:
            constantTable.addConstant(p.CTEF, self.floatC)
            self.pilaO.append(self.floatC)
            self.pTypes.append(2)
            self.floatC = self.floatC + 1
        elif isCTEF == 1:
            dirC = constantTable.getDir(p.CTEF)
            self.pilaO.append(dirC)
            self.pTypes.append(2)
        return p

    @_('variable')
    def factor9(self, p):
        print("entra factor9")
        isVar = varTable.searchVar(p.variable[1], self.currFuncName, self.programName)
        if isVar == 1:
            address = varTable.getDir(p.variable[1], self.currFuncName, self.programName)
            t_address = self.getType(address)
            self.pilaO.append(address)
            self.pTypes.append(t_address)
            # if t_address == 1:
            #     self.pTypes.append(1)
            # elif t_address == 2:
            #     self.pTypes.append(2)
            # else:
            #     raise TypeError("Type does not exists")
            
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
    constantTable = ConstantTable()

    result = parser.parse(lexer.tokenize(allLines))
    print(result)

    file.close()