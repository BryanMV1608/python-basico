class DatosPersonales:
    def _init_(self):
        self.nombre = None
        self.apellido = None
        self.edad = None

    def ingresar_nombre_apellido(self):
        self.nombre = input("Ingrese su nombre: ")
        self.apellido = input("ingrese su apellido: ")

    def ingresar_edad(self):
        self.edad = input("Ingrese su edad: ")

    def imprimir_resultados(self):
        resultados = {"Nombre" : self.nombre, "Apellido" : self.apellido, "Edad" : self.edad}
        print(resultados)

datos = DatosPersonales()
datos.ingresar_nombre_apellido()
datos.ingresar_edad()
datos.imprimir_resultados()