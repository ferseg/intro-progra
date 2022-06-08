# Semana 6
## Listas
Las listas es una estructura que puede contener información de diferentes tipos de datos, cada uno de los elementos de la lista
está separado por una coma `,` y los elementos deben estar contenidos entre paréntesis cuadrados `[]`.

Ejemplo:
```python
# Lista que contiene un string, un entero, un float y un boolean
soy_una_lista = ["elemento", 4, 5.5, True]
```

### Índices
A cada uno de los elementos en la lista se les asigna una posición o índice, este es un número consecutivo que empieza en 0,
además se puede obtener el elemento específicando el índice del mismo

Ejemplo:
```python
mi_lista = [1, 2, 3]
print(mi_lista[0]) # => Imprime 1
print(mi_lista[1]) # => Imprime 2
print(mi_lista[2]) # => Imprime 3
```

#### Sublistas
Se pueden obtener una sub-lista a partir de una lista con operaciones sobre los índices, la notación es `[desde:hasta]` donde el `desde`
es inclusivo y el `hasta` exclusivo, es decir el indice en la posición `desde` va a ser incluido en la sub lista pero el elemento que
se encuentra en la posición `hasta` no va a ser incluido en la sub lista

Ejemplo
```python
mi_lista = [1, 2, 3, 4, 5, 6, 7]
# La sub lista contiene desde el índice 2 hasta el 4, el 5 se omite
sub_lista = mi_lista[2:5]
print(sub_lista) # => [3, 4, 5]

sub_lista = mi_lista[:5]
# Se incluyen todos los elementos desde el inicio hasta el índice 4
print(sub_lista) # => [1,2, 3, 4, 5]

sub_lista = mi_lista[2:]
# Se incluyen todos los elementos desde el índice 2 hasta el último elemento
print(sub_lista) # => [3, 4, 5, 6, 7]
```

### Longitud de una lista
Para determinar la longitud de una lista se utiliza la función `len` por ejemplo `len(mi_lista)` en el ejemplo anterior sería 3
porque contiene 3 elementos

### Concatenar listas
Usando el operador de suma `+` se pueden concatenar una o más listas

Ejemplo:
```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
print(lista1 + lista2) # => [1, 2, 3, 4, 5, 6]
```

