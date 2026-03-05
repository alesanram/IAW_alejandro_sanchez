'''
Ejercicio 1 
Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, done n es el número introducido. 
Ejercicio 2 
Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, done n es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello. 
Ejercicio 3 
Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
'''

def guardar_tabla():
    n = int(input("Introduce un número entre 1 y 10: "))

    if 1 <= n <= 10:
        nombre_fichero = f"tabla-{n}.txt"

        with open(nombre_fichero, "w") as fichero:
            for i in range(1, 11):
                fichero.write(f"{n} x {i} = {n*i}\n")

        print("Tabla guardada en", nombre_fichero)
    else:
        print("Número fuera de rango")

guardar_tabla()

def mostrar_tabla():
    n = int(input("Introduce un número entre 1 y 10: "))
    nombre_fichero = f"tabla-{n}.txt"

    try:
        with open(nombre_fichero, "r") as fichero:
            print("\nTabla de multiplicar:")
            print(fichero.read())
    except FileNotFoundError:
        print("El fichero no existe.")

mostrar_tabla()

def mostrar_linea():
    n = int(input("Introduce un número entre 1 y 10: "))
    m = int(input("Introduce la línea que quieres ver (1-10): "))

    nombre_fichero = f"tabla-{n}.txt"

    try:
        with open(nombre_fichero, "r") as fichero:
            lineas = fichero.readlines()

            if 1 <= m <= len(lineas):
                print("\nResultado:")
                print(lineas[m-1])
            else:
                print("Línea fuera de rango.")
    except FileNotFoundError:
        print("El fichero no existe.")

mostrar_linea()