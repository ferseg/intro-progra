'''
El nuevo gobierno de Costa Rica quiere validar la lista de números
de teléfonos y categorizarlos para tener un mejor control de las
compañías que utilizan los ticos, para esto, se requiere un programa
que reciba un número de teléfono valide el formato y devuelva a que
categoría y compañía pertenece.
Params:
    - numero: Es el número de teléfono a categorizar
Return:
    - Si el número de teléfono empieza con 2 o 4, el programa debe indicar "El número pertenece a un hogar".
    - Si el número empieza con 8 o 9, el programa debe indicar "El número pertenece a Kolbi Celular"
    - Si el número empieza con 7, el programa debe indicar "El número pertenece a Claro Celular"
    - Si el número empieza con 6, el programa debe indicar "El número pertenece a Movistar Celular"
    - Si el número no es válido el programa debe retornar "[!] Número invalido"
Validaciones: Se deben aplicar un conjunto de validaciones para saber que el
número ingresado pertenece a un número válido.
    - La longitud del número SIN guiones debe ser de 8 caracteres
Supuestos:
    - El numero ingresado es de tipo string
    - El número ingresado puede tener guiones o espacios, por ejemplo 88-88-88 88, eso se debería
    traducir a 88888888.
Tips:
    - Para quitar los caracteres especiales al número pueden utilizar la funcion de .replace()
Test Cases:
    - categorizar_numero("88-88 88-88") # => El número pertenece a Kolbi Celular
    - categorizar_numero("988 8 88-88") # => El número pertenece a Kolbi Celular
    - categorizar_numero("788888-88") # => El número pertenece a Claro Celular
    - categorizar_numero("6 88888-88") # => El número pertenece a Movistar Celular
    - categorizar_numero("6888 88-8") # => [!] Número invalido
    - categorizar_numero("26888 88-8") # => El número pertenece a un hogar
    - categorizar_numero("42888 88-8") # => El número pertenece a un hogar
'''
