''''
mientras se_de_esto:
    haga_esto

while this:
    do this
'''

'''
Escriba un programa que reciba una lista y devuelva la suma de los elementos en la lista
Param:
    - nums: Una lista
Return:
    - La suma de los elementos en la lista
Test cases:
    - sumatoria([1,2,3]) # => 1+2+3 = 6
'''


def sumatoria_lista(lista):
    suma = 0
    x = 0
    while x < len(lista):
        suma += lista[x]
        x += 1
    return suma


print("La suma de los elementos de la lista es: ")
print(sumatoria_lista([1, 2, 3]))

lista = [1, 2, 3]
suma_lista = sum(lista)


'''
Escriba un programa que sume los elementos de dos listas en la misma posicion
Ej: sumar_listas([1,2,3], [4,5,6]) => [5, 7, 9]
'''


def sumar_listas(nums1, nums2):
    if len(nums1) != len(nums2):
        return []
    idx = 0
    result = []
    while idx < len(nums1):
        result_sum = nums1[idx] + nums2[idx]
        result.append(result_sum)
        idx += 1
    return result


print(sumar_listas([1, 2, 3], [4, 5, 6]))

print("==============================")

'''
range(n)
'''
x = range(5)
# [0,1,2,3,4]
print(x)

print("==============================")


'''
FOR LOOP
Itera a traves de los elementos
[1,2,3]
'''
x = [1, 2, 3]

for current_element in x:
    print(current_element)


print("==============================")


def filtrar_pares(nums):
    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num)
    return result


print(filtrar_pares([1, 3, 5]))
print(filtrar_pares([1, 3, 4]))  # => [4]
print(filtrar_pares([1, 3, 4, 7, 10, 8]))  # => [4,10,8]

print("==============================")


def sacar_mayor(nums):
    result = 0
    for num in nums:
        if num > result:
            result = num
    return result


print(sacar_mayor([3, 10, 25, 4, 7]))
print(sacar_mayor([3, 10, 25, 4, 70]))

print("==============================")


def sumar_listas_2(list1, list2):
    if len(list1) != len(list2):
        return []
    len_list1 = len(list1)
    result = []
    for idx in range(len_list1):
        result.append(list1[idx] + list2[idx])
    return result


print(sumar_listas_2([1, 2, 3, 12, 6], [4, 5, 6, 123, 63]))

print("==============================")

x, y = [1, 2]


def imprimir_patron(simbolos):
    for idx, simbolo in enumerate(simbolos):
        print(simbolo * (idx + 1))


imprimir_patron(["*", "-", "a", "+", "=", "+", "+", "s", "+", "z"])

print("==============================")

'''
                    ESPACIOS             SIMBOLO
      *           len(altura) - 1           1      n = 0 + 1
     ***          len(altura) - 2           3      n = 1 + 2
    *****         len(altura) - 3           5      n = 2 + 3
   *******        len(altura) - 4           7
  *********       len(altura) - 5           9
 ***********      len(altura) - 6           11
*************     len(altura) - 7           13
'''
def imprimir_arbol_navidad(simbolo, altura):
    for nivel in range(altura):
        nivel_mas_1 = nivel + 1
        cant_espacios = altura - nivel_mas_1
        cant_simbolos = nivel + nivel_mas_1
        print(" " * cant_espacios + simbolo * cant_simbolos)

imprimir_arbol_navidad("z", 11)