# Condicionales en python

import os
os.system('cls' if os.name == 'nt' else 'clear')


class Condicionales:
    def condicion(self):
        a = float(input("Ingrese un numero: "))
        if a % 2 == 0:
            print(f"{a} es par")
            if a == 0:
                print("No se puede dividir")
            else:
                print(f"{a} es par")
        else:
            print(f"{a} es impar")