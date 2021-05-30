constantTable = {}

class ConstantTable:
    # Add a constant to constant table
    def addConstant (self, val, address):
        global constantTable

        if val in constantTable:
            raise NameError("Constant already exists")
        else:
            constantTable[val] = address

    # Gets address of constant
    def getDir (self, val):
        global constantTable

        if val in constantTable:
            return constantTable[val]
        else:
            raise NameError("Constant does not have an address")

    # Search constant in constant table, if it exists returns 1, otherwise returns 0
    def searchConstant (self, val):
        global constantTable

        if val in constantTable:
            return 1
        else:
            return 0

    # Returns the constant table
    def getTable(self):
        return constantTable
    
    # Prints constant table
    def show(self):
        global constantTable
        print(constantTable)