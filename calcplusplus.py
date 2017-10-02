#!/usr/bin/python3

import sys
import csv

if __name__ == "__main__":

    with open('fichero.csv','r') as f:

        reader = csv.reader(f)        

        for num in reader:

            if num[0] == "suma":
                resultado = int(num[1])
                if num[-1] == "":
                    for i in num[2:-1]:
                        resultado = resultado + int(i)
                    print(resultado)
                else:
                    for i in num[2:]:
                        resultado = resultado + int(i)
                    print(resultado)
            elif num[0] == "resta":
                resultado = int(num[1])
                if num[-1] == "":
                    for i in num[2:-1]:
                        resultado = resultado - int(i)
                    print(resultado)
                else:
                    for i in num[2:]:
                        resultado = resultado - int(i)
                    print(resultado)
            elif num[0] == "multiplica":
                resultado = int(num[1])
                if num[-1] == "":
                    for i in num[2:-1]:
                        resultado = resultado * int(i)
                    print(resultado)
                else:
                    for i in num[2:]:
                        resultado = resultado * int(i)
                    print(resultado)
            elif num[0] == "divide":
                try:
                    resultado = int(num[1])
                    if num[-1] == "":
                        for i in num[2:-1]:
                            resultado = resultado / int(i)
                        print(resultado)
                    else:
                        for i in num[2:]:
                            resultado = resultado / int(i)
                        print(resultado)
                except ZeroDivisionError:
                    sys.exit("Division by zero is not allowed")
            else:
                sys.exit('Operación sólo puede ser sumar, restar, multiplicar o dividir.')
