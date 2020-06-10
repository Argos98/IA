class Campo:
    def __init__(self):
        self.cordenadas_borracho ={}

    def aniadir_borracho(self, borracho, cordenada):
        self.coordenadas_borrachos[borracho] = cordenada
    
    def mover_borracho(self, borracho):
        delta_x, delta_y = borracho.camnina()
        cordenada_actual = self.cordenadas_borracho[borracho]
        nueva_cordenada = cordenada_actual.mover(delta_x, delta_y)

        self.cordenadas_borracho[borracho] = nueva_cordenada

    def obtener_cordenada(self, borracho):
        return self.cordenadas_borracho[borracho]