'''
1. Escriba un programa que reciba una lista con 3 numeros enteros e indique 
si la lista está ordenada (de menor a mayor)
Params:
    - nums: una lista con 3 numeros enteros
Return:
    - True si la lista está ordenada
    - False si la lista NO está ordenada
Test Cases:
    - esta_ordenada([1, 2, 3]) # => True
    - esta_ordenada([1, 3, 2]) # => False
'''


def esta_ordenada(nums):
    # Solo debo revisar los indices en orden para saber que estan ordenados
    return nums[0] <= nums[1] and nums[1] <= nums[2]


print(esta_ordenada([1, 2, 3]))
print(esta_ordenada([3, 2, 1]))
print(esta_ordenada([1, 3, 3]))


'''
2. Escriba un programa que invierta los valores del primer elemento de la
lista con el último.
Params:
    - lista: Una lista de elementos
Return:
    - La lista con el primer y último valor intercambiados
Test Case:
    - invertir_valores(["hola", 1, 2, 3]) # => [3, 1, 2, "hola"]
    - invertir_valores([50, 10, 2, 35]) # => [35, 10, 2, 50]
    - invertir_valores(["hola"]) # => ["hola"]
'''


def invertir_valores(lst):
    # Si la lista es de tamano 1 no tengo que invertirla
    if len(lst) == 1:
        return lst
    # De lo contrario tengo que formar una nueva lista de la siguiente forma
    # - Agarrar el ultimo elemento de la lista
    # - Concatenar el ultimo elemento con una sub-lista que no contenga el primer elemento
    # - Concatenar el primer elemento de la lista con el resto
    # Nota: Como los elementos que obtengo no son listas, tengo que convertirlos a lista
    # para poder concatenarlos
    ultimo_elemento = lst[-1]
    sub_lista = lst[1:-1]
    primer_elemento = lst[0]
    return [ultimo_elemento] + sub_lista + [primer_elemento]


print(invertir_valores(["hola", 1, 2, 3]))  # => [3, 1, 2, "hola"]


'''
3. Escriba un programa que reciba 2 listas y devuelva una lista con 
los primeros 2 elementos de la primera lista y los últimos 2 elementos 
de la segunda lista.
Params:
    - lista1: Una lista
    - lista2: Una lista
Validaciones:
    - Debe asegurarse que lista1 y lista2 tienen un tamaño de al menos 2 elementos
Return:
    - Una lista con los primeros 2 elementos de lista1 y los últimos 2 elementos
    de lista2
    - Si alguna de las 2 listas no tiene al menos un tamaño de 2 entonces
    devolver una lista vacía []
Test Cases:
    - fusionar_listas([1, 2, 3], [4, 5, 6]) # => [1, 2, 5, 6] 
    - fusionar_listas(["hola", 2, 3, 8], [4, 5, 6, 9, "adios"]) # => ["hola", 2, 9, "adios"] 
    - fusionar_listas(["hola"], [4, 5, 6, 9, "adios"]) # => [] 
    - fusionar_listas(["hola"], ["adios"]) # => [] 
'''


def fusionar_listas(lista1, lista2):
    if len(lista1) < 2 or len(lista2) < 2:
        return []
    # De [:2] estoy diciendo que quiero una sub lista desde el índice 0 hasta el 2 sin incluir el 2
    # De [-2:] estoy diciendo que quiero una sub lista desde el penúltimo elemento hasta el último
    return lista1[:2] + lista2[-2:]

def fusionar_listas2(lista1, lista2):
    if len(lista1) < 2 or len(lista2) < 2:
        return []
    len_lista2 = len(lista2)
    indice_inicio = len_lista2 - 2
    return lista1[:2] + lista2[indice_inicio:]


print(fusionar_listas([1, 2, 3], [4, 5, 6]))  # => [1, 2, 5, 6]
# => ["hola", 2, 9, "adios"]
print(fusionar_listas(["hola", 2, 3, 8], [4, 5, 6, 9, "adios"]))
