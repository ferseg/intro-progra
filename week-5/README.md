# Semana 5

## Operadores lógicos

| Operador | Descripción | Ejemplo |
|----------|-------------|---------|
|`and` | Returna `True` si los dos estatutos son `True`, de lo contrario, retorna `False` | `True and True = True`, `False and True = False` |
| `or` | Retorna `False` si los dos estatutos son `False`, de lo contrario, retorna `True` | `True or False = True`, `False or False = False` |
| `not` | Invierte el resultado lógico de un estatuto, si el estatuto es `True` al aplicar `not` se convierte en `False` y viceversa | `not True = False`

### Formas de uso de los operadores lógicos
Los operadores lógicos pueden ser utilizados para unir un conjunto de estatutos que su resultado es un valor lógico (boolean), por ejemplo:

#### Ejemplo de AND
```python
# Yo prodría preguntar si un número se encuentra 
# dentro de un rango específico de la siguiente forma

num = 35
# Como num se encuentra dentro del rango, es decir,
# es mayor a 10 y menor a 50, entonces imprime True
if num > 10 and num < 50:
    return True
```

#### Ejemplo de OR
```python
# Yo prodría preguntar si un string empieza con 
# un conjunto de caracteres específicos

str_1 = "885466"
# Como str_1 empieza con 8 entonces devolvería Kolbi
# otra forma que devuelva Kolbi es que empiece con 9
if str_1.startswith("8") or str_1.startswith("9"):
    return "Kolbi"
```

#### Ejemplo de NOT
```python
# Yo prodría preguntar si un string NO empieza con 
# un conjunto de caracteres específicos

str_1 = "885466"
# Como str_1 NO empieza con 8 entonces devolvería No es Kolbi
# otra forma que devuelva No Kolbi es que empiece con 9
if not(str_1.startswith("8") or str_1.startswith("9")):
    return "No es Kolbi"
```

## Referencias
 - [Python Strings](https://www.w3schools.com/python/python_strings.asp)
 - [Operadores logicos](https://www.w3schools.com/python/python_operators.asp)