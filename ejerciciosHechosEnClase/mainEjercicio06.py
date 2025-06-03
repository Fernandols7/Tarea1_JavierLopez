# invocar la clase ejercicio06

from ejercicio06 import Compra2

precio = float(input("Ingrese el precio del producto: "))
cantidad = float(input("Ingrese la cantidad: "))

compra = Compra2(precio, cantidad)
compra.resultado()