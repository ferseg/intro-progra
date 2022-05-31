'''
1. Escriba un programa clasificador de frutas y verduras, el programa
debe recibir la fruta o verdura e indicar si es fruta o verdura según lo siguiente:
    - manzana, tomate, banano son frutas
    - brocoli, coliflor y zanahoria son verduras
Si la fruta o verdura no se encuentra registrada en el sistema debe retornar "No tenemos registro"
Params:
    - alimento: El alimento a clasificar, este alimento puede o no tener mayúsculas y minúsculas
Return:
    - "Fruta" si el alimento es manzana, tomate o banano
    - "Verdura" si el alimento es brocoli, coliflor o zanahoria
    - "No tenemos registro" en caso que no sea ninguna de las anteriores
Test cases:
    - clasificador_alimentos("BanaNo") # => "Fruta"
    - clasificador_alimentos("coliflor") # => "Verdura"
    - clasificador_alimentos("papaya") # => "No tenemos registro"
Tip: En el archivo de "string-operations.py" se encuentran funciones poner todo en mayúscula o minúscula
y así facilitar la comparación del alimento
'''


'''
2. Escriba un programa que me indique mi clasificación (bajo peso, normal, sobre peso, obeso) 
según mi IMC (Indice de masa corporal)
Param:
    - imc: El IMC
Return:
    - "Bajo peso" si el IMC es menor que 18.5
    - "Normal" si el IMC está entre 18.5 y 24.9
    - "Sobre peso" si el IMC está entre 25 y 29.9
    - "Obeso" si el IMC es mayor a 30
Test cases:
    - clasificador_imc(18) # => "Bajo peso"
    - clasificador_imc(23) # => "Normal"
    - clasificador_imc(29.9) # => "Sobre peso"
    - clasificador_imc(33.3) # => "Obeso"
'''


def clasificador_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobre peso"
    else:
        return "Obeso"


print(clasificador_imc(18))  # => "Bajo peso"
print(clasificador_imc(23))  # => "Normal"
print(clasificador_imc(29.9))  # => "Sobre peso"
print(clasificador_imc(33.3))  # => "Obeso"
print(clasificador_imc(25))  # => "Normal"

'''
3. Escriba un programa que reemplace las O por 0
si hubo algún reemplazo que imprima "Se reemplazaron las Os por 0s" y adicionalmente
imprima el nuevo string con los reemplazos
si no hubo reemplazo, entonces que imprima "No hubo reemplazos" y adicionalmente 
imprima el string original sin reemplazos
Param:
    - str: El string al cual se debe reemplazar las Os por 0s
Return
    - El string con los reemplazos si hubo alguno
    - El string sin los reemplazos si no hubo ninguno
Test cases:
    - reemplazas_os("Mi str") # => "No hubo reemplazos" "Mi str"
    - reemplazas_os("Yo sOy un str") # => "Se reemplazaron las Os por 0s" "Y0 s0y un str"
'''


'''
4. Escriba un programa que prediga el siguiente cambio de aceite del motor de un carro
dado la cantidad de km por semana.
Params:
    - km_por_semana: La cantidad de km que se usa el carro por semana
Return: 
    - La cantidad de meses para el siguiente cambio de aceite
Test case:
    - predecir_cambio_aceite(125) # => 10, Si uso el carro 125km por semana, en 10 meses deberia ser el siguiente cambio
    - predecir_cambio_aceite(500) # => 2.5, Si uso el carro 500km por semana, en 2.5 meses deberia ser el siguiente cambio
Tips (supuestos):
    - Un cambio de aceite se realiza cada 5000 km
    - Un mes está conformado por 4 semanas
'''


def predecir_cambio_aceite(km_por_semana):
    cant_semanas_para_cambio_aceite = 5000 / km_por_semana
    return cant_semanas_para_cambio_aceite / 4


# => 10, Si uso el carro 125km por semana, en 10 meses deberia ser el siguiente cambio
print(predecir_cambio_aceite(125))
# => 2.5, Si uso el carro 500km por semana, en 2.5 meses deberia ser el siguiente cambio
print(predecir_cambio_aceite(500))


'''
5. Escriba un programa que indique si el cambio de aceite de un carro se debe realizar por tiempo
o por cantidad de km.
Params:
    - km_por_semana: La cantidad de km por semana
Return:
    - "Cambio de aceite por tiempo", si el siguiente cambio de aceite se va a dar a mas de 6 meses
    - "Cambio de aceite por cantidad de km", si el siguiente cambio de aceite se va a dar en menos de 6 meses
Tip:
    - Para saber el siguiente cambio de aceite puede utilizar el programa desarrollado
    en el punto 4
'''


def indicar_razon_de_cambio_de_aceite(km_por_semana):
    siguiente_cambio = predecir_cambio_aceite(km_por_semana)
    if siguiente_cambio > 6:
        return "Cambio de aceite por tiempo"
    else:
        return "Cambio de aceite por cantidad de km"


print(indicar_razon_de_cambio_de_aceite(125))
print(indicar_razon_de_cambio_de_aceite(500))
