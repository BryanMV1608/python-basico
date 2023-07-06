class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def pagar_impuestos(self):
        if self.sueldo > 4000:
            impuesto = self.sueldo * 0.1
            print(f"El empleado {self.nombre} debe pagar {impuesto} de impuestos.")
        else:
            print(f"El empleado {self.nombre} no debe pagar impuestos.")

empleado1 = Empleado("Roberto", 30, 5000)
empleado1.pagar_impuestos()

empleado2 = Empleado("Jessica", 25, 3000)
empleado2.pagar_impuestos()
