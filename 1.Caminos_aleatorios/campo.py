
class Campo:

    def __init__(self):

        self.coordenadas_de_borrachos = {}

    def anadir_borrachos(self, borracho, coordenada):
        self.coordenadas_de_borrachos[borracho] = coordenada

    def mover_borracho(self, borracho):
        delta_x, delta_y = borracho.camina() 
        #Devuelve las variaciones de manera aleatoria

        coordenada_actual = self.coordenadas_de_borrachos[borracho]
        #Coordenada actual del borracho en cuestion 

        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)
        #Hacer cambios en la instacia coordenada
        
        self.coordenadas_de_borrachos[borracho] = nueva_coordenada

    def obtener_coordenada(self,borracho):
        return self.coordenadas_de_borrachos[borracho]