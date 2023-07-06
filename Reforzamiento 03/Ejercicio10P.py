import Ejercicio10M

##Llamado a la Función nombres_apellidos
nombre, apellido = Ejercicio10M.nombres_apellidos()
print(f"Nombres: {nombre}")
print(f"Apellidos: {apellido}")

##Llamado a la función tipo_seguro

tipo_seguro = Ejercicio10M.tipo_seguro()
print(f"Tipo de Seguro: {tipo_seguro} ")

##Llamado a la función mayor_edad

mayorEdad = Ejercicio10M.mayor_edad()
if mayorEdad:
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")



