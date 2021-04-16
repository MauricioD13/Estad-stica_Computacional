def fibonacci_recursivo(n):
    if n==0 or n==1:
        return 1
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def fibonacci_dinamico(n,memo={}):
    if n == 0 or n == 1:
        return
    try:
        return memo[n] #Buscamos n si se tiene 
    except :
        resultado = fibonacci_dinamico(n - 1,memo) + fibonacci_dinamico(n - 2,memo) 
        #Guardar resultados en el diccionario para no repetir calculos
        memo[n] = resultado
        return resultado
if __name__ == '__main__':
    n = int(input('Escoge un numero: '))
    resultado = fibonacci_dinamico(n)
    print(resultado)