import random 

def tirar_dado(numero_de_tiros):
    secuencia = []
    
    for _ in range(numero_de_tiros):
        tiro = random.choice([1, 2, 3, 4, 5, 6]) 
        secuencia.append(tiro)   
    return secuencia


def main(numero_de_tiros,intentos):
    tiros = []
    for _ in range(intentos):
        secuencia = tirar_dado(numero_de_tiros)
        tiros.append(secuencia)
    
    tiros_con_1 = 0
    
    for tiro in tiros:
        if 1 in tiro:
            tiros_con_1 +=1
    
    probabilidad_tiros_1 = tiros_con_1 / intentos
    #La media todas la probablidades será un buen aproximado al resultado analítico
    print(f'Probabilidad de obtener un 1 en {numero_de_tiros} tiros =  {probabilidad_tiros_1}')

if __name__ == '__main__':
    numero_de_tiros = int(input('Tiros de dado: '))
    intentos = int(input('Cuantas veces correra la simulación: '))
    #Ley de los grandes numeros:
        #Entre mayor sean la cantidad de muestras de una poblacion 
        #mas nos acercaremos a las probabilidades reales
        
    main(numero_de_tiros,intentos)