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
      if name in funcTable[i]["name"]:
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

    for i in range(len(funcTable)):
      if name in funcTable[i]["name"]:
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

  def show(self):
    print(varTable)