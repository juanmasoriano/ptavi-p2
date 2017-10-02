#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Calculadora:

    def plus(self, op1, op2):
        """ Function to sum the operands. Ops have to be ints """
        print(op1 + op2)

    def minus(self, op1, op2):
        """ Function to substract the operands """
        print(op1 - op2)

class CalculadoraHija(Calculadora):

    def multiplicacion(self,op1,op2):
        print(op1 * op2)

    def division(self,op1,op2):
        print(op1 / op2)

if __name__ == "__main__":
    
    c = Calculadora()
    
    try:
        op1 = int(sys.argv[1])
        op2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        c.plus(op1, op2)
    elif sys.argv[2] == "resta":
        c.minus(op1, op2)
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')
