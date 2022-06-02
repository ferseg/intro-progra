def separar():
    print("=====================================")


'''
OR: Siempre va a ser True si uno de los elementos es True

     |  True  |  False
-----|--------|--------
True |  True  |  True
-----|--------|--------     
False|  True  |  False

==========================

AND: Siempre va a ser False si uno de los elementos es False

     |  True  |  False
-----|--------|--------
True |  True  |  False
-----|--------|--------     
False|  False |  False

==========================

NOT
not True = False
not False = True

'''
separar()
print("Operaciones con OR")
print(True or True)
separar()
print(True or False)
separar()
print(False or False)
separar()
separar()


print("Operaciones con AND")
print(True and True)
separar()
print(True and False)
separar()
print(False and False)
separar()
separar()


print("Operaciones con NOT")
print(not True)
separar()
print(not False)
separar()
separar()

a = "Hola"
b = "adios"

if len(a) > len(b) or len(b) > 10 or len(a) == 4:
    print("Entro en la primera condición OR")
# elif <==== Sólo se ejecuta si el if anterior da False (si no se ejecuta)
# if <===== Ejecútese a pesar que el if anterior haya sido True
if len(a) == 4 and len(b) == 5 and len(a) == 5:
    print("Entro en condición de AND")

condicion_para_not = len(a) == 4 and len(b) == 5 and len(a) == 5
print(condicion_para_not)
print(not(condicion_para_not))

if not(condicion_para_not):
    print("Entro en condición de NOT")

len_tel = 9
valid_case = len_tel == 8

if not(valid_case):
    print("Numero invalido")
