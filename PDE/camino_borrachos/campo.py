#en este espacio definimos el lugar donde se va mover el borracho, es el espacio fisico donde nuestro borracho interactua 
class Campo:
    #aca solo tenemos un arreglo de las cordenadas de los borrachos
    def __init__(self):
        self.coordenadas_de_borrachos = {}

    #esto guarda las cordenadas obtenidas en la funcion 'mover_borracho'
    def anadir_borracho(self, borracho, coordenada):
        self.coordenadas_de_borrachos[borracho] = coordenada

    #esto hace que se mueva
    def mover_borracho(self, borracho):
        #asigna a donde moverse tanto en x e y
        delta_x, delta_y = borracho.camina()
        #toma las cordenadas actuales guardadas 
        coordenada_actual = self.coordenadas_de_borrachos[borracho]
        #esta almacena la nueva cordenada 
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)
        #este guarda las nuevas cordenas para el borracho corespondiente 
        self.coordenadas_de_borrachos[borracho] = nueva_coordenada

    #esto es un get
    def obtener_coordenada(self, borracho):
        return self.coordenadas_de_borrachos[borracho]