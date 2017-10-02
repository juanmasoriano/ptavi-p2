#!/usr/bin/python3

import sys


if __name__ == "__main__":
    fichero = open("Fichero.txt","w")
    fichero.write("suma,2,20,10,4,\nresta,15,10,5,\nmultiplica,1,1,5,3,2,\ndivide,80,2,0,1")
    fichero.close()

    fichero = open("Fichero.txt","r")

    for linea in fichero:
        num = linea.split(",")

        if num[0] == "suma":
            resultado = int(num[1])
            for i in num[2:-1]:
                resultado = resultado + int(i)
            print(resultado)
        elif num[0] == "resta":
            resultado = int(num[1])
            for i in num[2:-1]:
                resultado = resultado - int(i)
            print(resultado)
        elif num[0] == "multiplica":
            resultado = int(num[1])
            for i in num[2:-1]:
                resultado = resultado * int(i)
            print(resultado)
        elif num[0] == "divide":
            try:
                resultado = int(num[1])
                for i in num[2:-1]:
                    resultado = resultado / int(i)
                print(resultado)
            except ZeroDivisionError:
                sys.exit("Division by zero is not allowed")

        else:
            sys.exit('Operación sólo puede ser sumar, restar, multiplicar o dividir.')
