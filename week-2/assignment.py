# 1. Cree un programa que solicite al usuario (input => str) el peso en kg y la estatura en metros
# y calcule el IMC (Indice de Masa Corporal)
#
# Nota1: El IMC = peso_kg / (estatura_en_metros * estatura_en_metros)
# Nota2: Recuerde que tanto el peso como la estatura pueden ser numeros flotantes (float)
# es decir, deberá convertir de string a float
peso_kg_str = input("Digite su peso: ")  # str
estatura_m_str = input("Digite su estatura en metros: ")  # str
peso_kg = float(peso_kg_str)  # 25.8 => int(25.8) => 25
estatura_m = float(estatura_m_str)
imc = peso_kg / (estatura_m * estatura_m)
print("Su IMC es de", imc)

# 2. Cree un programa que solicite (input) un numero entero (int()) al usuario y saque el último dígito
# de izquierda a derecha y lo imprima
# Por ejemplo:
#  - Si el usuario digita 546, deberá imprimir: El último dígito del número 546 es 6
#  - Si el usuario digita 9, deberá imprimir: l último dígito del número 9 es 9
# Nota: Para este ejercicio comúnmente se usa el operador % (modulo) => residuo de la división
# x / y = 25 -> 30 = resiudo 0
# x / y = 25.5 -> 3.3 = residuo not 0
# 546 / x = 6
num_str = input("Digite el numero: ")
num = int(num_str)
ult_digito = num % 10
print("El último dígito es: ", ult_digito)


# 3. Cree un programa que desee los buenos días al nombre que digita el usuario
# Por ejemplo:
#  - Si el usuario digita Fernando, deberá imprimir: Buenos días Fernando!
nombre = input("Digite su nombre: ")
print("Buenos días", nombre, "!")


# 4. Cree un programa que solicite el valor de un platillo en un restaurante sin I.V. (13%)
# y devuelva el valor del platillo con el I.V y el impuesto de servicio (10%)
# Por ejemplo:
#  - Si el usuario digita que el platillo cuesta 1000, entonces el programa calcula el impuesto
# de servicio (10%), es decir 100 colones, y el impuesto de ventas (13%), es decir 130 colones
# al sumar ambos valores al valor del platillo queda un total de 1230 colones, entonces, el
# programa debe imprimir: El platillo con impuestos tiene un valor de 1230 colones
valor_sin_impuesto = float(input("Digite el valor del platillo: "))
valor_con_impuesto = valor_sin_impuesto * 1.23
print("El valor del platillo con impuestos es:", valor_con_impuesto)

valor_str = input("Digite el valor del platillo: ")
valor_sin_impuesto = float(valor_str)
impuesto_13 = valor_sin_impuesto * 0.13
impuesto_10 = valor_sin_impuesto * 0.1
valor_con_impuesto = valor_sin_impuesto + impuesto_13 + impuesto_10
print("El valor del platillo con impuestos es:", valor_con_impuesto)


# 5. Cree un programa que solicite 3 números y saque el promedio de los 3 número
# Por ejemplo:
#  - el usuario digita 3 3 3, el programa debe decir: El promedio de los tres números es: 3
