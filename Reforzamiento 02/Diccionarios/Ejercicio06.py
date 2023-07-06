dict_1 = {"Nombre": "Bryan", "Edad": 30, "Salario": 1500, "Edad": 30}

dict_1["DNI"] = 48954632

del dict_1["Edad"]

##Se convierte en una lista

lista_1 = dict_1.items()

lista_1 = list(lista_1)
print(lista_1)

##Se convierte en un diccionario

dict_2 = dict(lista_1)

print(dict_2)



