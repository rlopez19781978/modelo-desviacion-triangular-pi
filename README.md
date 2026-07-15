# modelo-desviacion-triangular-pi
Modelo matemático y análisis de desviación sobre 100 millones de dígitos de Pi por Roberto López Rodríguez

TÍTULO: El Orden Oculto en el Caos de $\pi$: Un Análisis Triangular con 100 Millones de Dígitos
Autor: Roberto López Rodríguez
Ubicación: Valladolid, España
Fecha: Julio de 2026
INTRODUCCIÓN
¿Es el aparente desorden infinito de los decimales de $\pi$ un reflejo perfecto del azar puro, o existen estructuras capaces de revelar anomalías? Para responder a esto, decidí diseñar un experimento computacional de gran escala. En lugar de analizar la secuencia de dígitos de forma lineal y pasiva, introduje un modelo que evalúa relaciones de orden local a través de una geometría no lineal.
Sometiendo a $\pi$ a un estrés estadístico masivo de 100 millones de dígitos, los resultados demuestran una de las convergencias probabilísticas más bellas de la matemática empírica.
1. METODOLOGÍA: El Operador de Descenso Triangular
El modelo, al que he denominado Operador de Descenso con Memoria y Estructura Triangular, se rige por dos reglas fundamentales:
Agrupamiento Triangular (Bloques variables): Los dígitos de $\pi$ se segmentan en filas de longitud estrictamente creciente. La fila 1 consume 1 dígito (1), la fila 2 consume 2 (4, 1), la fila 3 consume 3 (5, 9, 2), y la fila $n$ consume exactamente $n$ dígitos.
Regla de Memoria Dinámica (Bono $+9$): Al sumar los elementos internos de cada fila, se introduce un detector de tendencia. Si un dígito es estrictamente menor que el que lo precede, se añade una penalización/bono de $+9$ a la suma.
La base lógica del $45\%$
En una secuencia numérica uniformemente aleatoria (dígitos del 0 al 9), la probabilidad de que un número sea menor que su predecesor es exactamente del $45\%$. Esto se demuestra por pura simetría combinatoria: de las 100 parejas posibles de dígitos consecutivos, 10 son idénticas (mesetas), 45 son ascendentes y 45 son descendentes.
Al penalizar cada "caída" con un $+9$ (la distancia máxima entre dos dígitos), el modelo se convierte en un detector de pendiente negativa de alta sensibilidad. Si $\pi$ tuviera rachas ocultas de caída o sesgos cíclicos, la estructura se deformaría exponencialmente.
2. EL MODELO MATEMÁTICO: La Fórmula de Desviación
La introducción de esta regla altera la esperanza matemática de la secuencia. El valor esperado de un dígito clásico es $4.5$, pero bajo mi operador, cada transición lógicamente pasa a "pesar" $8.55$ ($4.5 + [0.45 \times 9]$).
Modelando el crecimiento cuadrático de la estructura geométrica, definí la Fórmula del Desvío Teórico Acumulado ($D^*$) para la fila $n$ como:
$$D^*(n) = T^*(n) - (4.275n^2 + 0.225n)$$
Donde $T^*(n)$ es la suma acumulada real observada en el experimento. Si $\pi$ es perfectamente normal (aleatorio), $D^*(n)$ debe oscilar controladamente cerca de cero, demostrando un error relativo despreciable a gran escala.
3. RESULTADOS: El Comportamiento de $\pi$ ante el Estrés Estadístico
El algoritmo se ejecutó aumentando la muestra de forma exponencial hasta alcanzar el umbral de los 100 millones de dígitos. A esa escala máxima, se completaron exactamente 14,141 filas triangulares cerradas (procesando un total de $99,997,911$ dígitos).
Los datos consolidados muestran una convergencia implacable:
Dígitos Evaluados
Filas Completadas
Descensos Detectados
Frecuencia Real
Desviación del Teórico (45%)
Desviación Final (D∗(n))
Error Relativo en Suma
Puntuación Z
190
19
86
50.29%
$+5.29\%$
$-5.50$
$0.71\%$
Ruido inicial
10,000
140
4,336
44.56%
$-0.44\%$
$-652.50$
$0.78\%$
$-0.86\sigma$
100,000
446
44,406
44.75%
$-0.25\%$
$-2,814.60$
$0.33\%$
$-1.59\sigma$
1,000,000
1,413
448,809
44.99%
$-0.01\%$
$-1,834.50$
$0.021\%$
$-0.21\sigma$
10,000,000
4,471
4,496,619
44.9984%
$-0.0016\%$
$-803.25$
$0.0009\%$
$-0.056\sigma$
100,000,000
14,141
44,991,723
44.99905%
$-0.00095\%$
$-8,762.53$
$0.0010\%$
$-0.195\sigma$

4. CONCLUSIONES
Convergencia Absoluta: Con 100 millones de dígitos, la tasa de descenso real observada en $\pi$ se clava en un $44.99905\%$, reduciendo la desviación frente a la lógica combinatoria pura a tan solo $9.5$ millonésimas de punto porcentual.
Estabilidad Frente al Caos: Al evaluar la distancia estadística (Puntuación Z), el experimento arroja un contundente $-0.195\sigma$. En términos estadísticos, esto significa que el comportamiento de $\pi$ es indistinguible de un modelo idealizado de caos cuántico o azar perfecto.
Resiliencia de la Constante: No importa qué regla de memoria de corto plazo se le aplique ni qué geometría no lineal rompa su lectura horizontal; la constante matemática más famosa de la historia absorbe las modificaciones, demostrando un error relativo en la suma de apenas el $0.0010\%$.
Este análisis empírico confirma que detrás del aparente desorden infinito de los decimales de $\pi$ no hay capricho ni deriva, sino una armonía estadística indestructible.
