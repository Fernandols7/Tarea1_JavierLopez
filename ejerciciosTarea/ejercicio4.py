import os
os.system('cls' if os.name == 'nt' else 'clear')

#  4. Número positivo, negativo o cero
#  Pide un número al usuario y muestra si es positivo, negativo o cero.


n = float(input("Ingrese un numero: "))
if n > 0:
    print(f"El numero {n} es positivo")
elif n < 0:
    print(f"El numero {n} es negativo")
else:
    print(f"El numero {n} es cero")