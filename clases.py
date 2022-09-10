class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido

    def __str__(self):
        return self.nombre + " " + str(self.edad) + " " + self.apellido


persona1 = Persona("Juan", 20)
print(persona1)
persona2 = Persona("Pedro", 30)
persona3 = Persona("Maria","Perez", 40)
