import math

'''
Ejercicio 1
Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.

Ejercicio 2
Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, tangente, exponencial y logaritmo neperiano. La función preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla con los enteros de 1 al valor introducido y el resultado de aplicar la función a esos enteros.

Ejercicio 3
Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.

Ejercicio 4
Escribir una función que reciba otra función booleana y una lista, y devuelva otra lista con los elementos de la lista que devuelvan True al aplicarles la función booleana.

Ejercicio 5
Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.
'''
# EJERCICIO 1
def aplicar_descuento(precio, porcentaje):
    return precio - precio * porcentaje / 100

def aplicar_iva(precio, porcentaje):
    return precio + precio * porcentaje / 100

def calcular_cesta(cesta, funcion):
    total = 0
    for (precio, porcentaje) in cesta.items():
        total += funcion(precio, porcentaje)
    return total

cesta = {
    "pan": (1.2, 10),
    "leche": (0.9, 5),
    "huevos": (2.5, 8)
}

print("Total con descuento:", calcular_cesta(cesta, aplicar_descuento))
print("Total con IVA:", calcular_cesta(cesta, aplicar_iva))

# EJERCICIO 2
def calculadora_cientifica():
    valor = int(input("Introduce un número entero: "))
    funcion = input("Introduce la función (sin, cos, tan, exp, log): ")

    funciones = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "exp": math.exp,
        "log": math.log
    }

    if funcion not in funciones:
        print("Función no válida")
        return

    print("\nTabla de resultados")
    for i in range(1, valor + 1):
        print(i, funciones[funcion](i))

calculadora_cientifica()

# EJERCICIO 3
def aplicar_funcion(funcion, lista):
    resultado = []
    for i in lista:
        resultado.append(funcion(i))
    return resultado

lista = [1, 2, 3, 4]
print("Cuadrados:", aplicar_funcion(lambda x: x**2, lista))

# EJERCICIO 4
def filtrar_lista(funcion_booleana, lista):
    resultado = []
    for i in lista:
        if funcion_booleana(i):
            resultado.append(i)
    return resultado

print("Pares:", filtrar_lista(lambda x: x % 2 == 0, lista))

# EJERCICIO 5
def palabras_longitud(frase):
    palabras = frase.split()
    diccionario = {}

    for palabra in palabras:
        diccionario[palabra] = len(palabra)

    return diccionario


frase = "hola mundo python"
print("Diccionario:", palabras_longitud(frase))