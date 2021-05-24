funcCount = 0
currentFunc = ''
funcTable = {}
varTable = {}
varCount = 0
class FuncTable():
  def addFunc (self, name, returnType):
    global funcTable
    global funcCount
    global varCount
    global currentFunc

    varCount = 0

    nameFlag = False
    # for i in range(len(funcTable)):
    #   if name == funcTable[i]["name"]:
    #     nameFlag = True
    if name in funcTable:
      nameFlag = True
    
    if not nameFlag:
      tempDict = {
        # "name": name,
        "type": returnType,
        # "scope": funcCount,
        "dir": 0,
        "param": [],
        "size": {},
        "varT": {}
      }

      # funcTable[funcCount] = tempDict
      funcTable[name] = tempDict
      currentFunc = name
      # funcCount = funcCount + 1
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

  def getParam (self, name):
    global funcTable

    if name in funcTable:
      return funcTable[name]["param"]
    else:
      raise NameError("function does not exists")

  def show(self):
    print(funcTable)


class VarTable():
  def addVar (self, name, varType, size):
    global varTable
    global funcTable
    global funcCount
    global varCount
    global currentFunc
    nameFlag = False
    tempDict = {}

    # check if variable name exists as a function name
    # for i in range(len(funcTable)):
    #   if name == funcTable[i]["name"]:
    #     nameFlag = True
    if name in funcTable:
      nameFlag = True
    
    # check if variable name exists as another local variable
    # for i in range(len(funcTable[funcCount-1]["varT"])):
    #   if name == funcTable[funcCount-1]["varT"][i]["name"]:
    #     nameFlag = True
    if name in funcTable[currentFunc]:
      nameFlag = True

    if not nameFlag:
        tempDict = {
            # "name": name,
            "type": varType,
            "dim": size,
            # "scope": funcCount-1,
            "dir": 0,
        }
        # funcTable[funcCount-1]["varT"][varCount] = tempDict
        funcTable[currentFunc]["varT"][name] = tempDict
        # varCount = varCount + 1
    else:
      raise NameError("variable name already exists")

  def searchVar (self, id, funcName):
    global funcTable
    print("serchVar entra")
    # for i in range(len(funcTable[scope]["varT"])):
    #   if id == funcTable[scope]["varT"][i]["name"]:
    #     return funcTable[scope]["varT"][i]["type"]
    if id in funcTable[funcName]["varT"]:
      return funcTable[funcName]["varT"][id]["type"]

    # print("variable does not exists")
    # exit()
    raise NameError("variable does not exists")

  def show(self):
    print(varTable)