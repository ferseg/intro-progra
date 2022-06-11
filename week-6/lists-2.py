def separar():
    print("=====================================")
# Asignaciones a una posición específica de la lista
lista = [1, 2, 3, 4]
print(lista[3]) # => 4
print(lista) # => [1, 2, 3, 4]

lista[3] = 10
print(lista[3]) # => 10
print(lista) # => [1, 2, 3, 10]


separar()

def invertir_valores (lista):
    temp = lista[0]
    lista[0] = lista[-1]
    lista[-1] = temp
    return lista

print(invertir_valores([1, 3, 5, 84, 78]))

separar()

# Replicar un elemento n veces en una lista
# Haga una lista con el numero 10 repetido n veces
n = 5
lista_con_repetidos = [10] * n
print(lista_con_repetidos)

mi_str = "a"
mi_str_repetido = mi_str * n
print(mi_str_repetido)

separar()

'''
*********** 11
 ********* 9
  ******* 7
   ***** 5
    *** 3
     * 1
'''
asterisco = "*"
espacio = " "
n = 0

print(espacio * n + asterisco*11)
n = 1
print(espacio * n + asterisco*9)
n = 2
print(espacio * n + asterisco*7)
n = 3
print(espacio * n + asterisco*5)
n = 4
print(espacio * n + asterisco*3)
n = 5
print(espacio * n + asterisco)

separar()

# Unpack
# Desempaquetar, se refiere a asignar posiciones de una lista a una variable sin tener que
# especificar el índice
a, b, c = [1, 2, 3]
print(a)
print(b)
print(c)

separar()
lista_t =  [4, 5, 6, 10, 26, 457]
a, b, *c = lista_t
print(a)
print(b)
print(c)


# [p_e, *[,,,] , u_e]
def invertir_valores2 (lista):
    p_e, *resto, u_e = lista
    return [u_e] + resto + [p_e]

print(invertir_valores2 (lista_t))

separar()
# Remover elementos de una lista
lista = [1, 2, 3, 4, 5] # 5
lista_wo_last = lista[:-1]
print(lista_wo_last)
print(lista)
lista_wo_first = lista[1:]
print(lista_wo_first)
print(lista)

separar()
# pop(n) => n = indice que queremos remover, si es destructiva
lista.pop(len(lista) - 1)
print(lista)

# pop() => remover el último elemento
lista.pop()
print(lista)

# del
del lista[0]
print(lista)

separar()
# Copy list
lista = [5,5645,4,8,9]
copia_lista = lista.copy()

print(lista)
print(copia_lista)

lista[0] = "hola"

print(lista)
print(copia_lista)

separar()

lista2 = [6,3,62,5,6,762]
copia_lista2 = lista2

print(lista2)
print(copia_lista2)

lista2[0] = "hello"
print(lista2)
print(copia_lista2)


## Se crean en memoria
'''
| espacio 1   | espacio 2    |
| a = [1,2,3] | b = a.copy() |
| b = a       |              |
'''
separar()

# Append
lista_append = [1,2,3]
lista_append.append(4)

lista_ref = [1,2,3]
lista_ref2  = lista_ref + [4]
print(lista_append)
print(lista_ref)
print(lista_ref2)

# Revertir el orden de una lista
lista_append.reverse()
print(lista_append)
print("Some string")

separar()

