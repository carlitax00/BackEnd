# Así se hacen los comentarios
""" estos se llaman docstring, para documentar funciones: al pasar el mouse por encima se puede ver el nombre de la función """

# import permite traer una biblioteca/paquete
import json
from src.utils import contarPares
from src.utils import comparoListas
# también se puede expresar como from src.utils import *


def sumar (a, b):
    """ Esto es un string para comentar ¿? """
    return a + b

def restar (a, b):
    return a - b

super_lista = [1, 2, 4, 5, 6, 7, 8, 9, 10]
print(3 in super_lista)
print(4 in super_lista)

count = 0
while count < 5:
    print(count)
    count = int(input("Ingrese un número: "))
print ("Fin del programa")

frontend_data = '{"name": "John", "age": 30, "city": "New York"}'

parsed_data = json.loads(frontend_data)

print(parsed_data)


# Tenemos como dato de entrada el día de hoy
today = "Lunes"

if today == "Viernes":
    print("Se viene el fin de semana...")
elif today == "Lunes":
    print("Se viene el día de trabajo...")
else:
    print("No se qué día es")


print("nes" in today) #evalúa si una cadena de texto está metida en today

lista_pares = [2,4,6,8,10]

lista_impares = [3] + lista_pares #agrega el 3 al comienzo de lista_pares

print (3 in lista_pares)


print(comparoListas(lista_pares, lista_impares))

listaA = [1,2,3,4,5]
listaB = [1,2,3,4,5]
matrix = [[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]]
print(matrix[1][3])

dias = ["Lunes", "Martes", "Miércoles"]
d1, d2, d3 = dias # asigna a las variables cada uno de los elementos de la lista
print (d1)
print (d2)
print (d3)

print(max(lista_impares))