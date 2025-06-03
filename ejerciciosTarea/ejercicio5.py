import os
os.system('cls' if os.name == 'nt' else 'clear')

#  5. Par o impar
#  Pide un número y determina si es par o impar.

n = float(input("Ingrese un numero: "))
if n % 2 == 0:
    print(f"El numero {n} es par")
else:
    print(f"El numero {n} es impar")