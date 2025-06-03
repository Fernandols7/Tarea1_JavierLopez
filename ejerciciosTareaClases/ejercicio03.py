# # 3. Calculadora de área de un rectángulo
#  Pide la base y altura, y muestra el área. Fórmula: área = base × altura

import os
os.system('cls' if os.name == 'nt' else 'clear')

class areaRectangulo:
    def calArea(self):
        base = float(input("Ingresa la base del rectangulo: "))
        altura = float(input("Ingresa la altura del rectangulo: "))
        area = base * altura
        print(f"El area del rectangulo es: {area}")