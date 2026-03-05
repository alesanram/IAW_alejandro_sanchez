'''
Ejercicio 1
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

Ejercicio 2
Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
'''

# Ejercicio 1
def ej1():
    nombre = input("Introduce tu nombre: ")
    n = int(input("Introduce un número entero: "))
    for _ in range(n):
        print(nombre)

ej1()

# Ejercicio 2
def ej2():
    nombre_completo = input("Introduce tu nombre completo: ")
    print(nombre_completo.lower())
    print(nombre_completo.upper())
    print(nombre_completo.title())

ej2()

# Ejercicio 3
def ej3():
    nombre = input("Introduce tu nombre: ")
    nombre_mayus = nombre.upper()
    numero_letras = len(nombre.replace(" ", ""))
    print(f"{nombre_mayus} tiene {numero_letras} letras")

ej3()