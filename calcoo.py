#!/usr/bin/python3

import sys

from calc import Calculadora

c = Calculadora()

if __name__ == "__main__":
    try:
        op1 = int(sys.argv[1])
        op2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")
  
    if sys.argv[2] == "suma":
        c.plus(op1,op2)
    elif sys.argv[2] == "resta":
        c.minus(op1,op2)
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')
