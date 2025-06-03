# Escribe un programa que imprima en pantalla: "¡Hola, Mundo!"

import os
os.system('cls' if os.name == 'nt' else 'clear')


class Saludo:
    def holaMundo(self):
        print("¡Hola, Mundo!")