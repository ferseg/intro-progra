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


## Variables globales
Las variables globales se definen en la raíz del archivo (al mismo nivel que se declaran las funciones), este tipo 
de variables puede ser utilizada dentro de cualquier función y su valor es compartido (entre todas las funciones que lo usen).

Para hacer uso de una variable global dentro de una función hay que usar la palabra reservada `global`

#### Ejemplo
```python
mi_var_global = 1

def incrementar_variable_global():
    global mi_var_global
    mi_var_global += 1

def imprimir_variable_global():
    global mi_var_global
    print(mi_var_global)

incrementar_variable_global()
incrementar_variable_global()
incrementar_variable_global()

# Esto va a imprimir 4, porque inicialmente la variable era 1
# como se llamó a incrementar 3 veces cada una de esas veces
# incrementó la variable en 1, a la hora de imprimir la variable es 4
imprimir_variable_global() 
```

## Listas
### Strings como listas
El string es una cadena de caracteres, cada caracter en el string se le asigna una posición de izquierda a derecha
empezando desde 0, esta posición es conocida como índice.

#### Operaciones sobre strings
Existen varias operaciones que se pueden realizar tanto en listas como en string, a continuación se ejemplifican algunas

- Obtener un segmento del string iniciando en el índice 0 y terminando en el índice x, el caracter en el índice x no va a ser incluido

```python
mi_str = "Hola mundo"
indice_x = 3
# Esto va a imprimir "Hol"
print(mi_str[:indice_x])
```

- Obtener un segmento del string iniciando en el índice x y terminando en el último caracter, el caracter en el índice x sí va a ser incluido

```python
mi_str = "Hola mundo"
indice_x = 3
# Esto va a imprimir "a mundo"
print(mi_str[indice_x:])
```

## Referencias
 - [Python Strings](https://www.w3schools.com/python/python_strings.asp)
 - [Operadores logicos](https://www.w3schools.com/python/python_operators.asp)