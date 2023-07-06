class Cadena:
    def revertir_palabras(self, cadena):
        palabras = cadena.split()
        palabras.reverse()
        return " ".join(palabras)

cadena = "Hola Pythonista, seguimos adelante"
cadena_obj = Cadena()
resultado = cadena_obj.revertir_palabras(cadena)
print(resultado)
resultado = cadena_obj.revertir_palabras(cadena)
print(resultado)
