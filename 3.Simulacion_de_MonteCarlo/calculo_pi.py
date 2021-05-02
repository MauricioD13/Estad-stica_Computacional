import random
import math
from statistics import mean, pstdev
from bokeh.plotting  import figure, show
def lanzar_agujas(numero_de_agujas):
    adentro_del_circulo = 0
    
    for _ in range(numero_de_agujas):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        # La funcion random regresa un valor entre 0 y 1
        distancia_euclidiana = math.sqrt(x**2 + y**2)
        
        if distancia_euclidiana <= 1:
            adentro_del_circulo += 1
    return (4 *adentro_del_circulo) / numero_de_agujas
        
def estimacion(numero_de_agujas, intentos):
    estimados = []
    
    for _ in range(intentos):
        estimacion_pi = lanzar_agujas(numero_de_agujas)
        estimados.append(estimacion_pi)
    
    media_estimados = mean(estimados)
    sigma = pstdev(estimados)
    print(f'Media = {round(media_estimados, 5)}, sigma = {round(sigma, 5)}, agujas = {numero_de_agujas}')
    return (media_estimados, sigma, estimados)

def graficar(x, y, intentos):
    
    grafica = figure(title = f'Distribucion normal estimaciones Pi con {intentos} intentos', x_axis_label ='estimaciones',y_axis_label = 'Frecuencia')
    grafica.circle(x, y)
    show(grafica)

def estimar_precision(precision, intentos, opcion): # Estimar con una precision requeria
    numero_de_agujas = 1000
    sigma = precision
    estimados = []
    if opcion == 1:
        while sigma >= precision /1.96:
            media, sigma, estimados = estimacion(numero_de_agujas, intentos)
            numero_de_agujas *= 2
    else:
        media, sigma, estimados = estimacion(numero_de_agujas, intentos)
        x = []
        y = []
        memo = {}
        for est in estimados:
            #est = round(est,3) 
            try:
                memo[est] = memo[est] + 1
            except:
                memo[est] = 1
                
        for key, values in memo.items():
            x.append(key)
            y.append(values)
        graficar(x, y, intentos)
            
        
        #graficar(x,estimados)
        
if __name__ == '__main__':
    opcion = int(input("Opcion: "))
    estimar_precision(0.05, 10000,opcion) #Precision de 0.1%