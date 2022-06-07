from os import sep


def separar():
    print("=====================================")


'''
Una lista es similar a un contenedor de elementos
un str => cadena de textos
una lista => cadena de elementos
- Se representan con los elementos separados por una coma y todo 
contenido en paréntesis cuadrados
- Al igual que los strs las listas tienen índices y el primer índice
es el 0 (los indices empiezan en 0)
- Acceder a un índice se hace de igual forma que en un str
'''
lista_vacia = []

lista_ints = [1, 2, 3]

print(lista_ints[1])

# Convertir string a lista con split

str1 = "Hola mundo soy Fernando"
list_str1 = str1.split()
print(list_str1)
print(str1[3])
print(list_str1[3])

separar()

str2 = "Hola"
list_str2 = list(str2)
print(list_str2)

separar()
list_str3 = ["quien", "quiere", "ser", "millonario"]
str3 = " ".join(list_str3)
print(list_str3)
print(str3)

separar()
'''
Cree un programa que remueva la primera palabra de un string
Params:
    - un string
Return:
    - el string sin la primera palabra
Hechos:
    - Cada palabra del string está separada por un espacio
Test cases:
    - remover_palabra("Hola mundo") # => mundo
    - remover_palabra("Quiero comer algo") # => comer algo
'''


def remover_palabra(palabra):
    palabra_list = palabra.split()
    palabra_wo_1 = palabra_list[1:]
    return " ".join(palabra_wo_1)


print(remover_palabra("Hola mundo"))

separar()

# Obtener el último elemto de una lista
my_list = [1, 2, 3, 4, 5, 6, 10]
print(my_list[-1])
print("Mi lista contiene", len(my_list))
last_idx = len(my_list) - 1
print(my_list[last_idx])

separar()
'''
Cree un programa que remueva la ultima palabra de un string
Params:
    - un string
Return:
    - el string sin la ultima palabra
Hechos:
    - Cada palabra del string está separada por un espacio
Test cases:
    - remover_palabra("Hola mundo") # => Hola
    - remover_palabra("Quiero comer algo") # => Quiero comer
'''


def remover_palabra2(palabra):
    palabra_list = palabra.split()
    palabra_wo_1 = palabra_list[:-1]
    return " ".join(palabra_wo_1)


print(remover_palabra2("Hola mundo"))

'''
 0  1  2  3
[1, 2, 3, 4]
-4 -3 -2 -1

l[-1]
l[3]

split(separador)
Un str => list especificando un separado

split() => separador = " " => split(" ")
str1 = "un#string#encriptado"
list1 = str1.split("#") => ["un", "string", "encriptado"]
list2 = str1.split("i") => ["un#str", "ng#encr", "ptado"]
str2 = " ".join(list1) => "un string encriptado"

'''
separar()
str1 = "un#string#encriptado"
list1 = str1.split("#")  # => ["un", "string", "encriptado"]
print(list1)
list2 = str1.split("i")  # => ["un#str", "ng#encr", "ptado"]
print(list2)
str2 = " ".join(list1)  # => "un string encriptado"
print(str2)
str3 = "/-/".join(list1)
print(str3)

# Concatenar listas
separar()
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2

print(list1)
print(list2)
print(list3)

# Añadir un elemento a la lista
list4 = [1, 3, 8]
num = 5
list5 = list4 + [num]
print(list5)

list6 = [1, 3, 8]
num_str = "5"
list7 = list4 + [num_str]
print(list7)

separar()
print(list1[:-1] + list2[1:])
# Añadir un elemento a la lista con append
