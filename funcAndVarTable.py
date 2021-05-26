# global variables
currentFunc = ''
funcTable = {}
varTable = {}

class FuncTable():
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
      raise NameError("function name already exists")

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
      raise NameError("function does not exists")

  def setParam (self, name, param):
    global funcTable

    if name in funcTable:
      funcTable[name]["param"].extend(param)
    else:
      raise NameError("Function does not exists")

  def getParam (self, name):
    global funcTable

    if name in funcTable:
      return funcTable[name]["param"]
    else:
      raise NameError("Function does not exists")

  def getType (self, name):
    global funcTable

    if name in funcTable:
      return funcTable[name]["type"]
    else:
      raise NameError("Function does not exists")

  def setDir (self, name, address):
    global funcTable

    if name in funcTable:
      funcTable[name]["dir"] = address
    else:
      raise NameError("Function does not exists")

  def searchFunc (self, name):
    global funcTable

    if name in funcTable:
      return 1
    else:
      raise NameError("Function does not exists")

  def delVarT (self, name):
    global funcTable

    if name in funcTable:
      del funcTable[name]["varT"]
    else:
      raise NameError("Function name does not exists")

  def getTable (self):
    return funcTable

  def show(self):
    print(funcTable)


class VarTable():
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

  def getDir (self, id, funcName, globalFunc):
    global funcTable

    if id in funcTable[funcName]["varT"]:
      return funcTable[funcName]["varT"][id]["dir"]
    elif id in funcTable[globalFunc]["varT"]:
      return funcTable[globalFunc]["varT"][id]["dir"]

    raise NameError("variable does not exists") 

  def searchVar (self, id, funcName, globalFunc):
    global funcTable
    
    if id in funcTable[funcName]["varT"]:
      return 1
    elif id in funcTable[globalFunc]["varT"]:
      return 1
    else:
      raise NameError("variable does not exists")

  def show(self):
    print(varTable)