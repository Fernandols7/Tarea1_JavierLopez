# Operaciones aritmeticas con funciones

import os
os.system('cls' if os.name == 'nt' else 'clear')

class FuncionesAritmeticas:

    def suma(self, a,b):
        return a+b

    # Resta
    def resta(self, a,b):
        return a-b

    # Multiplicacion
    def multi(self, a,b):
        return a*b

    # Division
    def division(self, a,b):
        return a/b

    # Potencia
    def potencia(self, a,b):
        return a**b

    # Raiz cuadrada
    def raiz(self, a):
        if a < 0:
            return "Error: raiz negativa"
        return a ** 0.5