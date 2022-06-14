'''
1. Escriba un programa que reciba un numero entero y dos posiciones conteniadas 
en el numero, basado en las posiciones indicadas se deben cambiar los valores 
en dicha posiciones.
Params:
    - num: El numero a ser cambiado
    - pos1: la posicion 1 a cambiar en el numero
    - pos2: la posicion 2 a cambiar con la posicion 1
Return:
    - El numero con las posiciones invertidas
Validations:
    - Las posiciones 1 y 2 deben estar contenidas en el numero
    - Si el numero es de tamano 1, no se realiza ninguna conversion
Tips: Para realizar este ejercicio se puede considerar hacer una conversion de 
entero a str, pero recuerde que el resultado debe ser de tipo entero
Test cases:
    - invertir_digitos(7284, 1, 3) # => 8274 (se invierte el 7 con el 8)
    - invertir_digitos(72, 1, 3) # => -1 (Porque el segundo indice no se encuentra dentro del numero)
    - invertir_digitos(876689, 5, 4) # => 876869 (Se invierte el 6 con el 8) 
'''
# mi_str = "Mi str"
# mi_str[0] = "h"


def invertir_digitos(num, pos1, pos2):
    str_num = str(num)  # 123 -> "123"
    list_num = list(str_num)  # "123" -> ["1", "2", "3"]
    len_num = len(str_num)
    if len_num < pos1 or len_num < pos2:
        return -1
    idx_pos_1 = pos1 - 1
    idx_pos_2 = pos2 - 1
    valor_pos_2_orig = list_num[idx_pos_2]
    list_num[idx_pos_2] = list_num[idx_pos_1]
    list_num[idx_pos_1] = valor_pos_2_orig  # ["3", "2", "1"]
    str_resultado = "".join(list_num)  # "321"
    return int(str_resultado)


print(invertir_digitos(7284, 1, 3))  # => 8274 (se invierte el 7 con el 8)
print(invertir_digitos(72, 1, 3))
print(invertir_digitos(876689, 5, 4))  # => 876869

'''
2. La escuela Del Este quiere mantener un registro de estudiantes que se 
matricularon este anho, por esta razon le piden que haga un programa donde puedan
insertar el nombre de los usuarios y otro programa para obtener los nombres
Programa de registro:
    - Recibe el nombre del estudiante, si el estudiante no se encuentra registrado
    debe registrarlo, de caso contrario debe devolver "El estudiante ya fue registrado"
    Params:
        - nombre: El nombre del estudiante
    Return:
        - "El estudiante fue registrado exitosamente" en caso que se pudo insertar
        - "El estudiante ya fue registrado" en caso que ya se encuentre registrado
    Test cases:
        - ingresar_estudiante("Fernando") # => "El estudiante fue registrado exitosamente" 
        - ingresar_estudiante("Melissa") # => "El estudiante fue registrado exitosamente" 
        - ingresar_estudiante("Fernando") # => "El estudiante ya fue registrado" 
Programa de visualizacion:
    - Muestra todos los estudiantes registrador
    Params: ninguno
    Return: La lista de estudiantes ingresados
    Test cases:
        - listar_estudiantes() # => ["Fernando", "Melissa"]
Tip: Para este programa es conveniente tener una variable global de tipo lista
en la cual se puedan insertar los estudiantes y se pueda imprimir (print)
'''
estudiantes = []


def ingresar_estudiante(nombre):
    global estudiantes
    if nombre in estudiantes:
        return "El estudiante ya fue registrado"
    #estudiantes += [nombre]
    estudiantes.append(nombre)
    return "El estudiante fue registrado exitosamente"


def limpiar_registros():
    global estudiantes
    estudiantes = []


def imprimir_estudiantes():
    global estudiantes
    return estudiantes


print(ingresar_estudiante("Fernando"))
print(ingresar_estudiante("Melissa"))
print(ingresar_estudiante("Fernando"))

print(imprimir_estudiantes())


'''
3. Utilice el siguiente programa para generar
-
--
---
----
-----
------
-------
------
-----
----
---
--
-
'''
def generar_simbolos(cant):
    return "-" * cant


print(generar_simbolos(1))
print(generar_simbolos(2))
print(generar_simbolos(3))
print(generar_simbolos(4))
print(generar_simbolos(5))
print(generar_simbolos(6))
print(generar_simbolos(7))
print(generar_simbolos(6))
print(generar_simbolos(5))
print(generar_simbolos(4))
print(generar_simbolos(3))
print(generar_simbolos(2))
print(generar_simbolos(1))

'''
4. Que hace el siguiente programa?
'''
def que_hace(list1, list2):
    list1.reverse()  # [1,2,3] -> [3,2,1]
    list2.reverse()  # [4,5,6] -> [6,5,4]
    half_len_list1 = len(list1) // 2  # 1
    half_len_list2 = len(list2) // 2  # 1
    return list1[:half_len_list1] + list2[half_len_list2:]


print(que_hace([1, 2, 3, 10], [4, 5, 6]))

