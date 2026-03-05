'''
Ejercicio 1
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

Ejercicio 2
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

Ejercicio 3
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
Fruta 	Precio
Plátano 	1.35
Manzana 	0.80
Pera 	0.85
Naranja 	0.70

Ejercicio 4
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
'''

# Ejercico1

def ej1():
    divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

    moneda = input("Introduce una divisa: ")

    if moneda in divisas:
        print("El símbolo es:", divisas[moneda])
    else:
        print("La divisa no está en el diccionario")

ej1()

#Ejercico2

def ej2():
    nombre = input("Introduce tu nombre: ")
    edad = input("Introduce tu edad: ")
    direccion = input("Introduce tu dirección: ")
    telefono = input("Introduce tu teléfono: ")

    persona = {
        "nombre": nombre,
        "edad": edad,
        "direccion": direccion,
        "telefono": telefono
    }

    print(persona["nombre"], "tiene", persona["edad"], "años, vive en", persona["direccion"], "y su número de teléfono es", persona["telefono"])

ej2()

#Ejercico3

def ej3():
    frutas = {
        "Plátano": 1.35,
        "Manzana": 0.80,
        "Pera": 0.85,
        "Naranja": 0.70
    }

    fruta = input("Introduce una fruta: ")
    kilos = float(input("Introduce el número de kilos: "))

    if fruta in frutas:
        precio = frutas[fruta] * kilos
        print("El precio es:", precio, "€")
    else:
        print("La fruta no está en el diccionario")

ej3()

#Ejercico4

def ej4():
    meses = {
        "01": "enero",
        "02": "febrero",
        "03": "marzo",
        "04": "abril",
        "05": "mayo",
        "06": "junio",
        "07": "julio",
        "08": "agosto",
        "09": "septiembre",
        "10": "octubre",
        "11": "noviembre",
        "12": "diciembre"
    }

    fecha = input("Introduce una fecha (dd/mm/aaaa): ")

    dia, mes, año = fecha.split("/")

    print(dia, "de", meses[mes], "de", año)

ej4()