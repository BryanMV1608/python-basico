
##Creación de la lista
lista_impar = []
for i in range(1,30):
    if i % 2 == 1:
        lista_impar.append(i)
print(lista_impar)


#Se agrega 3 números repetidos flotantes
lista_impar.append(3.5)
lista_impar.append(3.5)
lista_impar.append(3.5)
print(lista_impar)

##Se inserta una cadena
lista_impar.insert(3,"Impar")
print(lista_impar)


##Se elimina esa cadena
del lista_impar[3]
print(lista_impar)



