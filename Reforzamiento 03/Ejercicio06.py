class Alumno:
    def __init__(self, nombre, edad, nota_final):
        self.nombre = nombre
        self.edad = edad
        self.nota_final = nota_final

    def imprimir_datos(self):
        print("\nNombre:", self.nombre)
        print("Edad:", self.edad)
        print("Nota Final:", self.nota_final)

    def resultado_aprobacion(self):
        if self.nota_final >= 11:
            print("El alumno ha aprobado.")
        else:
            print("El alumno ha desaprobado")

alumno1 = Alumno("Juan", 20, 15)
alumno1.imprimir_datos()
alumno1.resultado_aprobacion()

alumno2 = Alumno("María", 22, 9)
alumno2.imprimir_datos()
alumno2.resultado_aprobacion()

alumno3 = Alumno("Carlos", 19, 12)
alumno3.imprimir_datos()
alumno3.resultado_aprobacion()