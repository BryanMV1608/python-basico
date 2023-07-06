class Persona:
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo

    def mostrar_datos(self):
        print("\nNombre:", self.nombre)
        print("Edad:", self.edad)
        print("Sueldo:", self.sueldo)

    def mayor_edad(self):
        if self.edad >= 18:
            print("Es mayor de edad.")
        else:
            print("No es mayor de edad.")

    def bonificacion(self):
        return self.sueldo * 0.2

persona1 = Persona("Rubén", 25, 5000)
persona1.mostrar_datos()
persona1.mayor_edad()
print(f"Su Bonificación es: {persona1.bonificacion()}")

persona2 = Persona("Zoila", 17, 1050)
persona2.mostrar_datos()
persona2.mayor_edad()
print(f"Su Bonificación es: {persona2.bonificacion()}")