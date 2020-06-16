#esta clase se encarga de mover todo oh mejor dicho hace los calculos correspondientes
class Coordenada:

    # solo se tiene llas cordenadas 'x' y 'y'
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #este hace que se mueva 
    def mover(self, delta_x, delta_y):
        return Coordenada(self.x + delta_x, self.y + delta_y)

    #esto calcula la distancia 
    def distancia(self, otra_coordenada):
        delta_x = self.x - otra_coordenada.x 
        delta_y = self.y - otra_coordenada.y 

        return (delta_x**2 + delta_y**2)**0.5