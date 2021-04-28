# Programación Estocástica

- Un programa es determinístico si cuando se corre con el mismo input produce el mismo output
    - Hay problemas que no se pueden resolver mediante programas determinísticos
- Programas estocásticos permite introduccir aleatoriedad

    - Resolver problemas y simulaciones más adecuadas
    - Distribuciones probabilísticas de un problema -> Estimaciones

Ejemplo de problema:

- Generar un programa para controlar los semaforos

  - Deterministicos -> Parametros -> Desicion
    - Patrones -> Datos estadísticos-> Distribuciones de probabilidad -> Desición
      - Responder mucho mejor

> Cambio de forma de ver un problema


## Calculo de Probabilidades

¿Cómo calcular probabilidades?

- Probabilidad: Medida de la certidumbre asociada a un evento o suceso futuro y siempre es un numero de 0 a 1

  - 0 jamas sucede el evento
  - 1 garantizado de suceder en el futuro

- Preguntamos: ¿Qué fracción de todos los posibles eventos tiene la propiedad  que buscamos
  - Se deben calcular todas la posibilidades de un evento 
  - Enumerar todas las posibilidades (Brute force)
> La probabilidade de que un evento suceda y mas la probabilidad de que no suceda es siempre 1

### Leyes
![Alt text](Leyes.png)

- Ley multiplicativa -> 'Or'
  - Funciona para eventos mutuamente excluyentes o no
- Ley aditiva -> 'And'
  - Cambia si los eventos son mutuamente excluyentes

Nota: 
- Metodo analítico -> Pensar de manera matematica las probabilidades

- Método empírico -> Simulación de lso eventos para mirar las probalidades de manera práctica

## Simulacion de Probabilidades

