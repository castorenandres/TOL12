constantTable = {}

class ConstantTable:
    def addConstant (self, val, address):
        global constantTable

        if val in constantTable:
            raise NameError("Constant already exists")
        else:
            constantTable[val] = address

    def getDir (self, val):
        global constantTable

        if val in constantTable:
            return constantTable[val]
        else:
            raise NameError("Constant does not have an address")

    def searchConstant (self, val):
        global constantTable

        if val in constantTable:
            return 1
        else:
            return 0
    
    def show(self):
        global constantTable
        print(constantTable)