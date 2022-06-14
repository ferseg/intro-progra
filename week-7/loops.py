'''
Loop = ciclo = bucle

Es una tarea repetitiva

Cada vez que se encuntre un loop el código dentro del loop
se va a ejecutar cierta cantidad de veces, la cantidad de veces
va a ser determinada por diferentes condiciones y también varia
dependiendo del tipo de ciclo que estamos ejecutando

while (mientras):

while condicion: # mientras la condición sea True el código se va a seguir
ejecutando

while condicion:
    linea1
    linea2
    ultima_linea_del_while
..
..
'''

contador = 0

'''
Iteración 1:
contador = 0 
print
contador += 1

Iteracion 2:
contador = 1
print
contador += 1

Iteración 3:
contador = 2
print
contador +=1

Iteración 4:
contador = 3
print
contador += 1

Iteración 5:
contador = 4
print
contador += 1

Iteracion 6:
contador = 5
X print

'''
while contador < 5:
    print(contador)
    contador += 1

print("Salió del ciclo")


estudiantes = ["Melissa", "Jonathan", "Migue", "Eduardo", "Camila"] # 5
print(estudiantes)

idx_actual = 0 # 0, 1, 2, 3, 4, 5
len_lista = len(estudiantes) # 5
print("len de la lista", len_lista)
while idx_actual < len_lista:
    print( estudiantes[idx_actual] )
    idx_actual += 1