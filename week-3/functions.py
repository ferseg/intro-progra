# convenciones de código
# Reglas => + entendible + limpio

# Variables:
#   - snake_case = cada_palabra_con_guion_bajo.
#   - no pueden empezar numero
#   - no pueden tener un caracter extraño (especial) $#@
#   - tratar siempre que tengan un significado, descriptivo
#   - sean en minúscula
#   - case sensitive: hola  Hola

# Funciones
# Seccion de código que se va a ejecutar cuando yo la llame explicitamente
# Forma: def nombre_funcion(parametro1, parametro2..., parametro_n):
# Funcion sin parametros
def imprimir_hola_mundo():
    print("Hola mundo!")


# Ejecute la funcion que se llama imprimir_hola_mundo
imprimir_hola_mundo()

# Parámetros: son valores de entrada de una función


def saludar(persona):
    print("Hola", persona)


saludar("Eduardo")  # print("Hola", "Eduardo")
saludar("Ariel")  # saludar(persona = "Ariel")
saludar("Meli")
saludar("Aqui yo puedo poner lo que yo quiera literalmente")


# num = int(input("Digitar numero entero: "))
# elevar_cuadrado(num)

# Valores de retorno
# input => str (lo que digito el usuario en string)
# print => no tiene valor de retorno
# mi_var = input("Algo: ")
# print(mi_var)

# print(elevar_cuadrado(50))

# return

# Función que me eleve al cuadrado
def solicitar_numero_entero(mensaje):
    return int(input(mensaje))


def solicitar_numero_float(mensaje):
    return float(input(mensaje))


def elevar_cuadrado(num):
    cuadrado = num * num
    return cuadrado


def calcular_imc():
    peso_kg = solicitar_numero_float("Digite su peso: ")
    estatura_m = solicitar_numero_float("Digite su estatura en metros: ")
    imc = peso_kg / elevar_cuadrado(estatura_m)
    print("Su IMC es de", imc)


calcular_imc()
