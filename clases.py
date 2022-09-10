class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return self.nombre + " " + str(self.edad)


persona1 = Persona("Juan", 20)
print(persona1)
persona2 = Persona("Pedro", 30)
persona3 = Persona("Ana", 40)
