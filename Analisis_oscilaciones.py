
"""
Modelo López-Rodríguez: Operador de Descenso Triangular, Cruces por Cero 
y Análisis de Fourier sobre la onda continua de todas las filas.
Autor: Roberto López Rodríguez
Valladolid, España
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# =====================================================================
# 1. MOTOR DEL MODELO LÓPEZ-RODRÍGUEZ (Operador de Descenso)
# =====================================================================
def generar_decimales_dummy(semilla, total_digitos):
    """
    Genera dígitos deterministas de alta calidad simulando la distribución
    de Pi o E para el experimento.
    """
    np.random.seed(semilla)
    return np.random.randint(0, 10, size=total_digitos)

def analizar_constante_triangular(digitos, max_filas=300):
    """
    Aplica el Operador de Descenso Triangular con bono de +10.
    Calcula la desviación D*(n) fila a fila de forma continua.
    """
    desviaciones = []
    puntero = 0
    suma_acumulada_real = 0.0
    
    for n in range(1, max_filas + 1):
        if puntero + n > len(digitos):
            break
            
        fila = digitos[puntero : puntero + n]
        puntero += n
        
        # Calcular suma de la fila aplicando la Regla de Memoria Dinámica (+10)
        suma_fila = fila[0] if len(fila) > 0 else 0
        for i in range(1, len(fila)):
            d_actual = fila[i]
            d_previo = fila[i-1]
            if d_actual < d_previo:
                suma_fila += (d_actual + 10)  # Penalización / Bono por descenso
            else:
                suma_fila += d_actual
                
        suma_acumulada_real += suma_fila
        
        # Fórmula del Desvío Teórico Acumulado: D*(n) = T*(n) - 4.5 * n^2
        D_n = suma_acumulada_real - 4.5 * (n**2)
        desviaciones.append(D_n)
        
    return np.array(desviaciones)

# =====================================================================
# 2. ANALIZADOR DE CRUCES POR CERO (Análisis de Oscilación)
# =====================================================================
def detectar_cruces_por_cero(trayectoria):
    """
    Detecta los índices y valores donde la señal cruza el eje horizontal (cero).
    """
    cruces = []
    for i in range(len(trayectoria) - 1):
        if trayectoria[i] * trayectoria[i+1] < 0:
            cruces.append({
                "fila": i + 1,
                "antes": trayectoria[i],
                "despues": trayectoria[i+1]
            })
    return cruces

# =====================================================================
# 3. EJECUCIÓN DEL EXPERIMENTO (300 FILAS CONTINUAS)
# =====================================================================
max_filas = 300
total_digitos_necesarios = int(max_filas * (max_filas + 1) / 2)

# Generación de señales digitales continuas
digitos_pi = generar_decimales_dummy(semilla=314159, total_digitos=total_digitos_necesarios)
digitos_e = generar_decimales_dummy(semilla=271828, total_digitos=total_digitos_necesarios)

# Trayectorias completas de la desviación D*(n) tomadas como ondas continuas
D_pi = analizar_constante_triangular(digitos_pi, max_filas=max_filas)
D_e = analizar_constante_triangular(digitos_e, max_filas=max_filas)
D_suma = D_pi + D_e

# Generador Sintético (Mersenne Twister) para contraste de deriva inercial
np.random.seed(42)
D_mersenne = np.cumsum(np.random.normal(loc=0.0, scale=12.0, size=max_filas))

# Detección de cruces por cero en la onda completa
cruces_pi = detectar_cruces_por_cero(D_pi)
cruces_e = detectar_cruces_por_cero(D_e)
cruces_mersenne = detectar_cruces_por_cero(D_mersenne)

# =====================================================================
# 4. ANÁLISIS DE FOURIER COMO ONDA CONTINUA UNIFICADA
# =====================================================================
# En lugar de promediar o segmentar por filas, tratamos el vector D*(n)
# completo como una única señal en el tiempo continuo (t = 1, 2, ..., N).
N = len(D_pi)  # Longitud total de la onda (300 puntos continuos de evolución)
Fs = 1.0       # Frecuencia de muestreo (1 muestra por incremento de fila)

# Eliminamos la tendencia lineal/media para concentrarnos únicamente en las oscilaciones de onda
D_pi_detrend = D_pi - np.mean(D_pi)
D_e_detrend = D_e - np.mean(D_e)
D_suma_detrend = D_suma - np.mean(D_suma)

# Cálculo de la Transformada Rápida de Fourier (FFT) sobre toda la onda
yf_pi = fft(D_pi_detrend)
yf_e = fft(D_e_detrend)
yf_suma = fft(D_suma_detrend)

# Vector de frecuencias continuas
xf = fftfreq(N, 1/Fs)[:N//2]

# Amplitud física del espectro de onda completa
amplitud_pi = 2.0/N * np.abs(yf_pi[0:N//2])
amplitud_e = 2.0/N * np.abs(yf_e[0:N//2])
amplitud_suma = 2.0/N * np.abs(yf_suma[0:N//2])

# Identificación de la frecuencia dominante real de toda la onda
f_dom_pi = xf[np.argmax(amplitud_pi[1:]) + 1]
f_dom_e = xf[np.argmax(amplitud_e[1:]) + 1]
f_dom_suma = xf[np.argmax(amplitud_suma[1:]) + 1]

# Imprimir consola descriptiva de física de ondas
print("="*75)
print("  ANÁLISIS DE ONDA CONTINUA Y ESPECTRO GLOBAL (Modelo López-Rodríguez)")
print("="*75)
print(f"| {'SISTEMA':<25} | {'CRUCES TOTALES':<16} | {'FREQ. DOMINANTE':<16} | {'PERÍODO (T)':<10} |")
print("-"*75)
print(f"| {'Onda Pi (Completa)':<25} | {len(cruces_pi):^16} | {f_dom_pi:^16.4f} Hz | {1/f_dom_pi:>8.2f} f  |")
print(f"| {'Onda E (Completa)':<25} | {len(cruces_e):^16} | {f_dom_e:^16.4f} Hz | {1/f_dom_e:>8.2f} f  |")
print(f"| {'Onda Suma (Pi + E)':<25} | {len(detectar_cruces_por_cero(D_suma)):^16} | {f_dom_suma:^16.4f} Hz | {1/f_dom_suma:>8.2f} f  |")
print(f"| {'Mersenne (Sintético)':<25} | {len(cruces_mersenne):^16} | {'N/A':^16} | {'N/A':>10} |")
print("-"*75)
print(f"Frecuencia Teórica de Batido Colectivo: {abs(f_dom_pi - f_dom_e):.4f} Hz")
print(f"Ciclo Completo de Modulación de Batido: {1/abs(f_dom_pi - f_dom_e):.2f} unidades de tiempo (filas)")
print("="*75)

# =====================================================================
# 5. DIBUJOS DE ONDAS EN VENTANAS SEPARADAS
# =====================================================================

# --- VENTANA 1: Dinámica de Ondas de Desviación ---
plt.figure(num="1. Ondas de Desviación Continua", figsize=(11, 5.5))
plt.plot(D_pi, label=f"Onda Pi (Cruces: {len(cruces_pi)})", color="#1f77b4", linewidth=2)
plt.plot(D_e, label=f"Onda E (Cruces: {len(cruces_e)})", color="#ff7f0e", linewidth=2)
plt.plot(D_mersenne, label=f"Mersenne Twister (Cruces: {len(cruces_mersenne)})", color="#7f7f7f", linestyle="--", alpha=0.8)
plt.axhline(0, color="black", linestyle="-", linewidth=1, alpha=0.9)

# Dibujar puntos exactos de cruce por cero en la onda de Pi
indices_cruces_pi = [c['fila'] - 1 for c in cruces_pi]
valores_cruces_pi = [0] * len(cruces_pi)
plt.scatter(indices_cruces_pi, valores_cruces_pi, color="red", zorder=5, label="Cruces por Cero (Pi)")

plt.title("Evolución de la Onda Continua de Desviación D*(n)\n(Modelo López-Rodríguez)", fontsize=11, fontweight='bold')
plt.xlabel("Tiempo de Evolución Continua (Filas n)")
plt.ylabel("Amplitud de Desviación D*(n)")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper left")
plt.tight_layout()

# --- VENTANA 2: Interferencia Ondulatoria y Batido Colectivo ---
plt.figure(num="2. Interferencia y Batido", figsize=(11, 5.5))
plt.plot(D_suma, label="Onda Resultante (Pi + E)", color="#2ca02c", linewidth=2.5)
plt.plot(D_pi, color="#1f77b4", alpha=0.25, label="Onda Pi (Componente)")
plt.plot(D_e, color="#ff7f0e", alpha=0.25, label="Onda E (Componente)")
plt.axhline(0, color="black", linestyle="-", linewidth=1, alpha=0.9)

# Resaltar envolvente del batido de forma visual básica (máximos locales)
plt.title("Interferencia Física de las Ondas Colectivas de Pi y E\n(Superposición de Ondas y Fenómeno de Batido)", fontsize=11, fontweight='bold')
plt.xlabel("Tiempo de Evolución Continua (Filas n)")
plt.ylabel("Amplitud Combinada de Desvío")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper left")
plt.tight_layout()

# --- VENTANA 3: Espectro de Fourier de la Onda Completa ---
plt.figure(num="3. Espectro Espectral de Fourier de Onda Completa", figsize=(11, 5.5))
# Graficamos a partir del índice 1 para evitar el componente de frecuencia 0 (DC)
plt.plot(xf[1:], amplitud_pi[1:], label=f"Espectro Pi (Pico: {f_dom_pi:.4f} Hz)", color="#1f77b4", linewidth=2)
plt.plot(xf[1:], amplitud_e[1:], label=f"Espectro E (Pico: {f_dom_e:.4f} Hz)", color="#ff7f0e", linewidth=2)
plt.plot(xf[1:], amplitud_suma[1:], label=f"Espectro Interferencia (Pico: {f_dom_suma:.4f} Hz)", color="#2ca02c", linewidth=2, linestyle="-.")

# Destacar el armónico dominante de la onda Pi
plt.axvline(f_dom_pi, color="#1f77b4", linestyle=":", alpha=0.7, label=f"Armónico Principal Pi ({f_dom_pi:.3f} Hz)")
plt.axvline(f_dom_e, color="#ff7f0e", linestyle=":", alpha=0.7, label=f"Armónico Principal E ({f_dom_e:.3f} Hz)")

plt.title("Análisis Espectral de Fourier (FFT) de la Onda Completa\n(Sintonización en el Dominio de la Frecuencia)", fontsize=11, fontweight='bold')
plt.xlabel("Frecuencia (Ciclos por Unidad de Fila o Hz)")
plt.ylabel("Densidad de Amplitud Espectral (Energía)")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper right")
plt.tight_layout()

# Renderizado de todas las ventanas físicas independientes
plt.show()
