
def separar():
    print("=====================================")


separar()

mi_var = "Hola, estoy haciendo un string extenso"

# len(x) => tamaño del str
len_del_var = len(mi_var)  # int
print(len_del_var > 5)


separar()

# if True:
# else:
if len_del_var > 5:  # True
    print("La longitud es mayor que 5")
    print("Otra cosa")
else:  # Sino
    print("La longitud es menor o igual que 5")


separar()


mi_var = "Hola"

len_del_var = len(mi_var)  # int

# elif
# si el if es Falso => ??
if len_del_var > 5:  # True
    print("La longitud es mayor que 5")
elif len_del_var == 5:
    print("La longitud es 5")
else:
    print("La longitud es menor que 5")


separar()

# Programa que reciba un string y un numero que va a ser la longitud deseada
# Imprimir:
#    "Si" si la longitud del string es mayor o igual que la longitud deseada
#    "No" si la longitud del string es menor que la longitud desada
# Corrida de ejemplo
# tiene_longitud_deseada("Mi string", 5)


def tiene_longitud_deseada(str, long_deseada):
    len_str = len(str)
    if len_str >= long_deseada:
        print("Si")
    else:
        print("No")


tiene_longitud_deseada("Mi string", 15)
tiene_longitud_deseada("Mi string", 3)
tiene_longitud_deseada("Mi string", 14)
tiene_longitud_deseada("Mi string", 1)

separar()

# Programa que retorne los 2 últimos dígitos de un número si los (if) dígitos son
# mayores a 25, sino (else) que devuelva -1
# Params
#    - El numero al cual le voy a sacar los últimos 2 dígitos
# Return
#    - Los últimos 2 dīgitos, si estos son mayor a 25
#    - -1 en otro caso
# Example:
#    obtener_ultimos_digitos(1258) => 58
#    obtener_ultimos_digitos(1200) => -1
#    obtener_ultimos_digitos(1324) => -1
1258 // 100  # = 12
1258 % 100  # = 58


def obtener_ultimos_digitos(num):
    res = num % 100
    if res > 25:
        return res
    else:
        return -1


print(obtener_ultimos_digitos(1258))  # => 58
print(obtener_ultimos_digitos(1200))  # => -1
print(obtener_ultimos_digitos(1324))  # => -1


separar()

# Escriba un programa que me de los úlimos "n" digitos de un número
# Params
#    - un numero entero: El número al cual le voy a sacar los dígitos
#    - un numero entero: que es la cantidad de dígitos que debo sacar al número
# Return
#    - Los últimos n digitos
# Test case:
#    sacar_n_dig(num, n)
#    sacar_n_dig(12544, 1) => 4
#    sacar_n_dig(12544, 3) => 544
#    sacar_n_dig(2, 5) => 2
#    sacar_n_dig(2, 0) => 0


def elevar(num, pot):
    return num ** pot


def sacar_n_dig(num, n):
    if n == 0:
        return -1
    elif num < 10:
        return num
    else:
        dividendo = elevar(10, n)
        residuo = num % dividendo
        return residuo


print(sacar_n_dig(544, 1))
print(sacar_n_dig(12544, 3))
print(sacar_n_dig(2, 5))
