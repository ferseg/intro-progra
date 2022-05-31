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
