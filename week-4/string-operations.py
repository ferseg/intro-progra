# Modificar mayuscula minuscula
str1 = "un stRing"
str1_upper = str1.upper()
str1_lower = str1_upper.lower()

print(str1_upper)
print(str1_lower)

# Reemplazar algún caracter
str_repl1 = "Hola"
str_replaced = str_repl1.replace("H", "B")

print(str_replaced)

str_repl1 = "Hola"
str_replaced = str_repl1.replace("la", "C")

print(str_repl1)
print(str_replaced)

str_w_spaces = "  Un string  "
str_wo_spaces = str_w_spaces.strip().lower().replace("s", "p")

print(str_wo_spaces)


# Encontrar elemento dentro del string
# 0123456789
"Mi strings"


mi_str = "Mi string"
print(mi_str.find("s"))

# Si el string termina en un caracter especifico
print(mi_str.endswith("g"))

# Si el string empieza en un caracter especifico
print(mi_str.startswith("m"))


'''
Cree un programa para una operadora telefonica de CR,
la operadora quiere saber a qué compañía de teléfono pertenece un
número celular.
Las compañías son:
    - Si empieza con 8 o con 9 es de Kolbi
    - Si empieza con 6 es de Movistar
    - Si empieza con 7 es Claro
    - De lo contrario no pertenece a una compañía tica
'''


def identificador_compania(numero):
    if numero.startswith("9"):
        return "Kolbi"
    elif numero.startswith("8"):
        return "Kolbi"
    elif numero.startswith("7"):
        return "Claro"
    elif numero.startswith("6"):
        return "Movistar"
    else:
        return "No registrado"


print(identificador_compania("68888788"))
print(identificador_compania("98888788"))
print(identificador_compania("78888788"))
