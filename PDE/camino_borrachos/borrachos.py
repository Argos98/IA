#esta liberia nos permtie hacer el ramdom 
import random


class Borracho:

    #esta clase solo tiene nombre como paremetro de creacion en su constructor 
    def __init__(self, nombre):
        self.nombre = nombre

#esta clase es hija de borracho(herencia)
class BorrachoTradicional(Borracho):

#este constructo lo mismo que su padre(borracho)
    def __init__(self, nombre):
        super().__init__(nombre)
    #esta funcion es la que escoje hacia que direcion moverse con igualdad de probabilidad en cada una de ellas 
    def camina(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

    