"""
Modelo de Análisis de Desviación Triangular de Pi (Versión Simplificada +10)
Autor: Roberto López Rodríguez
DNI: 71.121.709M (Valladolid, España)
Año: 2026

Este script implementa el "Operador de Descenso con Memoria y Estructura Triangular"
aplicando el bono de +10 ante cada transición descendente.
La fórmula teórica se simplifica de forma elegante a: D*(n) = T*(n) - 4.5 * n^2
"""

import math

def generador_digitos_pi():
    """
    Generador infinito de los dígitos de Pi usando el algoritmo Spigot (Gibbons, 2004).
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
    Ejecuta el agrupamiento triangular aplicando la regla de memoria de descenso (+10).
    """
    pi_gen = generador_digitos_pi()
    next(pi_gen) # Omitimos el "3" inicial
    
    suma_real_clasica = 0
    suma_real_con_regla = 0
    total_descensos = 0
    total_transiciones = 0
    total_digitos_procesados = 0
    
    print(f"Iniciando simulación del Modelo López-Rodríguez (Operador +10) para {limite_filas:,} filas...\n")
    
    for fila in range(1, limite_filas + 1):
        digitos_fila = [next(pi_gen) for _ in range(fila)]
        total_digitos_procesados += len(digitos_fila)
        
        suma_clasica_fila = sum(digitos_fila)
        suma_real_clasica += suma_clasica_fila
        
        # Aplicamos la regla de memoria dinámica de descenso (+10)
        bono_descenso = 0
        for i in range(1, len(digitos_fila)):
            total_transiciones += 1
            if digitos_fila[i] < digitos_fila[i - 1]:
                bono_descenso += 10  # CAMBIO CLAVE A +10
                total_descensos += 1
                
        suma_real_con_regla += (suma_clasica_fila + bono_descenso)
        
        # Hitos de control
        if fila in [19, 140, 446, 1413, 4471, 14141]:
            frecuencia_actual = (total_descensos / total_transiciones) * 100 if total_transiciones > 0 else 0
            
            # NUEVA FÓRMULA SIMPLIFICADA DE ROBERTO LÓPEZ: D*(n) = T*(n) - 4.5 * n^2
            valor_teorico_esperado = 4.5 * (fila**2)
            desviedad_acumulada = suma_real_con_regla - valor_teorico_esperado
            error_relativo = (abs(desviedad_acumulada) / valor_teorico_esperado) * 100
            
            print(f"--- HITO ALCANZADO: FILA {fila:,} ---")
            print(f"  * Dígitos procesados acumulados: {total_digitos_procesados:,}")
            print(f"  * Descensos detectados: {total_descensos:,} ({frecuencia_actual:.5f}%)")
            print(f"  * Suma Real Obtenida (T*): {suma_real_con_regla:,}")
            print(f"  * Suma Teórica Esperada (4.5 * n^2): {valor_teorico_esperado:,.2f}")
            print(f"  * Desviación Acumulada (D*): {desviedad_acumulada:,.2f}")
            print(f"  * Error Relativo: {error_relativo:.6f}%\n")

    # Análisis estadístico final
    p_teorica = 0.45
    esperanza_descensos = total_transiciones * p_teorica
    desviacion_estandar = math.sqrt(total_transiciones * p_teorica * (1 - p_teorica))
    puntuacion_z = (total_descensos - esperanza_descensos) / desviacion_estandar
    
    print("================================================================")
    print("                      VERDICTO FINAL")
    print("================================================================")
    print(f"Puntuación Z del Experimento: {puntuacion_z:.4f}σ")
    print("================================================================")

if __name__ == "__main__":
    simular_modelo_triangular(14141)
