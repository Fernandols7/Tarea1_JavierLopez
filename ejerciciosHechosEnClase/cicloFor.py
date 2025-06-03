import os
os.system('cls' if os.name == 'nt' else 'clear')

# Ciclo for

class CicloFor:
    def Ciclo(self):
        for i in range(1,11):
            print(i)

# Tabla de multiplicar 5

class TablaMultiplicar5:
    def Tabla(self):
        print("Tabla de multiplicar del 5")
        for i in range(1,11):
            print(f"5 X {i} = {i*5}")