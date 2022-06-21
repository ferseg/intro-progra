from multiprocessing.dummy import current_process


def separar():
    print("========================")

'''
1. Escriba un programa que imprima el siguiente patrón
*
**
***
****
del tamaño especificado por el usuario.
Params:
    - tamano: El tamaño que el usuario quiere el patrón (tamaño de arriba a abajo, altura)
Return:
    - No retorna nada, sólo imprimer el patrón según corresponda
Test cases:
    - imprimir_patron(3)
    # *
    # **
    # ***
    - imprimir_patron(5)
    # *
    # **
    # ***
    # ****
    # *****
'''


def imprimir_patron(num):
    contador = 0
    asterisco = "*"
    while contador < num:
        contador += 1
        print(asterisco * contador)


imprimir_patron(3)
separar()
imprimir_patron(5)
separar()

'''
2. Escriba un programa que reciba una lista de números enteros y devuelva 
la lista con los dobles (elementos multiplicados por 2) de cada nuero
Params:
    - nums: una lista de numeros enteros
Return:
    - La lista con cada elemento multiplicado por 2 (el doble)
Test cases:
    - sacar_dobles([1,2,3]) # => [2,4,6]
    - sacar_dobles([10,55,33]) # => [20,110,66]
    - sacar_dobles([0,-2,9]) # => [0,-4,18]
'''


def sacar_dobles(nums):
    idx = 0
    len_list = len(nums)
    while idx < len_list:
        nums[idx] *= 2
        idx += 1
    return nums


print(sacar_dobles([1, 2, 3]))
print(sacar_dobles([10, 55, 33]))

'''
[1,5,7]
Iteracion | idx | len | lista[idx] | lista[idx] *= 2
----------|-----|-----|------------|--------------------
1         |  0  |  3  |    1       | lista[0] *= 2 = 2  
2         |  1  |  3  |    5       | lista[1] *= 2 = 10  
3         |  2  |  3  |    7       | lista[2] *= 2 = 14
4         |  3  |  3 -> [2,10,14]

'''

'''
3. Escriba un programa que reciba una lista de números enteros y devuelva
sólo los numeros pares en la lista
Params:
    - nums: una lista de numeros enteros.
Return:
    - Los números pares en la lista
Test cases:
    - filtrar_pares([1,3,5]) # => []
    - filtrar_pares([1,3,4]) # => [4]
    - filtrar_pares([1,3,4,7,10,8]) # => [4,10,8]
'''
def filtrar_pares(nums):
    idx = 0
    # Donde almacenar mis elementos que cumplen el criterio
    result = []
    # Mientras el indice actual sea menor que la longitud de la lista
    # (Que el indice se encuentre dentro de la lista)
    while idx < len(nums):
        current_value = nums[idx]
        # Si el valor en la posicion actual es par
        # entonces agreguelo a la lista
        if current_value % 2 == 0:
            result.append(current_value)
        # Incremento el indice actual para que apunte a la siguiente posicion
        idx += 1
    # Una vez que terminó la ejecucion del while, devuelva el resultado
    return result

print(filtrar_pares([1,3,5]))
print(filtrar_pares([1,3,4])) # => [4]
print(filtrar_pares([1,3,4,7,10,8])) # => [4,10,8]

range(6)