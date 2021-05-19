funcCount = 0
funcTable = {}
varTable = {}
varCount = 0
class FuncTable():
  def addFunc (self, name, returnType):
    global funcTable
    global funcCount
    global varCount

    varCount = 0

    nameFlag = False
    for i in range(len(funcTable)):
      if name == funcTable[i]["name"]:
        nameFlag = True
    
    if not nameFlag:
      tempDict = {
        "name": name,
        "type": returnType,
        "scope": funcCount,
        "dir": 0,
        "varT": {}
      }

      funcTable[funcCount] = tempDict
      funcCount = funcCount + 1
    else:
      print("nombre existente")

  def show(self):
    print(funcTable)


class VarTable():
  def addVar (self, name, varType, size):
    global varTable
    global funcTable
    global funcCount
    global varCount
    nameFlag = False
    tempDict = {}

    # check if variable name exists as a function name
    for i in range(len(funcTable)):
      if name == funcTable[i]["name"]:
        nameFlag = True
    
    # check if variable name exists as another local variable
    for i in range(len(funcTable[funcCount-1]["varT"])):
      if name == funcTable[funcCount-1]["varT"][i]["name"]:
        nameFlag = True

    if not nameFlag:
        tempDict = {
            "name": name,
            "type": varType,
            "dim": size,
            "scope": funcCount-1,
            "dir": 0,
        }
        funcTable[funcCount-1]["varT"][varCount] = tempDict
        varCount = varCount + 1
    else:
      print("nombre de var existente")

  def searchVar (self, id, scope):
    print("serchVar entra")
    for i in range(len(funcTable[scope]["varT"])):
      if id == funcTable[scope]["varT"][i]["name"]:
        return funcTable[scope]["varT"][i]["type"]

    # print("variable does not exists")
    # exit()
    raise NameError("variable does not exists")

  def show(self):
    print(varTable)