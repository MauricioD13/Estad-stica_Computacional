
from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure, show


def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)

    return inicio.distancia(campo.obtener_coordenada(borracho))


def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho(nombre='David')#Funcion agnostica al tipo
    origen = Coordenada(0, 0)
    distancias = []

    for _ in range(numero_de_intentos):#El guion bajo indica que no importa la variable

        campo = Campo()
        campo.anadir_borrachos(borracho, origen)# Poner el borracho en el origen
        resultado_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(resultado_caminata, 1)) 
    return distancias
def graficar(x, y):
    grafica = figure(title= 'Camino aletorio',x_axis_label='pasos',y_axis_label='distancia')
    #Crear la figura 
    grafica.line(x, y ,legend='distancia media')
    #Dibujar la linea
    show(grafica)
    #Mostrar


def main(distancias_de_caminata,intentos, tipo_de_borracho):
    distancias_medio_caminata = []
    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos,intentos,tipo_de_borracho)

        distancia_media = round(sum(distancias)/len(distancias),3)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_medio_caminata.append(distancia_media)
        print(f'{tipo_de_borracho.__name__} caminada aleatoria de {pasos} pasos')
        print(f"Media = {distancia_media}")
        print(f"Max = {distancia_maxima}")
        print(f"Min = {distancia_minima}")
    graficar(distancias_de_caminata, distancias_medio_caminata)


if __name__ == '__main__':

    distancias_de_caminata = [10, 100, 1000, 10000]
    intentos = 100
    
    main(distancias_de_caminata,intentos, BorrachoTradicional)