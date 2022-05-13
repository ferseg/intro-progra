# Solución del ejercicio
num1 = 12
num2 = 235.1
res1 = num1 + num2
res2 = num1 - num2

print(res1)
print(res2)

# devolver (return) un resultado
#
# str(x) => "x"
# type(x) => x es de tipo algo
# int(x) => x como entero
# print(a1, a2, a3,...)

type_res1 = type(res1)  # El valor de res1 => <class 'float'>
type_res2 = type(res2)

print(type(res1), type(res2))

print(type_res1, type_res2)

# input: Recibir una interacción del usuario, o una entrada
# input("Escriba un numero: ") => retornar el valor ingresado
valor_ingresado = input("Escriba un número: ")

print("El numero que escribiste es: " + valor_ingresado)

# El programa va a solicitar (input o interacción)
# 2 numeros y va a desplegar la suma de esos 2 numeros

# Pregunto por el primer numero
num1 = input("Digite numero 1: ")
# Pregunto por el segundo numero
num2 = input("Digite numero 2: ")

# Como los numeros estan en str tengo que convertirlo a entero
int_num1 = int(num1)
int_num2 = int(num2)

# Asigno la suma del resultado a una variable
resultado_suma = int_num1 + int_num2

# Imprimo el resultado. *(Sin el print no se puede imprimir el resultado en la consola)*
print("La suma de los numeros es:", resultado_suma)

# ========================================================
# Solicitar un numero y lo eleva al cuadrado
num = input("Digite un numero para elevarlo al cuadrado: ")  # string

# int_num va a contener el numero digitado por el usuario pero en forma de entero
int_num = int(num)
# Multiplico el numero que ingresaron por si mismo para obtener el cuadrado
resultado_cuadrado = int_num * int_num
# Imprimo el cuadrado de manera mas entendible
print("El cuadrado del numero", num, "es:", resultado_cuadrado)

# ========================================================
# Solicitar 2 numeros y sacar el residuo de la división
# del primer numero entre el segundo
num1 = input("Digite un numero: ")  # string
num2 = input("Digite un numero: ")  # string

int_num1 = int(num1)
int_num2 = int(num2)

# => resultado = int(num1) % int(num2) => resultado = int("") % int("")
resultado = int_num1 % int_num2

print("El residuo de la division es:", resultado)
