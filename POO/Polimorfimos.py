class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('estoy caminando')


class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('ando en bicicleta')


def main():

    perso1 = Persona('David') 
    perso1.avanza

    ciclista = Ciclista('Pepe')     
    ciclista.avanza

if __name__ == '__main__':
    main()
