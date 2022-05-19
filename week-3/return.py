# Return
# Definir un valor de retorno, yo puedo hacer uso de lo que devuelve la funcion
# y asignarla a una variable


def solicitar_numero_entero(mensaje):
    return int(input(mensaje))


def solicitar_numero_float(mensaje):
    return float(input(mensaje))


num_int = solicitar_numero_entero("Digite un número entero: ")
print(type(num_int))

# Puede devolver cualquier dato
# int
# float
# string

# Si el return no se define entonces va retornar un tipo que se llama None NoneType

# type(None) => NoneType


def solicitar_numero_entero_none(mensaje):
    print(int(input(mensaje)))


var_none = solicitar_numero_entero_none("Cualquier mensaje: ")
print(type(var_none))


def solicitar_numero_entero_opt(mensaje="Digite un numero entero: "):
    return int(input(mensaje))


print(solicitar_numero_entero_opt("Mensaje modificado: "))
print(solicitar_numero_entero_opt())

# Parámetros de la función:
#   - impuesto de ventas
#   - impuesto de servicio (propina)


def calcular_impuesto_al_platillo(imp_v, imp_s):
    valor_str = input("Digite el valor del platillo: ")
    valor_sin_impuesto = float(valor_str)
    valor_del_imp_v = valor_sin_impuesto * imp_v
    valor_del_imp_s = valor_sin_impuesto * imp_s
    valor_total = valor_sin_impuesto + valor_del_imp_v + valor_del_imp_s
    return valor_total


# Costa Rica
print(calcular_impuesto_al_platillo(13, 10))

# EU
# calcular_impuesto_al_platillo(imp_v = 0.15, imp_s = 0.1)
print(calcular_impuesto_al_platillo(15, 0))

# Crear una función que convierta un numero decimal a porcentaje
# Parámetro:
#    - numero entero
# Return:
#    - un numero flotante que va a ser el porcentaje del numero ingresado
# Por ejemplo:
#    - 13 -> 0.13
#    - 25 -> 0.25
#    - 3  -> 0.03
#    28 -> 28.0
#    28.0 / 1 = 28.0
#    28.0 / 10 = 2.80
#    28.8 / 100 = 0.280


def calcular_porcentaje(num):
    return num / 100


print(calcular_porcentaje(13))
print(calcular_porcentaje(25))
print(calcular_porcentaje(3))


# V2 de calcular impuesto
# En vez de recibir 2 parámetros, va a recibir 3
# Parámetros:
#   - valor_platillo (float)
#   - imp_v (int) (opcional, valor por defecto 13)
#   - imp_s (int) (opcional, valor por defecto 10)
# Return:
#   - Cálculo del platillo con impuestos
# NOTA: debe utilizar la funcion calcular_porcentaje para convertir los parámetros referentes al impuesto
def calcular_impuestos_v2(valor_sin_impuesto, imp_v=13, imp_s=10):
    imp_v_por = calcular_porcentaje(imp_v)
    impuesto_1 = valor_sin_impuesto * imp_v_por
    impuesto_2 = valor_sin_impuesto * calcular_porcentaje(imp_s)
    total = valor_sin_impuesto + impuesto_1 + impuesto_2
    return total


print(calcular_impuestos_v2(5000, 25, 15))
print(calcular_impuestos_v2(5000, 13, 10))
print(calcular_impuestos_v2(5000))
print(calcular_impuestos_v2(10, 15, 0))
