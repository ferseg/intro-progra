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