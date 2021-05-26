# # import
from MemoryVM import GlobalMemory
from MemoryVM import LocalMemory
class VirtualMachine:
    memoryG = GlobalMemory()
    constantTable = {}
    funcTable = {}
    # programName = ''

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
        

# para operaciones checar con la direccion si es un getValue o updateMemory gloabl o local
# primero checar que se pongan variables globales y constantes en la memoria global
# hago los ifs, elifs para checar op

    # Main function of the virtual machine, runs the intermidiate code generated by the parser.
    def startProgram(self, quadruples, funcTable, constantTable):
        print("---------------------------------------------------------------")
        self.funcTable = funcTable
        self.constantTable = constantTable
        self.setGlobalVariables()
        self.setConstantVariables()
        # print(self.constantTable, '\n')
        # print(self.funcTable, "\n")
        # self.memoryG.show()
        print(quadruples)