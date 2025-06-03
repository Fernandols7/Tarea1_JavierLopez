#  6. Mayor de tres números
#  Pide tres números al usuario y muestra cuál es el mayor.

import os
os.system('cls' if os.name == 'nt' else 'clear')

class Mayor:
    def nMayor(self):
        n1 = float(input("Ingrese el primer numero: "))
        n2 = float(input("Ingrese el segundo numero: "))
        n3 = float(input("Ingrese el tercer numero: "))

        if n1 > n2 and n1 > n3:
            print(f"El numero mayor es: {n1}")
        elif n2 > n1 and n2 > n3:
            print(f"El numero mayor es: {n2}")
        elif n3 > n1 and n3 > n2:
            print(f"El numero mayor es: {n3}")
        elif n1 == n2 and n1 > n3:
            print(f"Los numeros mayores son: {n1} y {n2}")
        elif n1 == n3 and n1 > n2:
            print(f"Los numeros mayores son: {n1} y {n3}")
        elif n2 == n3 and n2 > n1:  
            print(f"Los numeros mayores son: {n2} y {n3}")   
        else:
            print(f"Todos los numeros son iguales")