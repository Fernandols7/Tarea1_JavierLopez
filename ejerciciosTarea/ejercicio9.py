import os
os.system('cls' if os.name == 'nt' else 'clear')

#  9. Sumar los primeros N números
#  Pide un número N y muestra la suma del 1 hasta N.

n = int(input("Ingrese un numero: "))
suma = 0

for i in range(1, n + 1):
    suma += i

print(f"La suma de los primeros {n} numeros es: {suma}")
