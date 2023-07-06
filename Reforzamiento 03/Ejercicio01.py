class Calculadora:
    def _init_(self, resultado):
        self.resultado = resultado

    def cubo(self, num):
        self.resultado = num ** 3

    def cuadrado_del_cubo(self):
        return self.resultado ** 2

calc = Calculadora()
num = int(input("Ingresa un número: "))
calc.cubo(num)
print(f"El cuadrado del cubo es: {calc.cuadrado_del_cubo()}")