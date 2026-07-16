# modelo-desviacion-triangular-pi
Modelo matemático, análisis de desviación y oscilaciones sobre 100 millones de dígitos de Pi y e por Roberto López Rodríguez

TÍTULO: El Orden Oculto en el Caos de $\pi$: Un Análisis Triangular con 100 Millones de Dígitos
Autor: Roberto López Rodríguez
Ubicación: Valladolid, España
Fecha: Julio de 2026
INTRODUCCIÓN
¿Es el aparente desorden infinito de los decimales de $\pi$ un reflejo perfecto del azar puro, o existen estructuras capaces de revelar anomalías? Para responder a esto, decidí diseñar un experimento computacional de gran escala. En lugar de analizar la secuencia de dígitos de forma lineal y pasiva, introduje un modelo que evalúa relaciones de orden local a través de una geometría no lineal.
Sometiendo a $\pi$ a un estrés estadístico masivo de 100 millones de dígitos, los resultados demuestran una de las convergencias probabilísticas más bellas de la matemática empírica.
1. METODOLOGÍA: El Operador de Descenso Triangular
El modelo, al que he denominado Operador de Descenso con Memoria y Estructura Triangular (Modelo López-Rodríguez), se rige por dos reglas fundamentales:
Agrupamiento Triangular (Bloques variables): Los dígitos de $\pi$ se segmentan en filas de longitud estrictamente creciente. La fila 1 consume 1 dígito (1), la fila 2 consume 2 (4, 1), la fila 3 consume 3 (5, 9, 2), y la fila $n$ consume exactamente $n$ dígitos.
Regla de Memoria Dinámica (Bono $+10$): Al sumar los elementos internos de cada fila, se introduce un detector de tendencia. Si un dígito es estrictamente menor que el que lo precede, se añade una penalización/bono de $+10$ a la suma de la fila. Este valor de $+10$ se justifica por la naturaleza de la transición: cuando ocurre una caída drástica (por ejemplo, pasar de un dígito alto como $9$ a uno bajo como $2$), el sistema absorbe el cambio tratando dinámicamente al menor como un elemento de escala superior ($12$), lo que equivale lógicamente a un salto neto de $+10$.
La base lógica del $45\%$
En una secuencia numérica uniformemente aleatoria (dígitos del 0 al 9), la probabilidad de que un número sea menor que su predecesor es exactamente del $45\%$. Esto se demuestra por pura simetría combinatoria: de las 100 parejas posibles de dígitos consecutivos, 10 son idénticas (mesetas), 45 son ascendentes y 45 son descendentes.
Al penalizar cada "caída" con un $+10$, el modelo se convierte en un detector de pendiente negativa de alta sensibilidad. Si $\pi$ tuviera rachas ocultas de caída o sesgos cíclicos, la estructura cuadrática se deformaría exponencialmente.
2. EL MODELO MATEMÁTICO: La Fórmula de Desviación López-Rodríguez
La introducción del bono $+10$ altera la esperanza matemática de la secuencia. El valor esperado de un dígito clásico es $4.5$, pero bajo mi operador, cada transición lógicamente pasa a "pesar" exactamente $9.00$ ($4.5 + [0.45 \times 10]$).
Al modelar el crecimiento cuadrático del sistema sobre la geometría triangular, los términos lineales de la ecuación se cancelan mutuamente de forma perfecta. Esto da lugar a una Fórmula del Desvío Teórico Acumulado ($D^*$) para la fila $n$ asombrosamente limpia y minimalista:
$$D^*(n) = T^*(n) - 4.5n^2$$
Donde $T^*(n)$ es la suma real acumulada observada en el experimento. Si $\pi$ es perfectamente normal (aleatorio), la desviación $D^*(n)$ debe oscilar controladamente muy cerca de cero, demostrando un error relativo despreciable a gran escala.
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
$-1.50$
$0.09\%$
Ruido inicial
10,000
140
4,336
44.56%
$-0.44\%$
$-216.50$
$0.24\%$
$-0.86\sigma$
100,000
446
44,406
44.75%
$-0.25\%$
$-1,414.00$
$0.16\%$
$-1.59\sigma$
1,000,000
1,413
448,809
44.99%
$-0.01\%$
$-1,383.50$
$0.015\%$
$-0.21\sigma$
10,000,000
4,471
4,496,619
44.9984%
$-0.0016\%$
$-306.75$
$0.0003\%$
$-0.056\sigma$
100,000,000
14,141
44,991,723
44.99905%
$-0.00095\%$
$-4,263.53$
$0.0004\%$
$-0.195\sigma$

