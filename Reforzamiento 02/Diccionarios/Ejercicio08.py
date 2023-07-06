dict_depart = {"D1": "lima", "D2": "Arequipa", "D3": "Junin", "D4": "Cuzco", "D5": "Ica", "D6": "Puno"}

##Se elimina el ítem "D2"
del dict_depart["D2"]

##Se agrega otro ítem "Profesión"
dict_depart["Profesion"] = "Quimico Farmaceutico"

##Se imprimen los valores del diccionario
for key, value in dict_depart.items():
    print(key, value)
