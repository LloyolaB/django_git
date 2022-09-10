class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido

    def __str__(self):
        return self.nombre + " " + str(self.edad) + " " + self.apellido


persona1 = Persona("Juan", 20)
persona2 = Persona("Pancho", 30)
persona3 = Persona("Ana", 40)


class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso

    def __str__(self):
        return super().__str__() + " " + self.curso


estudiante1 = Estudiante("Luis", 21, "GIT")
estudiante2 = Estudiante("Pedro", 31, "Python")

print(persona1)
print(estudiante1)
persona3 = Persona("Ana", 40)
persona3 = Persona("Maria", "Perez", 40)