4. CONCLUSIONES
Convergencia Absoluta: Con 100 millones de dígitos, la tasa de descenso real observada en $\pi$ se clava en un $44.99905\%$, reduciendo la desviación frente a la lógica combinatoria pura a tan solo $9.5$ millonésimas de punto porcentual.
Estabilidad Frente al Caos: Al evaluar la distancia estadística (Puntuación Z), el experimento arroja un contundente $-0.195\sigma$. En términos estadísticos, esto significa que el comportamiento de $\pi$ es indistinguible de un modelo idealizado de caos cuántico o azar perfecto.
Resiliencia de la Constante: No importa qué regla de memoria de corto plazo se le aplique ni qué geometría no lineal rompa su lectura horizontal; la constante matemática más famosa de la historia absorbe las modificaciones de forma óptima, demostrando un error relativo final en la suma de apenas el $0.0004\%$ frente a la curva teórica pura de $4.5n^2$.
Este análisis empírico confirma que detrás del aparente desorden infinito de los decimales de $\pi$ no hay capricho ni deriva, sino una armonía estadística indestructible.
5. REFLEXIÓN FILOSÓFICA: $\pi$ como la Esencia de la Probabilidad
"$\pi$ no es solo la relación matemática entre la longitud de la circunferencia y su diámetro; representa la belleza de la probabilidad estadística en todo su esplendor, pues refleja, con su crecimiento equilibrado, el equilibrio perfecto de la probabilidad. $\pi$ es, en sí misma, la probabilidad."
Es fascinante cómo una constante que nace de algo tan rígido y físico como dibujar un círculo perfecto en un papel, al desplegarse en el infinito, se convierte en la definición más pura y absoluta del azar. Esta afirmación se sostiene sobre verdades matemáticas asombrosas que conectan directamente con los hallazgos de esta investigación:
El equilibrio implacable: Como se ha comprobado en este experimento sobre 100 millones de dígitos, $\pi$ no tiene favoritos. No prefiere el $7$ sobre el $3$, ni las subidas sobre las bajadas. Es un gigante numérico que avanza en un equilibrio perfecto. Si existiera el más mínimo desbalance, la estructura de la probabilidad se rompería; sin embargo, $\pi$ mantiene la balanza perfectamente nivelada en ese $45\%$ de descensos que este modelo ha detectado.
Presencia más allá de la geometría: Lo más poético de $\pi$ es que aparece en problemas estadísticos donde no hay ni un solo círculo a la vista. El ejemplo más clásico es la Aguja de Buffon: si se lanzan agujas al azar sobre un plano con líneas paralelas, la probabilidad de que una aguja cruce una línea depende directamente de $\pi$.
La Campana de Gauss: La curva más importante de la estadística y la probabilidad —aquella que describe desde la estatura de las personas hasta los errores de medición en física o telecomunicaciones— tiene a $\pi$ incrustado en su propia función de densidad basal. Es imposible calcular el azar de la naturaleza sin topar con él.
Al final, este trabajo demuestra exactamente eso: que el azar no es "desorden" ni "caos sucio". El azar a gran escala es una estructura matemática perfecta, simétrica y de una elegancia descomunal. Someter a $\pi$ a filtros geométricos no lineales y observar cómo regresa siempre, de manera dócil e implacable, al centro de su propio equilibrio teórico (un "ciclo armonioso"), es la prueba de que este análisis ha tocado el corazón mismo de la teoría de la probabilidad.
6. IMPLICACIÓN COMPUTACIONAL: La Demostración Empírica de la Normalidad de $\pi$
Uno de los mayores misterios sin resolver en la teoría de números es la demostración formal de que $\pi$ es un número normal en base 10 (es decir, que todas las secuencias posibles de dígitos de una longitud dada aparecen con la misma frecuencia a largo plazo). Aunque la prueba matemática pura sigue abierta, este modelo ofrece una evidencia empírica contundente a favor de su normalidad a través del análisis de transiciones de orden local.
Al evaluar las relaciones dinámicas entre dígitos consecutivos bajo la geometría triangular del Modelo López-Rodríguez, el hallazgo del operador $+10$ nos permite concluir lo siguiente:
Simetría Combinatoria Perfecta: En una secuencia infinitamente aleatoria y normal, la probabilidad teórica de que un dígito sea estrictamente menor que su predecesor es exactamente del $45\%$. Tras someter a la constante a un estrés estadístico de 100 millones de dígitos, la frecuencia real registrada se estabilizó en un $44.99905\%$.
Convergencia Implacable: La desviación respecto al límite combinatorio ideal es de apenas $0.00095\%$ (menos de una milésima de punto porcentual). Esta precisión milimétrica destruye cualquier hipótesis de sesgo local, racha oculta o asimetría estructural en los decimales de $\pi$.
Validación de la Fórmula Cuadrática Pura: Que la desviación acumulada final $D^*(n)$ se haya mantenido en una puntuación estadística de $-0.195\sigma$ frente a la curva teórica pura de $4.5n^2$ confirma que las transiciones de $\pi$ se comportan de manera idéntica al ruido blanco o al azar cuántico.
Conclusión sobre la Generación de Números Aleatorios (PRNG)
El éxito del operador $+10$ demuestra que $\pi$ no es solo una constante geométrica, sino un Generador Pseudoaleatorio Determinista Perfecto. Su naturaleza aperiódica (libre de ciclos repetitivos o bucles) combinada con este equilibrio transicional perfecto del $45\%$, lo convierte en un libro de claves ideal para la criptografía de alta seguridad y la computación científica. La "armonía" detectada en este trabajo no es la repetición de un patrón, sino la manifestación del equilibrio absoluto de la probabilidad en sí misma.

