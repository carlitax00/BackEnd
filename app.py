# crear una función que permita ingresar al usuario nros enteros y strings
# 1. print -> imprime la lista que se fue cargando hasta el momento
# 2. append a, siendo a nro entero
# 3. remove b, siendo b nro entero
# 4. sort
# 5. reverse
# 6. insert c d, siendo ambos nros enteros; c el índice; d el valor
# 7. exit -> termina el programa

isRunning = True

myList = []

while isRunning:
    userInput = input("Ingrese comando: ")
    command = userInput.split() # split separa los elementos de una cadena de texto en una lista de varios elementos

    if command[0] == "exit":
        isRunning = False
    elif command[0] == "append":
        # quizás debamos hacer un chequeo del input para validar que el ingreso del dato es válido
        argumentos = command[1]
        if argumentos.isdigit():
            myList.append(int(argumentos))
    elif command[0] == "print":
        print(myList)
    elif command[0] == "sort":
        myList.sort()
    elif command[0] == "insert":
        myList.insert(int(command[1]), int(command[2]))
        # print("Se agregó ", command[2], " en el índice ", command[1])


# En javascript: las arrow functions, que son anónimas
# myFunction = (x) => x**2

# En Python:
myFunction = lambda x: x**2  # toma un parámetro (x), y devuelve un resultado (x**2)

