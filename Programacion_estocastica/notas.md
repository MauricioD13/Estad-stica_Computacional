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

- Ley multiplicativa -> 'And'
  - Funciona para eventos mutuamente excluyentes o no
- Ley aditiva -> 'Or'
  - Cambia si los eventos son mutuamente excluyentes

Nota: 
- Metodo analítico -> Pensar de manera matematica las probabilidades

- Método empírico -> Simulación de lso eventos para mirar las probalidades de manera práctica

## Inferencia Estadística

Simulación para calcular probabilidades de eventos complejos sabiendo las probabilidades de eventos simples

- ¿Qué pasa cuando no sabemos las probabilidades de los eventos simples?

- Técnicas de la inferencia estadística nos permite inferir/concluir las propiedades de una población a partir de una muestra aleatorioa

![Alt text](inferencia.png)
![Alt text](inferencia1.png)

Resolver problemas sin tener que realizar todos los computos del data set.

Al sacar varias muestras en diferentes momentos la probabilidad de que sea una muestra representativa de la población aumenta. La media de la poblacion se asemeja a la media de la muestra, con algunas variaciones 
  - Varianza
  - Desviacion estandar

**Ley de los grandes números**

- En pruebas independientes repetidas con la misma probabilidad p de un resultado, la fracción de desviaciones de p converge a cero conforme la cantidad de pruebas se acerca al infinito

![A cute kitten](ley_grandes_numeros.png?style=centerme)

*Falacia del apostado*:

- Señala que después de un evento extremo, ocurrirán eventos menos extremos para nivelar la media
  - Cada evento es independiente

- La *regresión a la media* señala que después de un evento aleatorio extremo, el siguiente evento probablemente será menos extremo