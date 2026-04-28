"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""

import sys

try:
    total_load = float(sys.argv[1])
    num_supports = int(sys.argv[2])

    if num_supports == 0:
        print("Error: Cannot divide by zero! Supports must be greater than zero.")
    else:
        resultado = total_load / num_supports
        print(f"Load per support point: {resultado:.2f} N")

except:
    print("Error: Invalid input! Enter numeric values only.")