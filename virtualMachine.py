# # import
import turtle
from collections import deque
from typing import Type
from MemoryVM import GlobalMemory
from MemoryVM import LocalMemory
from copy import deepcopy

class VirtualMachine:
    memoryG = GlobalMemory()
    constantTable = {}
    funcTable = {}
    instruction = 1
    prevInstruction = deque()
    isAsleep = False
    prevMemoryL = []
    funcName = ''
    prevFunc = deque()
    # quadruples parts
    op = 0
    right = 0
    left = 0
    res = 0
    trt = turtle.Turtle()

    # Return the program's name, which holds global variables and constants.
    def getProgramsName(self):
        for key, value in self.funcTable.items():
            if "varT" in value:
                return key


    # Iterate through funcTable dictionary by variable to add each variable to memory.
    def setGlobalVariables(self):
        programName = self.getProgramsName()
        varTable = self.funcTable[programName]["varT"]
        for variable in varTable:
            self.memoryG.setGlobalVariables(varTable[variable]["dir"])

    # Iterate through constantTable dictionary by constant to add each constant to memory.
    def setConstantVariables(self):
        for constant in self.constantTable:
            dirC = self.constantTable[constant]
            self.memoryG.setConstants(dirC, constant)

    # Returns the quadruple parts.    
    def breakQuadrupleParts(self, quadruple, instruction):
        op = quadruple[instruction]["op"]
        left = quadruple[instruction]["left"]
        right = quadruple[instruction]["right"]
        res = quadruple[instruction]["res"]

        return op, left, right, res

    # Returns the size parts.
    def breakFunctionSizes(self, name):
        if name in self.funcTable:
            size = self.funcTable[name]["size"]
            parami = size["parami"]
            paramf = size["paramf"]
            vari = size["vari"]
            varf = size["varf"]
            tempi = size["tempi"]
            tempf = size["tempf"]
        else:
            raise NameError("Function name does not exists")

        return parami, paramf, vari, varf, tempi, tempf

    # Returns function address.
    def getFuncDir(self, name):
        if name in self.funcTable:
            return self.funcTable[name]["dir"]

    def getGlobalVariableDir(self, name):
        programName = self.getProgramsName()
        if name in self.funcTable[programName]["varT"]:
            return self.funcTable[programName]["varT"][name]["dir"]
        else:
            raise NameError("Global variable does not exists")

    # Main function of the virtual machine, runs the intermidiate code generated by the parser.
    def startProgram(self, quadruples, funcTable, constantTable):
        print("---------------------------------------------------------------")
        self.funcTable = funcTable
        self.constantTable = constantTable
        self.setGlobalVariables()
        self.setConstantVariables()
        # print(funcTable, '\n')
        # print(constantTable, '\n')
        # print(quadruples, '\n')
        # self.memoryG.show()

        while self.instruction < len(quadruples):
            self.op, self.left, self.right, self.res = self.breakQuadrupleParts(quadruples, self.instruction)

            # arithmetic expressions
            if self.op == 1: # +
                if self.left >= 5000 and self.left < 9000:
                    # local variable
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        leftSide = tempMemoryL.getLocalValue(self.left)
                    else:
                        leftSide = memoryL.getLocalValue(self.left)
                else:
                    leftSide = self.memoryG.getValue(self.left)

                if self.right >= 5000 and self.right < 9000:
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        rightSide = tempMemoryL.getLocalValue(self.right)
                    else:
                        rightSide = memoryL.getLocalValue(self.right)
                    
                else:
                    rightSide = self.memoryG.getValue(self.right)
                    
                result = leftSide + rightSide

                if self.res >= 5000 and self.res < 9000:
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        tempMemoryL.updateLocalMemory(self.res, result)
                    else:
                        memoryL.updateLocalMemory(self.res, result)
                else:
                    self.memoryG.setTempVariables(self.res, result)
            elif self.op == 2: # -
                if self.left >= 5000 and self.left < 9000:
                    # local variable
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        leftSide = tempMemoryL.getLocalValue(self.left)
                    else:
                        leftSide = memoryL.getLocalValue(self.left)
                else:
                    leftSide = self.memoryG.getValue(self.left)

                if self.right >= 5000 and self.right < 9000:
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        rightSide = tempMemoryL.getLocalValue(self.right)
                    else:
                        rightSide = memoryL.getLocalValue(self.right)
                else:
                    rightSide = self.memoryG.getValue(self.right)
                    
                result = leftSide - rightSide

                if self.res >= 5000 and self.res < 9000:
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        tempMemoryL.updateLocalMemory(self.res, result)
                    else:
                        memoryL.updateLocalMemory(self.res, result)
                else:
                    self.memoryG.setTempVariables(self.res, result)
            elif self.op == 3: # *
                if self.left >= 5000 and self.left < 9000:
                    # local variable
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        leftSide = tempMemoryL.getLocalValue(self.left)
                    else:
                        leftSide = memoryL.getLocalValue(self.left)
                else:
                    leftSide = self.memoryG.getValue(self.left)

                if self.right >= 5000 and self.right < 9000:
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        rightSide = tempMemoryL.getLocalValue(self.right)
                    else:
                        rightSide = memoryL.getLocalValue(self.right)
                else:
                    rightSide = self.memoryG.getValue(self.right)
                    
                result = leftSide * rightSide

                if self.res >= 5000 and self.res < 9000:
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        tempMemoryL.updateLocalMemory(self.res, result)
                    else:
                        memoryL.updateLocalMemory(self.res, result)
                else:
                    self.memoryG.setTempVariables(self.res, result)
            elif self.op == 4: # /
                if self.left >= 5000 and self.left < 9000:
                    # local variable
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        leftSide = tempMemoryL.getLocalValue(self.left)
                    else:
                        leftSide = memoryL.getLocalValue(self.left)
                else:
                    leftSide = self.memoryG.getValue(self.left)

                if self.right >= 5000 and self.right < 9000:
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        rightSide = tempMemoryL.getLocalValue(self.right)
                    else:
                        rightSide = memoryL.getLocalValue(self.right)
                else:
                    rightSide = self.memoryG.getValue(self.right)
                    
                result = leftSide / rightSide

                if self.res >= 5000 and self.res < 9000:
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        tempMemoryL.updateLocalMemory(self.res, result)
                    else:
                        memoryL.updateLocalMemory(self.res, result)
                else:
                    self.memoryG.setTempVariables(self.res, result)
            elif self.op == 5: # ==
                if self.left >= 5000 and self.left < 9000:
                    # local variable
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        leftSide = tempMemoryL.getLocalValue(self.left)
                    else:
                        leftSide = memoryL.getLocalValue(self.left)
                else:
                    leftSide = self.memoryG.getValue(self.left)

                if self.right >= 5000 and self.right < 9000:
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        rightSide = tempMemoryL.getLocalValue(self.right)
                    else:
                        rightSide = memoryL.getLocalValue(self.right)
                else:
                    rightSide = self.memoryG.getValue(self.right)
                    
                if leftSide == rightSide:
                    result = 1
                else:
                    result = 0
                
                if self.res >= 5000 and self.res < 9000:
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        tempMemoryL.updateLocalMemory(self.res, result)
                    else:
                        memoryL.updateLocalMemory(self.res, result)
                else:
                    self.memoryG.setTempVariables(self.res, result)
            elif self.op == 6: # !=
                if self.left >= 5000 and self.left < 9000:
                    # local variable
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        leftSide = tempMemoryL.getLocalValue(self.left)
                    else:
                        leftSide = memoryL.getLocalValue(self.left)
                else:
                    leftSide = self.memoryG.getValue(self.left)

                if self.right >= 5000 and self.right < 9000:
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        rightSide = tempMemoryL.getLocalValue(self.right)
                    else:
                        rightSide = memoryL.getLocalValue(self.right)
                else:
                    rightSide = self.memoryG.getValue(self.right)
                    
                if leftSide != rightSide:
                    result = 1
                else:
                    result = 0
                
                if self.res >= 5000 and self.res < 9000:
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        tempMemoryL.updateLocalMemory(self.res, result)
                    else:
                        memoryL.updateLocalMemory(self.res, result)
                else:
                    self.memoryG.setTempVariables(self.res, result)
            elif self.op == 7: # >
                if self.left >= 5000 and self.left < 9000:
                    # local variable
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        leftSide = tempMemoryL.getLocalValue(self.left)
                    else:
                        leftSide = memoryL.getLocalValue(self.left)
                else:
                    leftSide = self.memoryG.getValue(self.left)

                if self.right >= 5000 and self.right < 9000:
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        rightSide = tempMemoryL.getLocalValue(self.right)
                    else:
                        rightSide = memoryL.getLocalValue(self.right)
                else:
                    rightSide = self.memoryG.getValue(self.right)
                    
                if leftSide > rightSide:
                    result = 1
                else:
                    result = 0
                
                if self.res >= 5000 and self.res < 9000:
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        tempMemoryL.updateLocalMemory(self.res, result)
                    else:
                        memoryL.updateLocalMemory(self.res, result)
                else:
                    self.memoryG.setTempVariables(self.res, result)
            elif self.op == 8: # <
                if self.left >= 5000 and self.left < 9000:
                    # local variable
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        leftSide = tempMemoryL.getLocalValue(self.left)
                    else:
                        leftSide = memoryL.getLocalValue(self.left)
                else:
                    leftSide = self.memoryG.getValue(self.left)

                if self.right >= 5000 and self.right < 9000:
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        rightSide = tempMemoryL.getLocalValue(self.right)
                    else:
                        rightSide = memoryL.getLocalValue(self.right)
                else:
                    rightSide = self.memoryG.getValue(self.right)
                    
                if leftSide < rightSide:
                    result = 1
                else:
                    result = 0
                
                if self.res >= 5000 and self.res < 9000:
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        tempMemoryL.updateLocalMemory(self.res, result)
                    else:
                        memoryL.updateLocalMemory(self.res, result)
                else:
                    self.memoryG.setTempVariables(self.res, result)
            elif self.op == 9: # &
                if self.left >= 5000 and self.left < 9000:
                    # local variable
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        leftSide = tempMemoryL.getLocalValue(self.left)
                    else:
                        leftSide = memoryL.getLocalValue(self.left)
                else:
                    leftSide = self.memoryG.getValue(self.left)

                if self.right >= 5000 and self.right < 9000:
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        rightSide = tempMemoryL.getLocalValue(self.right)
                    else:
                        rightSide = memoryL.getLocalValue(self.right)
                else:
                    rightSide = self.memoryG.getValue(self.right)
                
                if leftSide and rightSide:
                    result = 1
                else:
                    result = 0
                
                if self.res >= 5000 and self.res < 9000:
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        tempMemoryL.updateLocalMemory(self.res, result)
                    else:
                        memoryL.updateLocalMemory(self.res, result)
                else:
                    self.memoryG.setTempVariables(self.res, result)
            elif self.op == 10: # |
                if self.left >= 5000 and self.left < 9000:
                    # local variable
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        leftSide = tempMemoryL.getLocalValue(self.left)
                    else:
                        leftSide = memoryL.getLocalValue(self.left)
                else:
                    leftSide = self.memoryG.getValue(self.left)

                if self.right >= 5000 and self.right < 9000:
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        rightSide = tempMemoryL.getLocalValue(self.right)
                    else:
                        rightSide = memoryL.getLocalValue(self.right)
                else:
                    rightSide = self.memoryG.getValue(self.right)

                if leftSide or rightSide:
                    result = 1
                else:
                    result = 0
                
                if self.res >= 5000 and self.res < 9000:
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        tempMemoryL.updateLocalMemory(self.res, result)
                    else:
                        memoryL.updateLocalMemory(self.res, result)
                else:
                    self.memoryG.setTempVariables(self.res, result)
            elif self.op == 11: # =
                if self.left >= 5000 and self.left < 9000:
                    # local variable
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        leftSide = tempMemoryL.getLocalValue(self.left)
                    else:
                        leftSide = memoryL.getLocalValue(self.left)
                else:
                    leftSide = self.memoryG.getValue(self.left)
                
                if self.res >= 5000 and self.res < 9000:
                    if len(self.prevMemoryL) > 1 and not self.isAsleep:
                        tempMemoryL.updateLocalMemory(self.res, result)
                    else:
                        memoryL.updateLocalMemory(self.res, result)
                else:
                    if self.res >= 2000 and self.res < 3000 or self.res >= 4000 and self.res < 5000:
                        self.memoryG.setTempVariables(self.res, leftSide)
                    else:
                        self.memoryG.updateMemory(self.res, leftSide)
            
            # Pre-define functions
            # read and write
            elif self.op == 101:
                result = input()

                if "." in result:
                    result = float(result)
                else:
                    result = int(result)

                if self.res >= 5000 and self.res < 9000:
                    # local variable
                    t_res = memoryL.getType(self.res)
                    if t_res == "int" and type(result) == int:
                        memoryL.updateLocalMemory(self.res, result)
                    elif t_res == "float" and type(result) == float:
                        memoryL.updateLocalMemory(self.res, result)
                    else:
                        raise TypeError("Input and variable type do not match")
                    print("local variable")
                else:
                    t_res = self.memoryG.getType(self.res)
                    if t_res == "int" and type(result) == int:
                        self.memoryG.updateMemory(self.res, result)
                    elif t_res == "float" and type(result) == float:
                        self.memoryG.updateMemory(self.res, result)
                    else:
                        raise TypeError("Input and variable type do not match")
            elif self.op == 102:
                if self.res >= 11000 and self.res < 12000:
                    result = self.memoryG.getValue(self.res)
                    result = result.replace('"', '')
                    result = result.replace("\\n", "\n")
                    print(result, end="")
                else:
                    result = self.memoryG.getValue(self.res)
                    print(result)
            
            # Turtle graphics functions
            elif self.op == 103:
                if self.left >= 5000 and self.left < 9000:
                    # local variable
                    x = memoryL.getLocalValue(self.left)
                else:
                    x = self.memoryG.getValue(self.left)

                if self.right >= 5000 and self.right < 9000:
                    y = memoryL.getLocalValue(self.right)
                else:
                    y = self.memoryG.getValue(self.right)
                
                self.trt.setpos(x, y)
            elif self.op == 104:
                if self.left >= 5000 and self.left < 9000:
                    # local variable
                    radius = memoryL.getLocalValue(self.left)
                else:
                    radius = self.memoryG.getValue(self.left)

                self.trt.circle(radius)
            elif self.op == 105:
                if self.left >= 5000 and self.left < 9000:
                    # local variable
                    distance = memoryL.getLocalValue(self.left)
                else:
                    distance = self.memoryG.getValue(self.left)
                
                if self.right == "vertical":
                    self.trt.sety(distance)
                else:
                    self.trt.setx(distance)
            elif self.op == 106:
                if self.left >= 5000 and self.left < 9000:
                    # local variable
                    radius = memoryL.getLocalValue(self.left)
                else:
                    radius = self.memoryG.getValue(self.left)

                if self.right >= 5000 and self.right < 9000:
                    angle = memoryL.getLocalValue(self.right)
                else:
                    angle = self.memoryG.getValue(self.right)
                
                self.trt.circle(radius, angle)
            elif self.op == 107:
                self.trt.penup()
            elif self.op == 108:
                self.trt.pendown()
            elif self.op == 109:
                if self.left >= 5000 and self.left < 9000:
                    # local variable
                    red = memoryL.getLocalValue(self.left)
                else:
                    red = self.memoryG.getValue(self.left)

                if self.right >= 5000 and self.right < 9000:
                    green = memoryL.getLocalValue(self.right)
                else:
                    green = self.memoryG.getValue(self.right)
                
                if self.res >= 5000 and self.res < 9000:
                    blue = memoryL.getLocalValue(self.res)
                else:
                    blue = self.memoryG.getValue(self.res)
                
                self.trt.screen.colormode(255)
                self.trt.pencolor(red, green, blue)
            elif self.op == 110:
                if self.left >= 5000 and self.left < 9000:
                    # local variable
                    width = memoryL.getLocalValue(self.left)
                else:
                    width = self.memoryG.getValue(self.left)
                
                self.trt.width(width)
            elif self.op == 111:
                self.trt.clear()

            # conditionals and loops
            elif self.op == 30:
                self.instruction = self.res - 1
            elif self.op == 31:
                if self.left >= 5000 and self.left < 9000:
                    if memoryL.getLocalValue(self.left) == 0:
                        self.instruction = self.res - 1
                else:
                    if self.memoryG.getValue(self.left) == 0:
                        self.instruction = self.res - 1
            elif self.op == 32:
                if self.left >= 5000 and self.left < 9000:
                    if memoryL.getLocalValue(self.left) == 1:
                        self.instruction = self.res - 1
                else:
                    if self.memoryG.getValue(self.left) == 1:
                        self.instruction = self.res - 1

            # functions
            elif self.op == 33: # ERA
                if self.funcName != '':
                    # More than one local memory
                    tempMemoryL = self.prevMemoryL[len(self.prevMemoryL) - 1]
                    self.prevFunc.append(self.funcName)
                    parami, paramf, vari, varf, tempi, tempf = self.breakFunctionSizes(self.res)
                    self.funcName = self.res
                    self.prevMemoryL.append(LocalMemory(parami, paramf, vari, varf, tempi, tempf))
                    memoryL = self.prevMemoryL[len(self.prevMemoryL) - 1]
                    self.isAsleep = False
                else:
                    parami, paramf, vari, varf, tempi, tempf = self.breakFunctionSizes(self.res)
                    self.funcName = self.res
                    self.prevMemoryL.append(LocalMemory(parami, paramf, vari, varf, tempi, tempf))
                    memoryL = self.prevMemoryL[len(self.prevMemoryL) - 1]
            elif self.op == 34: # PARAM
                if self.left >= 5000 and self.left < 9000:
                    result = tempMemoryL.getLocalValue(self.left)
                    self.isAsleep = True
                else:
                    result = self.memoryG.getValue(self.left)
                
                memoryL.setParam(result)
                # memoryL.show()
            elif self.op == 35: # GOSUB
                funcDir = self.getFuncDir(self.res)
                self.prevInstruction.append(self.instruction)
                self.instruction = funcDir - 1
            elif self.op == 36: # ENDFUNC
                if len(self.prevMemoryL) >= 2:
                    self.prevMemoryL.pop()
                    memoryL = self.prevMemoryL[len(self.prevMemoryL) - 1]
                    tempMemoryL = self.prevMemoryL[len(self.prevMemoryL) - 2]
                    self.funcName = self.prevFunc.pop()
                elif len(self.prevMemoryL) == 1:
                    memoryL = self.prevMemoryL.pop()
                    self.funcName = ''
                else:
                    del memoryL
                    self.funcName = ''
                
                self.instruction = self.prevInstruction.pop()
            elif self.op == 100: # Return
                
                if self.res >= 5000 and self.res < 9000:
                    result = memoryL.getLocalValue(self.res)
                else:
                    result = self.memoryG.getValue(self.res)
                
                retVariable = self.funcName + "Value"
                retVariableDir = self.getGlobalVariableDir(retVariable)
                self.memoryG.updateMemory(retVariableDir, result)
                


            # print(self.instruction)
            self.instruction = self.instruction + 1
        turtle.done()
        print('\n')
        self.memoryG.show()
        # print(quadruples)
