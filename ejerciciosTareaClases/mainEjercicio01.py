# Invocar a la clase ejercicio01

import os
os.system('cls' if os.name == 'nt' else 'clear')

from ejercicio01 import Saludo

s = Saludo()
s.holaMundo()