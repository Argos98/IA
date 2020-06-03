class Persona:
    
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido 

    def saludar_otro(self, persona):
        return f'Hola {persona.nombre}, me llamo {self.nombre}'




david = Persona('David','Serrano')
alberto = Persona('Alberto','Feroz')

print(david.saludar_otro(alberto))