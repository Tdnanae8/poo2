class Person():
    #__init__método que se llama cuando se crea el objeto.
    def __init__(self, name, lastname): 
        self.name = name
        self.lastname = lastname
persona1 = Person("JUANA", "DEL RIO")
print(persona1.name, persona1.lastname)

persona2 = Person("PATRICIO","ESTRELLA")
print(persona2.name, persona2.lastname)

persona3 = Person("BOB","ESPONJA")
print(persona3.name, persona3.lastname)

