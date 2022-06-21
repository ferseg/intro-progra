'''
1. Escriba un programa que cuente la cantidad de veces que un elemento
aparece en una lista.
Params:
    - elements: la lista de elementos
    - search_el: el elemento a contar
Return:
    - La cantidad de veces que el elemento aparece en la lista
Test cases:
    - contar_apariciones([1,2,3,4,5,4,5,4,4], 4) # => 4, el 4 aparece 4 veces
    - contar_apariciones([1,2,3,4,5,4,5,4,4], 5) # => 2, el 5 aparece 2 veces
    - contar_apariciones([1,2,3,4,5,4,5,4,4], 10) # => 0, el 10 aparece 0 veces
    - contar_apariciones(["Fer", "Meli"], "Fer") # => 1
'''


'''
2. Escriba un programa que retorne el o los índice (en base 0) en que se
encuentra un elemento, si el elemento aparece más de una vez debe retornar todas
las posiciones
Params:
    - elements: la lista de elementos
    - search_el: el elemento a buscar el indice
Return:
    - Los índices en donde se encontró los elementos
Test cases:
    - buscar_indices([1,2,3,4,5,4,5,4,4], 4) # => [3,5,7,8]
    - buscar_indices([1,2,3,4,5,4,5,4,4], 10) # => []
'''


'''
3. En la escuela X están requiriendo un programa que saque el promedio de notas
de un grupo específico, escriba un programa para la escuela X
Params:
    - grades: una lista de notas
Return:
    - El promedio de notas del grupo
Test case:
    - sacar_promedio([70,70,60]) # => 66.66
    - sacar_promedio([70,70,70]) # => 70
'''


'''
4. El parque nacional Manuel Antonio está requiriendo un programa que indique los tipos de
aves que tiene en común con el parque nacional Rincón de la Vieja.
Params:
    - bird_types_ma: Una lista de numeros enteros, donde cada uno de los enteros es un tipo de ave
    en el parque Manuel Antonio
    - bird_types_rv: Una lista de numeros enteros, donde cada uno de los enteros es un tipo de ave
    en el parque Rincón de la vieja
Return:
    - La lista de aves en común entre el el parque Manuel Antonio y Rincón de la Vieja
Test cases:
    - sacar_comunes([1,1,2,2,3], [4,5,2,1,1]) # => [1,2]
    - sacar_comunes([1,1,2,2,3], [4,5,2,10,11]) # => [2]
    - sacar_comunes([1,1,2,2,3], [4,5,20,10,11]) # => []
'''
