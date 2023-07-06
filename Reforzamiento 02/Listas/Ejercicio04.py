lista_cursos = ["Biología", "Química", "Bioquímica", "Biotecnología", "Farmacotecnia", "Botánica"]

lista_cursos.append("Anatomía")
lista_cursos.append("Farmacología")
lista_cursos.append("Biofarmacia")
lista_cursos.append("Farmacognosia")

##Lista de cursos luego de usar función 'remove'

lista_cursos.remove("Química")
lista_cursos.remove("Biología")

##Invertimos los valores de la lista
lista_cursos.reverse()

print(lista_cursos)