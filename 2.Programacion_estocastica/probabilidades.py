import random 
from bokeh.plotting import figure, show

def tirar_dado(numero_de_tiros):
    secuencia_1 = []
    secuencia_2 = []

    for _ in range(numero_de_tiros):
        tiro_1 = random.choice([1, 2, 3, 4, 5, 6]) 
        tiro_2 = random.choice([1, 2, 3, 4, 5, 6])
        secuencia_1.append(tiro_1)
        secuencia_2.append(tiro_2)  
    
    return secuencia_1,secuencia_2


def main(numero_de_tiros,intentos):
    tiros_1 = []
    tiros_2 = []
    x = []
    for i in range(intentos):
        secuencia_1,secuencia_2 = tirar_dado(numero_de_tiros)
        tiros_1.append(secuencia_1)
        tiros_2.append(secuencia_2)
        x.append(i)
    tiros_con_6_1 = 0
    tiros_con_6_2 = 0
    for tiro_1 in tiros_1:
        if 6 in tiro_1:
            tiros_con_6_1 +=1
    for tiro_2 in tiros_2:
        if 6 in tiro_2:
            tiros_con_6_2 +=1
    #Dado que es una probabilidad incluyente entonces
    probabilidad_tiros_6_1 = tiros_con_6_1 / intentos
    probabilidad_tiros_6_2 = tiros_con_6_2 / intentos
    
    prob_total = probabilidad_tiros_6_1*probabilidad_tiros_6_2
    #La media todas la probablidades será un buen aproximado al resultado analítico
    #Ley multiplicativa
    #Prob de sacar 6 en el dado 1 y Prob de sacar 6 en el dado 2
    #P(A)*P(B)
    """grafica = figure(title= 'Prob. tiro de dado',x_axis_label='muestras',y_axis_label='resultado')
    #Crear la figura 
    grafica.circle(x, tiros,legend='Tiros',size = 10)
    #Dibujar la linea
    show(grafica)
    #Mostrar
    """
    print(f'Probabilidad de obtener un 12 en {numero_de_tiros} con dos datos y con tiros =  {prob_total}')

if __name__ == '__main__':
    numero_de_tiros = int(input('Tiros de dado: '))
    intentos = int(input('Cuantas veces correra la simulación: '))
    #Ley de los grandes numeros:
        #Entre mayor sean la cantidad de muestras de una poblacion 
        #mas nos acercaremos a las probabilidades reales
        
    main(numero_de_tiros,intentos)
    