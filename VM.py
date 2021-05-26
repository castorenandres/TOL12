# # import
from MemoryVM import GlobalMemory
from MemoryVM import LocalMemory
# class VirtualMachine:
#     # memoria puede ser con arreglos y por tipos traer de la clase memoria
#     # hacer funciones para obtener el valor que esta dentro de la memoria
#     # funcion que recibe cuadruplo, tabla de funcion y tabla de constantes
#     # hago los ifs, elifs para checar op

# para operaciones checar con la direccion si es un getValue o updateMemory gloabl o local

mem = GlobalMemory()
localM = LocalMemory(2, 0, 5, 0, 6, 0)
localM.setParam(10)
localM.setParam(30)
localM.updateLocalMemory(5003, 8)
localM.updateLocalMemory(6000, 90)
localM.show()
localV = localM.getLocalValue(6000)
print(localV)

# mem.setConstants(10450, 3.1415)
# mem.setGlobalVariables(1500)
# mem.setTempVariables(4200, 2.4)
# mem.updateMemory(1500, 35)
# mem.show()
# val = mem.getValue(1500)
# print(val)