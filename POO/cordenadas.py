class Coordenada: 
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_cordenada):
        x_diff = (self.x - otra_cordenada.x)**2
        y_diff = (self.y - otra_cordenada.y)**2

        return(x_diff + y_diff )**0.5


if __name__ == '__main__':

    cord_1 = Coordenada(3,44)
    cord_2 = Coordenada(45,5)

    print(cord_1.distancia(cord_2))

