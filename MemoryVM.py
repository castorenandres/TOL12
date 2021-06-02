from collections import deque

class GlobalMemory:
    globalMemory = {
        "int": {},
        "tempi": {},
        "float": {},
        "tempf": {},
        "intC": {},
        "floatC": {},
        "stringC": {}
    }

    # set constant to global memory
    def setConstants(self, address, value):
        if address < 12000 and address >= 9000:
            if address >= 11000:
                self.globalMemory["stringC"][address] = value
            elif address >= 10000:
                self.globalMemory["floatC"][address] = float(value)
            elif address >= 9000:
                self.globalMemory["intC"][address] = int(value)
        else:
            raise ValueError("Address is not a constant")

    # set global variable to global memory
    def setGlobalVariables(self, address):
        if address >= 3000 and address < 4000:
            self.globalMemory["float"][address] = None
        elif address >= 1000 and address < 2000:
            self.globalMemory["int"][address] = None
        else:
            raise ValueError("Address is not a global variable")

    # set temporary variables to global memory
    def setTempVariables(self, address, value):
        if address >= 4000 and address < 5000:
            self.globalMemory["tempf"][address] = value
        elif address >= 2000 and address < 3000:
            self.globalMemory["tempi"][address] = value
        else:
            raise ValueError("Address is not a temporal variable")

    # get type of variable
    def getType(self, address):
        if address < 12000 and address >= 1000:
            if address >= 11000:
                return "stringC"
            elif address >= 10000:
                return "floatC"
            elif address >= 9000:
                return "intC"
            elif address >= 5000 and address < 9000:
                raise MemoryError("Out of scope of global memory")
            elif address >= 4000:
                return "tempf"
            elif address >= 3000:
                return "float"
            elif address >= 2000:
                return "tempi"
            elif address >= 1000:
                return "int"
        else:
            raise ValueError("Address not found")

    # update variable's value
    def updateMemory(self, address, value):
        typeAddress = self.getType(address)
        if address in self.globalMemory[typeAddress]:
            self.globalMemory[typeAddress][address] = value
        else:
            raise IndexError("Address does not exists")
        
    # get value of variable
    def getValue(self, address):
        typeAddress = self.getType(address)
        
        if address in self.globalMemory[typeAddress]:
            if self.globalMemory[typeAddress][address] == None:
                raise ValueError("Varible is not initialized")
            else:
                return self.globalMemory[typeAddress][address]
        else:
            raise IndexError("Address does not exists")

    # Checks if a variable exists in global memory
    def isDir(self, address):
        for key in self.globalMemory:
            if address in self.globalMemory[key]:
                return 1
        return 0

    # prints global memory
    def show(self):
        print(self.globalMemory)

class LocalMemory:
    # Constructor
    # Adds the necessary register/space for the local memory
    def __init__(self, parami, paramf, vari, varf, tempi, tempf):
        self.intL = 5000
        self.tempiL = 6000
        self.floatL = 7000
        self.tempfL = 8000
        self.params = deque()
        self.paramsType = deque()
        self.localMemory = {
            "int": {},
            "tempi": {},
            "float": {},
            "tempf": {},
        }
        
        if parami != 0:
            for i in range(parami):
                self.localMemory["int"][self.intL] = None
                self.params.append(self.intL)
                self.paramsType.append("int")
                self.intL = self.intL + 1

        if paramf != 0:
            for i in range(paramf):
                self.localMemory["float"][self.floatL] = None
                self.params.append(self.floatL)
                self.paramsType.append("float")
                self.floatL = self.floatL + 1
        
        if vari != 0:
            for i in range(vari):
                self.localMemory["int"][self.intL] = None
                self.intL = self.intL + 1

        if varf != 0:
            for i in range(vari):
                self.localMemory["float"][self.floatL] = None
                self.floatL = self.floatL + 1

        if tempi != 0:
            for i in range(tempi):
                self.localMemory["tempi"][self.tempiL] = None
                self.tempiL = self.tempiL + 1

        if tempf != 0:
            for i in range(tempf):
                self.localMemory["tempf"][self.tempfL] = None
                self.tempfL = self.tempfL + 1

    # set parameter value to local memory
    def setParam(self, value):
        if len(self.params) > 0:
            paramAddress = self.params.popleft()
            paramType = self.paramsType.popleft()
            self.localMemory[paramType][paramAddress] = value
        else:
            raise IndexError("Parameter does not exists")

    # get type of variable
    def getType(self, address):
        if address < 9000 or address >= 5000:
            if address >= 8000:
                return "tempf"
            elif address >= 7000:
                return "float"
            elif address >= 6000:
                return "tempi"
            elif address >= 5000:
                return "int"
        else:
            raise ValueError("Address not found")

    # updates value of local variables
    def updateLocalMemory(self, address, value):
        typeAddress = self.getType(address)
        if address in self.localMemory[typeAddress]:
            self.localMemory[typeAddress][address] = value
        else:
            raise IndexError("Local address does not exists")

    # gets local variable value
    def getLocalValue(self, address):
        typeAddress = self.getType(address)
        
        if address in self.localMemory[typeAddress]:
            if self.localMemory[typeAddress][address] == None:
                if typeAddress == "tempi" or typeAddress == "tempf":
                    raise MemoryError("Temporal variable does not have value")
                else:
                    raise ValueError("Varible is not initialized")
            else:
                return self.localMemory[typeAddress][address]
        else:
            raise IndexError("Address does not exists")

    # prints local memory
    def show(self):
        print(self.localMemory)