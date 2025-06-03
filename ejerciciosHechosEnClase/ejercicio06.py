# Elaborar un programa que muestre el total de una compra de un solo producto 
# calculando el isv y dar un descuento solamente cuando el importe de la compra 
# sea mayor a 10,000 el descuento sera de un 25%

import os
os.system('cls' if os.name == 'nt' else 'clear')

class Compra2:
    def __init__(self, precio, cantidad):
        self.precio = precio
        self.cantidad = cantidad

    def cal_subtotal(self):
        return self.precio * self.cantidad

    def cal_descuento(self, subtotal):
        if subtotal >= 10000:
            descuento = subtotal * 0.25
            subtotal -= descuento
            print(f"Descuento: L. {descuento}")
        else:
            descuento = 0
        return subtotal, descuento

    def cal_isv(self, subtotal):
        return subtotal * 0.15

    def cal_total(self):
        subtotal = self.cal_subtotal()
        subtotal, descuento = self.cal_descuento(subtotal)
        isv = self.cal_isv(subtotal)
        total = subtotal + isv
        return subtotal, isv, total

    def resultado(self):
        subtotal, isv, total = self.cal_total()
        print(f"\nSubtotal: L. {subtotal}")
        print(f"ISV: L. {isv}")
        print(f"Total a pagar: L. {total}")