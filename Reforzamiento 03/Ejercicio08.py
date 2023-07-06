class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, email, dni):
        contacto = {"Nombre": nombre, "Teléfono": telefono, "Email": email, "DNI": dni}
        self.contactos.append(contacto)

    def mostrar_contactos(self):
        for contacto in self.contactos:
            print(contacto)

    def buscar_contacto(self, dni):
        for contacto in self.contactos:
            if contacto["DNI"] == dni:
                print("\nContacto encontrado.")
                print(contacto)

agenda = Agenda()
agenda.agregar_contacto("José", "915456789", "jose@example.com", "45628973")
agenda.agregar_contacto("Luisa", "978753951", "luisa@example.com", "47895261")

agenda.mostrar_contactos()

agenda.buscar_contacto("45628973")
agenda.buscar_contacto("47895261")