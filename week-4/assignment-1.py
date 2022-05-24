'''
1. Escriba un programa que reciba 2 números enteros y sume los últimos 2 dígitos 
de cada número entre sí.
Params:
    - num1: Es un número entero
    - num2: Es un número entero
Return:
    - La suma de los últimos 2 dígitos de cada número
Test cases:
    sumar_digitos_numeros(25, 27) # => (25 + 27) = 52
    sumar_digitos_numeros(5456, 786) # => (56 + 86) = 142
    sumar_digitos_numeros(135458, 5545) # => (58 + 45) = 103
    sumar_digitos_numeros(0, 1) # => (0 + 1) = 1
'''


'''
2. Escriba un programa que reciba un número entero, si el número recibido
es un multiplo de 2 (es decir el número par) elévelo al cubo (elevado a 3)
y devuelva el resultado de la operación
sino entonces eleve el número al cuadrado (elevado a 2) y devuelva el resultado
de la operación
Params:
    - num1: Es un número entero
Return:
    - Si el número es multiplo de 2, entonces el número elevado al cubo
    - Si el número no es múltiplo de 2, entonces el número elevado al cuadrado
Test cases:
    elevar_par_impar(2) # => Como 2 es multiplo de 2 (es decir par), entonces elevo al cubo 2 ** 3 = 8
    elevar_par_impar(3) # => Como 3 NO es multiplo de 2 (es decir impar), entonces elevo al cuadrado 3 ** 2 = 9
Tip:
    Para saber si un número es múltiplo de otro número, el residuo de la división de uno con el otro DEBE SER 0
'''


'''
3. Escriba un programa que reciba 2 strings, si el string 'a' tiene una longitud
mayor a la del string 'b' entonces retorne la concatenación de 'b' con 'a', sino retorne la
concatenación de 'a' con 'b'
Params:
    - str1: que es un string
    - str2: que es un string
Return:
    - La concatenación de a con b o de b con a dependiendo de las longitudes
Test cases:
    concatenar_strings_locos("Hola", "Mundo") # como la longitud (len) de b es mayor que a entonces retorna a con b = "Hola Mundo"
    concatenar_strings_locos("Holas!", "Mundo") # como la longitud (len) de a es mayor que b entonces retorna b con a = "Mundo Holas!"
    concatenar_strings_locos("Cuentos", "Largos") # => "Largos Cuentos"
'''
