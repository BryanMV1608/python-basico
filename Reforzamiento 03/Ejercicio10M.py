def nombres_apellidos():
    nombre = input("Ingrese su nombre: ")
    apellido = input("ingrese su apellido: ")
    return nombre, apellido

def tipo_seguro():
    seguro = input("Ingrese el tipo de seguro al que se encuentra afiliado: ")
    return seguro

def mayor_edad():
    edad = int(input("Ingrese su edad: "))
    if edad >= 18:
        return True
    else:
        return False