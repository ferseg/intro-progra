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

print(str_replaced)

str_w_spaces = "  Un string  "
str_wo_spaces = str_w_spaces.strip().lower().replace("s", "p")

print(str_wo_spaces)
