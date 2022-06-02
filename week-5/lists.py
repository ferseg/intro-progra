def separar():
    print("=====================================")


'''
Posición = Índice

0  1  2  3  4  5  6  7  8  9
H  o  l  a  #  m  u  n  d  o

Str = cadena de caracteres
Lista de caracteres
Caracter = un elemento del string

Cuál es el caracter que está en la posición 6: u
Cuál es el caracter que está en la posición 8: d

Cuales elementos están después del indice 4: mundo
Cuales elementos están antes del indice 4: Hola
Cuales elementos están entre el indice 2 y 7: la#mun
'''
str_1 = "Hola#mundo"  # Cadena de caracteres

print("Caracter indice 6:", str_1[6])
print("Caracter indice 8:", str_1[8])
print("Caracter indice 3:", str_1[3])

separar()

# str[desde:hasta]
# si no tiene desde, entonces desde = 0
# si no tiene hasta, entonces hasta = final del str
print("Cuales elementos están después del indice 4:", str_1[5:])
print("Cuales elementos están antes del indice 4:", str_1[:4])
print("Cuales elementos están entre el indice 2 y 7:", str_1[2:8])

print(str_1[5:] + " " + str_1[:4])
