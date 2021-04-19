import sys
def fibonacci_recursivo(n):
    if n==0 or n==1:
        return 1
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def fibonacci_dinamico(n,memo={}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n] #Buscamos n si se tiene 
    except KeyError:
        #Si no tiene el valor en memo entonces se calcula el numero
        resultado = fibonacci_dinamico(n - 1,memo) + fibonacci_dinamico(n - 2,memo) 
        
        #Guardar resultados en el diccionario para no repetir calculos
        memo[n] = resultado
        return resultado
if __name__ == '__main__':
    sys.setrecursionlimit(10002) #Cambia la profundidad de la recursividad
    n = int(input('Escoge un numero: '))
    resultado = fibonacci_dinamico(n)
    print(resultado)
