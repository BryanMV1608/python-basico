import math
radio = 4.2
potencia = pow(radio,3)
volumen = 4 / 3 * math.pi * potencia
print("El volumen de una esfera de radio {} cm es {} cm3.".format(radio,round(volumen,4)))
