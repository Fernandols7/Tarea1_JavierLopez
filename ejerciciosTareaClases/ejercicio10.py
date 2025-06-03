#  10. Dibujo de asteriscos
#  Pide un número N y dibuja una línea de N asteriscos.

import os
os.system('cls' if os.name == 'nt' else 'clear')

class Asteriscos:
    def MostrarAsteriscos(self):
        n = int(input("Ingrese un numero: "))
        print("")

        for i in range(n):
            print("*", end = " ")