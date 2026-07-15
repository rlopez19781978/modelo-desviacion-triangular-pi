"""
Modelo de Análisis de Desviación Triangular de Pi
Autor: Roberto López Rodríguez
DNI: 71.121.709M (Valladolid, España)
Año: 2026

Este script implementa el "Operador de Descenso con Memoria y Estructura Triangular"
sobre los dígitos decimales de Pi, calculando la desviación real frente al 
modelo teórico esperado de crecimiento cuadrático.
"""

import math

def generador_digitos_pi():
    """
    Generador infinito de los dígitos de Pi usando el algoritmo Spigot (Gibbons, 2004).
    Evita la necesidad de leer o descargar archivos de texto masivos de internet.
    """
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if 4 * q + r - t < n * t:
            yield n
            nr = 10 * (r - n * t)
            n = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r = nr
        else:
            nr = (2 * q + r) * l
            nn = (q * (7 * k + 2) + r * l) // (t * l)
            q *= k
            t *= l
            l += 2
            k += 1
            n = nn
            r = nr

def simular_modelo_triangular(limite_filas):
    """
    Ejecuta el agrupamiento triangular y aplica la regla de memoria de descenso (+9).
    Calcula las desviaciones paso a paso e imprime el análisis final.
    """
    pi_gen = generador_digitos_pi()
    
    # Omitimos el "3" inicial de Pi para trabajar estrictamente con la parte decimal
    next(pi_gen) 
    
    suma_real_clasica = 0
    suma_real_con_regla = 0
    total_descensos = 0
    total_transiciones = 0
    total_digitos_procesados = 0
    
    print(f"Iniciando simulación del Modelo López-Rodríguez para {limite_filas:,} filas...\n")
    
    for fila in range(1, limite_filas + 1):
        # 1. Extraemos de forma dinámica los dígitos para la fila actual
        digitos_fila = [next(pi_gen) for _ in range(fila)]
        total_digitos_procesados += len(digitos_fila)
        
        # 2. Calculamos la suma clásica de la fila
        suma_clasica_fila = sum(digitos_fila)
        suma_real_clasica += suma_clasica_fila
        
        # 3. Aplicamos la regla de memoria dinámica de descenso (+9)
        bono_descenso = 0
        for i in range(1, len(digitos_fila)):
            total_transiciones += 1
            # Si el dígito actual es estrictamente menor que su predecesor
            if digitos_fila[i] < digitos_fila[i - 1]:
                bono_descenso += 9
                total_descensos += 1
                
        suma_real_con_regla += (suma_clasica_fila + bono_descenso)
        
        # Imprimir progreso intermedio para escalas clave
        if fila in [19, 140, 446, 1413, 4471, 14141]:
            frecuencia_actual = (total_descensos / total_transiciones) * 100 if total_transiciones > 0 else 0
            # Fórmula teórica del desvío acumulado de Roberto: D*(n) = T*(n) - (4.275 * n^2 + 0.225 * n)
            valor_teorico_esperado = 4.275 * (fila**2) + 0.225 * fila
            desviedad_acumulada = suma_real_con_regla - valor_teorico_esperado
            error_relativo = (abs(desviedad_acumulada) / valor_teorico_esperado) * 100
            
            print(f"--- HITO ALCANZADO: FILA {fila:,} ---")
            print(f"  * Dígitos procesados acumulados: {total_digitos_procesados:,}")
            print(f"  * Transiciones analizadas: {total_transiciones:,}")
            print(f"  * Descensos detectados: {total_descensos:,} ({frecuencia_actual:.5f}%)")
            print(f"  * Suma Real Obtenida (T*): {suma_real_con_regla:,}")
            print(f"  * Suma Teórica Esperada: {valor_teorico_esperado:,.2f}")
            print(f"  * Desviación Acumulada (D*): {desviedad_acumulada:,.2f}")
            print(f"  * Error Relativo: {error_relativo:.6f}%\n")

    # 4. Análisis estadístico final (Cálculo de la Puntuación Z)
    p_teorica = 0.45
    esperanza_descensos = total_transiciones * p_teorica
    desviacion_estandar = math.sqrt(total_transiciones * p_teorica * (1 - p_teorica))
    puntuacion_z = (total_descensos - esperanza_descensos) / desviacion_estandar
    
    print("================================================================")
    print("                      VERDICTO FINAL")
    print("================================================================")
    print(f"Frecuencia Final de Descensos: {total_descensos / total_transiciones * 100:.6f}%")
    print(f"Frecuencia Teórica de Azar Puro: 45.000000%")
    print(f"Desviación de Descensos Absoluta: {total_descensos - esperanza_descensos:,.1f} descensos")
    print(f"Puntuación Z del Experimento: {puntuacion_z:.4f}σ")
    
    if abs(puntuacion_z) < 1.96:
        print("Resultado: Dentro del rango normal del azar (-1.96σ a +1.96σ).")
        print("Conclusión: Pi se comporta como un generador de caos perfectamente aleatorio.")
    else:
        print("Resultado: Fuera del rango de fluctuación normal.")
        print("Conclusión: Se detecta una desviación estadística significativa.")
    print("================================================================")

# Para correr el experimento completo hasta los 100 millones de dígitos (14,141 filas):
if __name__ == "__main__":
    # Puedes cambiar este número para pruebas rápidas (ej. 140 o 446 filas)
    # 14,141 filas consume exactamente 99,997,911 dígitos.
    FILAS_A_PROCESAR = 14141 
    simular_modelo_triangular(FILAS_A_PROCESAR)
