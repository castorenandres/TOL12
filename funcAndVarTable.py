# global variables
currentFunc = ''
funcTable = {}
varTable = {}

class FuncTable():
  # Add function to function table
  def addFunc (self, name, returnType):
    global funcTable
    global currentFunc

    nameFlag = False
    if name in funcTable:
      nameFlag = True
    
    if not nameFlag:
      tempDict = {
        "type": returnType,
        "dir": None,
        "param": [],
        "size": {},
        "varT": {}
      }
      funcTable[name] = tempDict
      currentFunc = name
    else:
      raise NameError("Function name already exists")

  # Sets the size of the functions
  def setFuncSize (self, name, parami, paramf, vari, varf, tempi, tempf):
    global funcTable

    if name in funcTable:
      funcSize = {
        "parami": parami,
        "paramf": paramf,
        "vari": vari,
        "varf": varf,
        "tempi": tempi,
        "tempf": tempf
      }
      funcTable[name]["size"] = funcSize
    else:
      raise NameError("Function does not exists")

  # Sets the parameters type used in a function
  def setParam (self, name, param):
    global funcTable

    if name in funcTable:
      funcTable[name]["param"].extend(param)
    else:
      raise NameError("Function does not exists")

  # Gets the parameters type used in a function
  def getParam (self, name):
    global funcTable

    if name in funcTable:
      return funcTable[name]["param"]
    else:
      raise NameError("Function does not exists")

  # Gets the type of a function
  def getType (self, name):
    global funcTable

    if name in funcTable:
      return funcTable[name]["type"]
    else:
      raise NameError("Function does not exists")

  # Sets the address that defines the start of the function
  def setDir (self, name, address):
    global funcTable

    if name in funcTable:
      funcTable[name]["dir"] = address
    else:
      raise NameError("Function does not exists")

  # Searchs a function in the function table, if it exists it returns a 1, otherwise an error is raised
  def searchFunc (self, name):
    global funcTable

    if name in funcTable:
      return 1
    else:
      raise NameError("Function does not exists")

  # Deletes the variable table of a function
  def delVarT (self, name):
    global funcTable

    if name in funcTable:
      del funcTable[name]["varT"]
    else:
      raise NameError("Function name does not exists")

  # Returns function table
  def getTable (self):
    return funcTable

  # Prints function table
  def show(self):
    print(funcTable)


class VarTable():
  # Add a variable to the variable table
  def addVar (self, name, varType, size, address):
    global varTable
    global funcTable
    global currentFunc
    nameFlag = False
    tempDict = {}

    # check if variable name exists as a function name
    if name in funcTable:
      nameFlag = True
    
    # check if variable name exists as another local variable
    if name in funcTable[currentFunc]:
      nameFlag = True

    if not nameFlag:
        tempDict = {
            "type": varType,
            "dim": size,
            "dir": address,
        }
        funcTable[currentFunc]["varT"][name] = tempDict
    else:
      raise NameError("variable name already exists")

  # Add the function name + 'Value' as a variable to the global variables table
  def addFuncNameAsVar (self, name, varType, size, address, globalFunc):
    global varTable
    global funcTable
    global currentFunc
    nameFlag = False
    tempDict = {}

    # check if variable name exists as a function name
    if name in funcTable:
      nameFlag = True
    
    # check if variable name exists as another local variable
    if name in funcTable[globalFunc]:
      nameFlag = True

    if not nameFlag:
        tempDict = {
            "type": varType,
            "dim": size,
            "dir": address,
        }
        funcTable[globalFunc]["varT"][name] = tempDict
    else:
      raise NameError("variable name already exists")

  # Gets address of variable
  def getDir (self, id, funcName, globalFunc):
    global funcTable

    if id in funcTable[funcName]["varT"]:
      return funcTable[funcName]["varT"][id]["dir"]
    elif id in funcTable[globalFunc]["varT"]:
      return funcTable[globalFunc]["varT"][id]["dir"]

    raise NameError("variable does not exists") 

  # Search in variable table for a variable, if it exists returns 1, otherwise an error is raised
  def searchVar (self, id, funcName, globalFunc):
    global funcTable
    
    if id in funcTable[funcName]["varT"]:
      return 1
    elif id in funcTable[globalFunc]["varT"]: # Search in global variable table
      return 1
    else:
      raise NameError("variable does not exists")

  # Prints variable table
  def show(self):
    print(varTable)