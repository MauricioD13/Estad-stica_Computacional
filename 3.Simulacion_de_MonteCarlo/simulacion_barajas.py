import random
import collections
PALOS = ['espada','corazon','rombo','trebol']
VALORES = ['as','2','3','4','5','6','7','8','9','10','jota','reina','rey']

def crear_baraja():
    cartas = []
    for palo in PALOS:
        for valor in VALORES:
            cartas.append((palo,valor))
    return cartas

def obtener_mano(cartas, tam_mano):
    mano = random.sample(cartas,tam_mano)
    """
    Esta funcion de random obtiene un valor aleatorio de una coleccion 
    sin posibilidad de reposicion. Es decir que, no se puede sacar el 
    mismo valor dos veces.
    
    """
    return mano

def main(tam_mano, intentos):
    cartas = crear_baraja()
    manos = []
    for _ in range(intentos):
        mano = obtener_mano(cartas, tam_mano)
        manos.append(mano)
    
    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
                valores.append(carta[0])
        counter = dict(collections.Counter(valores))
        
        for val in counter.values():
            if val == 5:
                pares +=1
                break
    probabilidad_par = pares / intentos
    print(f'Probabilidad de obtener un par en un mano de {tam_mano} en {intentos} intentos es: {probabilidad_par}')    
if __name__ == '__main__':
    tam_mano = int(input('De cuantas cartas sera la mano: '))
    intentos = int(input('Cuantos intentors para calcular la probabilidad: '))
    main(tam_mano, intentos)