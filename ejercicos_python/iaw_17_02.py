# Ejercicio 1
# Crear una lista de 10 elemento donde se pide por teclado los valores y los elementos de la lista debe de ser en orden ascendente 
#-----------------------------------------------------

def crearLista(listy):
    cont=0
    while cont < 10:
        try:
            value = int(input(f'Introduce el Valor del elemento # {cont + 1} '))
            if( len(listy) >= 1):
                if(listy[(cont - 1)] <= value):
                    listy.append(value)
                    cont+=1
                else:
                    print(f'El valor debe de ser mayor o igual al anterior({listy[(cont -1)]})\n')
            else:
                listy.append(value)
                cont+=1
        except ValueError:
            print(f'El valor es incorrecto, No es un numero entero\n')
    return listy



lista=[]
result=crearLista(lista)

print(f'La lista es de {result}')
#-----------------------------------------------------
# Ejercicio 2
# Crear una lista de lista de 5 lista como en el ejercio anterior
#-----------------------------------------------------
def superLista():
    super=[]
    for i in range(5):
        item= crearLista([])
        super.append(item)

superLista()