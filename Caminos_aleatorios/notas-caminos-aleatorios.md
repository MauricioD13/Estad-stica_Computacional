# Notas: Caminos aleatorios

Problemas que incluyen la aleatoriedad:

- Es un tipo de simulación que elige aleatoriamente una decision dentro de un conjunto de decisiones válidas

- Se utiliza en muchos campos del conocimiento cuando los sistemas no son deterministas e incluyen elementos de aleatoriedad

- Tipo de programación probabilísitica -> Cada ves que halla una nueva entrada abra una salida diferente

Ejemplo:

- Movimiento browniano -> Simulación de particulas
  - Para una simulación se generan muchas particulas por medio de la programación que tengan el comportamiento adecuado

- Simulación de movimiento de las galaxias

- Simulación de mercados 

----

## Entendiento aleatoriedad con Python

Teoría previa para entender la programación de el camino de borrachos;

Problema que se dividio en tres clases:

- ¿Que es un borracho?
    - Clase Borracho -> Persona
    - Define como se mueve -> 25% de probabilidad para todas las direcciones
- ¿Donde se mueve el borracho?
    - Clase Campo -> Mapa
- Coordenada -> Clase Coordenada
    - Clase Coordenada -> Movimiento

Generar una jerarquía mediante la herencia. La clase Borracho extiende la clase Borracho Tradicional.
- El borracho tradicional tiene los movimientos básicos 

Quiero saber donde va a estar el borracho después de una cierta cantidad de pasos: 10, 100, 1000, etc...

- En resumen hay que saber donde inicia y donde termina. Esto es posible mediante la distancia euclidiana

- No importa cuantos pasos se le pongan al borracho, tiene una tendencia en el comportamiento

- Entre más pasos haya hay más información. Pero también es muy imnportante correr la simulación muchas veces para poder ver las tendencias

----

A medida que se toman mas muestras al momento de hacer una simulación , es posible generar certeza sobre lo tipos de comportamiento que tiene un programa
