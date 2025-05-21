import os
os.system('cls' if os.name == 'nt' else 'clear')

# 8. Tabla de multiplicar
# Pide un número y muestra su tabla del 1 al 10.

n = int(input("Ingrese un numero: "))
print("")
print(f"Tabla de multiplicar del {n}")

for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")