#  2. Suma de dos números
#  Pide al usuario que ingrese dos números y muestra su suma.

import os
os.system('cls' if os.name == 'nt' else 'clear')


class Suma:
    def sumar(self):
        
        n1 = int(input("Ingrese el primer numero: "))
        n2 = int(input("Ingrese el segundo numero: "))
        suma = n1 + n2
        print(f"La suma de {n1} + {n2} es: {suma}")