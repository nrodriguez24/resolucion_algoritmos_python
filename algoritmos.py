import os

def ocurrencias(cadena):
    palabras=cadena.split() #funcion que crea una lista usando los string separados por un espacio en blanco.
    dicc={}
    for palabra in palabras:
        for letra in palabra:
            if letra in dicc:
                dicc[letra]+= 1
            else:
                dicc[letra]=1
    return dicc

def evaluar(numero):
    if int(numero) > 0:
        return("El número es positivo (+)")
    elif int(numero) == 0:
        return("El número es igual a cero (0)")
    else:
        return("El número es negativo (-)")

while True: 
    
    print("---1--- Contar el numero de ocurrencias de cada letra de una frase ingresada por usuario.\n---2--- Ingresar un numero para saber si es (+,-,0) \n---3--- Ingresar números para saber su sumatoria y promedio \n---4--- Ingresar un número para sumar sus digitos \n---5--- Salir del programa")

    opcion=int(input("+++ Ingrese la opción elegida: "))

    if opcion == 1:
        var=input("Por favor escriba una oracion: ")
        freA=ocurrencias(var)
        print("Las palabras y el número de ocurrencias de cada una es: ")
        print(freA)

    elif opcion == 2:
        while True:
            numero=input("Ingrese el número que será evaluado: ")
            print("Para finalizar el ingreso coloque un asterisco *")
            if numero == "*":
                break 
            else:
                resultado= evaluar(numero)
                print(resultado)

    elif opcion == 3:
        lista=[]
        sumatoria=0
        while True:
            num= int(input("Ingrese un número, finalizará cuando ingrese un cero (0): "))
            if num == 0:
                break
            else: 
                lista.append(num)
        for i in lista:
            sumatoria+= i
        print(f"La sumatoria de los números guardados en la lista es igual a {sumatoria}. Y el promedio de los números es {sumatoria/len(lista)}")

    elif opcion == 4:
        sum=0
        ingresar=input("Por favor ingrese un número: ")
        for i in ingresar:
            sum += int(i)
        print(f"La sumatoria de los digitos del numero {ingresar} es {sum}")

    elif opcion == 5:
        break

    else:
        print("--> POR FAVOR ELIGA UNA OPCION QUE SE ENCUENTRE EN EL MENÚ")
    
    c = input("Presione Enter para continuar...")
    c = os.system('cls' if os.name == 'nt' else 'clear')