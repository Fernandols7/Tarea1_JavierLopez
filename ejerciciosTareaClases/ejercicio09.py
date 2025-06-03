#  9. Sumar los primeros N números
#  Pide un número N y muestra la suma del 1 hasta N.

import os
os.system('cls' if os.name == 'nt' else 'clear')


class SumaNumeros:
    def num(self):
        n = int(input("Ingresa un numero: "))
        suma = 0

        for i in range(1, n + 1):
            suma += i

        print(f"La suma de los primeros {n} numeros es: {suma}")