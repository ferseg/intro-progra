def separar():
    print("=====================================")


# Boolean = valor de verdad
# puede tener solo 2 posibles valores: Verdadero (True) o Falso (False)
mi_primer_boolean = True
mi_segundo_boolean = False

print(mi_primer_boolean)
print(mi_segundo_boolean)

separar()

print(type(mi_primer_boolean))
print(type(mi_segundo_boolean))

separar()

# Comparadores (comparar): Siempre retornan un valor de verdad (True, False)
# menor que: <
# mayor que: >
# igual: ==
# diferente: !=
# menor o igual: <=
# mayor o igual: >=

# Las funciones que devuelven un valor de verdad, deberían tener un
# nombre en forma de pregunta


def es_a_mayor_que_b(a, b):
    return a > b


def son_a_y_b_iguales(a, b):
    return a == b


# es_a_mayor_que_b(10, 25) => a = 10, b = 25 ==> False
print(es_a_mayor_que_b(10, 25))
# es_a_mayor_que_b(25, 10) => a = 25, b = 10 ==> True
print(es_a_mayor_que_b(25, 10))

separar()

print(son_a_y_b_iguales(10, 10))  # True
print(son_a_y_b_iguales(10, 11))  # False
print(son_a_y_b_iguales(1044, 1144))  # False

mi_str_1 = "Soy el string 1"
mi_str_2 = "Soy el string 2"

separar()

print(mi_str_1 == mi_str_2)
