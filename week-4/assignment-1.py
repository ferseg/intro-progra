def separar():
    print("=====================================")


'''
1. Escriba un programa que reciba 2 números enteros y sume los últimos 2 dígitos 
de cada número entre sí.
Params:
    - num1: Es un número entero
    - num2: Es un número entero
Return:
    - La suma de los últimos 2 dígitos de cada número
Test cases:
    sumar_digitos_numeros(25, 27) # => (25 + 27) = 52
    sumar_digitos_numeros(5456, 786) # => (56 + 86) = 142
    sumar_digitos_numeros(135458, 5545) # => (58 + 45) = 103
    sumar_digitos_numeros(0, 1) # => (0 + 1) = 1
'''


def sumar_digitos_numeros(num1, num2):
    res_1 = num1 % 100
    res_2 = num2 % 100
    return res_1 + res_2


print(sumar_digitos_numeros(25, 27))  # => (25 + 27) = 52
print(sumar_digitos_numeros(5456, 786))  # => (56 + 86) = 142
print(sumar_digitos_numeros(135458, 5545))  # => (58 + 45) = 103
print(sumar_digitos_numeros(0, 1))  # => (0 + 1) = 1

separar()

'''
2. Escriba un programa que reciba un número entero, si el número recibido
es un multiplo de 2 (es decir el número par) elévelo al cubo (elevado a 3)
y devuelva el resultado de la operación
sino entonces eleve el número al cuadrado (elevado a 2) y devuelva el resultado
de la operación
Params:
    - num1: Es un número entero
Return:
    - Si el número es multiplo de 2, entonces el número elevado al cubo
    - Si el número no es múltiplo de 2, entonces el número elevado al cuadrado
Test cases:
    elevar_par_impar(2) # => Como 2 es multiplo de 2 (es decir par), entonces elevo al cubo 2 ** 3 = 8
    elevar_par_impar(3) # => Como 3 NO es multiplo de 2 (es decir impar), entonces elevo al cuadrado 3 ** 2 = 9
Tip:
    Para saber si un número es múltiplo de otro número, el residuo de la división de uno con el otro DEBE SER 0
'''


def es_multiplo(num, mult):
    return num % mult == 0


def elevar_par_impar(num1):
    if es_multiplo(num1, 2):
        return num1 ** 3
    else:
        return num1 ** 2


print(elevar_par_impar(2))
print(elevar_par_impar(3))
print(elevar_par_impar(50))
print(elevar_par_impar(51))

separar()
'''
3. Escriba un programa que reciba 2 strings, si el string 'a' tiene una longitud
mayor a la del string 'b' entonces retorne la concatenación de 'b' con 'a', sino retorne la
concatenación de 'a' con 'b'
Params:
    - str1: que es un string
    - str2: que es un string
Return:
    - La concatenación de a con b o de b con a dependiendo de las longitudes
Test cases:
    concatenar_strings_locos("Hola", "Mundo") # como la longitud (len) de b es mayor que a entonces retorna a con b = "Hola Mundo"
    concatenar_strings_locos("Holas!", "Mundo") # como la longitud (len) de a es mayor que b entonces retorna b con a = "Mundo Holas!"
    concatenar_strings_locos("Cuentos", "Largos") # => "Largos Cuentos"
'''


def concatenar_strings_locos(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    if len_str1 > len_str2:
        return str2 + " " + str1
    else:
        return str1 + " " + str2


# como la longitud (len) de b es mayor que a entonces retorna a con b = "Hola Mundo"
print(concatenar_strings_locos("Hola", "Mundo"))
# como la longitud (len) de a es mayor que b entonces retorna b con a = "Mundo Holas!"
print(concatenar_strings_locos("Holas!", "Mundo"))
print(concatenar_strings_locos("Cuentos", "Largos"))  # => "Largos Cuentos"

separar()
'''
Escriba un programa que reciba un numero entre 1 - 100
si el numero está fuera del rango, el programa debería retornar -1
si el numero está ente 1 y 30, el programa debe retornar 1
si el numero esta entre 31 y 70, el programa debe retornar 2
si el numero esta entre 71 y 100, el programa debe retornar 3
Params:
    - un numero entero (cualquiera)
Return:
    - -1 si el numero esta fuera del rango
    - 1 si esta entre 1 y 30
    - 2 si esta entre 31 y 70
    - 3 si esta entre 71 y 100
'''


def seccionar_estudiantes(num):
    if num < 1:
        return -1
    elif num > 100:
        return -1
    elif num > 70:
        return 3
    elif num > 30:
        return 2
    else:
        return 1


print(seccionar_estudiantes(101))
print(seccionar_estudiantes(100))
print(seccionar_estudiantes(71))
print(seccionar_estudiantes(70))
print(seccionar_estudiantes(31))
print(seccionar_estudiantes(1))
print(seccionar_estudiantes(30))