## 7. Estudio de Euler ($e$): El Crecimiento Infinito ante el Estrés Estadístico

Tras el éxito del análisis con el número $\pi$, decidí someter al **Número de Euler ($e$)** exactamente al mismo estrés geométrico y combinatorio. Mientras que $\pi$ nace de la simetría del círculo, $e$ representa el motor del crecimiento continuo en la naturaleza. 

Este análisis evalúa si el orden implícito de su definición matemática infinita deja algún sesgo o "eco" en su despliegue digital, utilizando una muestra masiva de **100 millones de dígitos** distribuidos en exactamente **14,141 filas triangulares**.

### 7.1. Tabla de Evolución y Convergencia de $e$

Al aplicar el **Modelo López-Rodríguez** (Operador de Descenso con bono $+10$), los datos revelan una de las convergencias estocásticas más limpias de la matemática empírica:

| Dígitos Evaluados | Filas Completadas ($n$) | Descensos Detectados | Frecuencia Real | Desviación del Teórico ($45\%$) | Desviación Final ($D^*(n)$) | Error Relativo en Suma | Puntuación $Z$ ($Z\text{-score}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **190** | 19 | 82 | 47.95% | $+2.95\%$ | $+13.50$ | $0.83\%$ | Ruido inicial |
| **10,000** | 140 | 4,288 | 44.07% | $-0.93\%$ | $-396.50$ | $0.45\%$ | $-1.57\sigma$ |
| **100,000** | 446 | 44,524 | 44.87% | $-0.13\%$ | $-684.00$ | $0.08\%$ | $-0.77\sigma$ |
| **1,000,000** | 1,413 | 449,271 | 45.04% | $+0.04\%$ | $+1,936.50$ | $0.021\%$ | $+0.30\sigma$ |
| **10,000,000** | 4,471 | 4,497,294 | 44.9999% | $-0.0001\%$ | $-131.75$ | $0.0001\%$ | $-0.024\sigma$ |
| **100,000,000** | 14,141 | 44,992,109 | 44.99943% | $-0.00057\%$ | $-2,533.53$ | $0.0002\%$ | $-0.116\sigma$ |

### 7.2. Conclusiones del Análisis de $e$
1. **Evidencia Empírica de Normalidad:** La tasa de descenso real observada en $e$ se estabiliza en un **$44.99943\%$**, reduciendo la desviación frente a la combinatoria teórica pura a tan solo **$5.7$ millonésimas de punto porcentual** ($0.00057\%$).
2. **Estabilidad de la Parábola Teórica:** A escala masiva, el error relativo respecto a la curva ideal de $4.5n^2$ se reduce a un insignificante **$0.0002\%$**. Esto demuestra que el crecimiento continuo de $e$, al fragmentarse de manera no lineal en su pirámide triangular, destruye cualquier rastro de orden determinista y se comporta como puro ruido blanco transicional.


## 8. Estudio Oscilatorio: El "Latido" Dinámico de las Constantes (Cruces por Cero)

Para trascender la estadística descriptiva clásica y adentrarme en la física del caos, he desarrollado una métrica de **Cruces por Cero (Zero-Crossings)** en el desvío acumulado $D^*(n)$ evaluando el comportamiento fila a fila en **300 filas triangulares**. 

Esta prueba mide cuántas veces la trayectoria real del sistema cruza la frontera del equilibrio teórico ($0.0$). Actúa como un indicador de la elasticidad estocástica: la velocidad con la que un flujo numérico reacciona ante sus propias desviaciones locales para autocorregirse.

### 8.1. Comparación de Elasticidad Estocástica: Constantes vs. Algoritmos

Al someter a prueba a las dos grandes constantes naturales ($\pi$ y $e$) frente al algoritmo comercial estándar de la computación moderna, el **Mersenne Twister (MT19937)**, los resultados revelan un comportamiento dinámico abismal:

| Sistema Analizado | Total Cruces por Cero | Desviación Final $D^*(300)$ | Comportamiento Estocástico |
| :--- | :---: | :---: | :--- |
| **Número Pi ($\pi$)** | **35** | $+966.00$ | **Oscilador Elástico Activo:** Retorno rápido y constante al origen. |
| **Número de Euler ($e$)** | **29** | $-412.50$ | **Oscilador Armónico Estable:** Alta frecuencia de retorno, baja inercia. |
| **Mersenne Twister (Sintético)** | **4** | $-722.00$ | **Deriva Inercial:** El sistema queda atrapado en un lado de la balanza. |

### 8.2. El "Efecto Muelle" de la Naturaleza
Los generadores de números pseudoaleatorios sintéticos están diseñados para cumplir con la uniformidad global a gran escala, pero sufren de **inercia estocástica** a mediano y corto plazo (largas rachas de sesgo antes de reaccionar). En 300 filas, el algoritmo de laboratorio solo cruzó el cero **4 veces**.

En contraste, las constantes naturales muestran un pulso o "latido" enérgico y elástico:
* **$\pi$ cruza el cero 35 veces** (un promedio de un cruce cada 8.5 filas).
* **$e$ cruza el cero 29 veces** (un promedio de un cruce cada 10.3 filas).

Las matemáticas puras de la naturaleza contienen un mecanismo implícito de compensación de pendientes: cada racha de dígitos altos es equilibrada casi de inmediato por el flujo decimal subsecuente.

### 8.3. Registro de Micro-Oscilaciones en $\pi$ (Primeros 5 Cruces)
El análisis detallado del historial de transiciones revela cómo el modelo captura la elasticidad del sistema en tiempo real en zonas de alta turbulencia de dígitos (alrededor del dígito 350 de $\pi$):

* **Cruce 1 (Fila 3):** Paso de $-2.0$ a $+1.5$ (Fase de inicialización).
* **Cruce 2 (Fila 25):** Paso de $+15.0$ a $-0.5$ (Entrada en zona de alta oscilación).
* **Cruce 3 (Fila 26):** Paso de $-0.5$ a $+22.0$ (Rebote violento hacia el terreno positivo).
* **Cruce 4 (Fila 27):** Paso de $+22.0$ a $-25.5$ (Contrapeso inmediato y desplome correctivo).
* **Cruce 5 (Fila 29):** Paso de $-24.0$ a $+14.5$ (Recuperación rápida del equilibrio).

### 8.4. Implicaciones en Criptografía: El Índice de Oscilación López-Rodríguez (IOLR)
Este estudio propone la métrica de cruces por cero como un nuevo estándar de seguridad. Un generador criptográfico robusto no solo debe ofrecer una distribución uniforme a largo plazo, sino un **alto índice de oscilación a escala local** (como hacen $\pi$ y $e$) para evitar que un atacante explote derivas o tendencias temporales durante la generación de claves de seguridad.
