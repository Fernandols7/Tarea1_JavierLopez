import os
os.system('cls' if os.name == 'nt' else 'clear')

#  10. Dibujo de asteriscos
#  Pide un número N y dibuja una línea de N asteriscos.

n = int(input("Ingrese un numero: "))
print("")   

for i in range(n):
    print("*", end = " ")