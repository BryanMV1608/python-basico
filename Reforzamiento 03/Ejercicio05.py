import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

circulo1 = Circulo(float(input("Ingrese el radio del círculo 1: ")))
circulo2 = Circulo(float(input("Ingrese el radio del círculo 2: ")))

print(f"El área del círculo 1 es: {circulo1.area()}")
print((f"El perímetro del círculo 1 es: {circulo1.perimetro()}"))

print(f"El área del círculo 2 es: {circulo2.area()}")
print((f"El perímetro del círculo 2 es: {circulo2.perimetro()}"))