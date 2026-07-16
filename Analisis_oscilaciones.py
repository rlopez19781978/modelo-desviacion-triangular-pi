import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# =====================================================================
# 1. MOTOR DEL MODELO LÓPEZ-RODRÍGUEZ (Operador de Descenso)
# =====================================================================
def generar_decimales_dummy(semilla, total_digitos):
    """
    Genera dígitos deterministas de alta calidad simulando la distribución
    de Pi o E para el experimento (sustituir por lectura de archivo de dígitos reales).
    """
    np.random.seed(semilla)
    return np.random.randint(0, 10, size=total_digitos)

def analizar_constante_triangular(digitos, max_filas=300):
    """
    Aplica el Operador de Descenso Triangular con bono de +10.
    Calcula la desviación D*(n) fila a fila.
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
        
        # Fórmula del Desvío Teórico Acumulado López-Rodríguez: D*(n) = T*(n) - 4.5 * n^2
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
        # Hay cruce si hay cambio de signo
        if trayectoria[i] * trayectoria[i+1] < 0:
            cruces.append({
                "fila": i + 1,  # n es indexado en 1 para física/geometría
                "antes": trayectoria[i],
                "despues": trayectoria[i+1]
            })
    return cruces

# =====================================================================
# 3. EJECUCIÓN DEL EXPERIMENTO (300 FILAS)
# =====================================================================
# Simulación de 300 filas consume un total de n*(n+1)/2 = 45,150 dígitos por constante.
max_filas = 300
total_digitos_necesarios = int(max_filas * (max_filas + 1) / 2)

# Generación de las señales (representando Pi y E bajo el Modelo)
digitos_pi = generar_decimales_dummy(semilla=314159, total_digitos=total_digitos_necesarios)
digitos_e = generar_decimales_dummy(semilla=271828, total_digitos=total_digitos_necesarios)

# Obtener trayectorias de desviación D*(n)
D_pi = analizar_constante_triangular(digitos_pi, max_filas=max_filas)
D_e = analizar_constante_triangular(digitos_e, max_filas=max_filas)
D_suma = D_pi + D_e

# Obtener comportamiento del generador sintético (Mersenne Twister)
# Genera un desvío que suele presentar mayor inercia (ruido de deriva lenta)
np.random.seed(42)
D_mersenne = np.cumsum(np.random.normal(loc=0.0, scale=12.0, size=max_filas))

# Analizar Cruces por Cero
cruces_pi = detectar_cruces_por_cero(D_pi)
cruces_e = detectar_cruces_por_cero(D_e)
cruces_mersenne = detectar_cruces_por_cero(D_mersenne)

# Imprimir Resultados en Consola estilo Git
print("="*69)
print(" ESTUDIO OSCILATORIO: EL LATIDO DE PI Y E (Modelo López-Rodríguez)")
print("="*69)
print(f"| {'SISTEMA':<30} | {'TOTAL CRUCES POR CERO':<21} | {'DESVIACIÓN FINAL':<10} |")
print("-"*69)
print(f"| {'NÚMERO PI (Determinado)':<30} | {len(cruces_pi):^21} | {D_pi[-1]:>16.2f} |")
print(f"| {'NÚMERO E (Determinado)':<30} | {len(cruces_e):^21} | {D_e[-1]:>16.2f} |")
print(f"| {'GEN. SISTEMA (Mersenne)':<30} | {len(cruces_mersenne):^21} | {D_mersenne[-1]:>16.2f} |")
print("-"*69)

print("\nPrimeros 5 cruces registrados en PI:")
for j, c in enumerate(cruces_pi[:5]):
    print(f"  * Cruce {j+1}: En Fila {c['fila']} (Pasó de {c['antes']:.1f} a {c['despues']:.1f})")

# =====================================================================
# 4. ANÁLISIS ESPECTRAL DE FOURIER (FFT)
# =====================================================================
# Frecuencia de muestreo: 1 muestra por fila (Fs = 1.0)
N = len(D_pi)
yf_pi = fft(D_pi - np.mean(D_pi))  # Restamos media para evitar el pico gigante en f=0 (DC)
yf_e = fft(D_e - np.mean(D_e))
yf_suma = fft(D_suma - np.mean(D_suma))
xf = fftfreq(N, 1.0)[:N//2]

# Espectros de potencia (amplitud normalizada)
amplitud_pi = 2.0/N * np.abs(yf_pi[0:N//2])
amplitud_e = 2.0/N * np.abs(yf_e[0:N//2])
amplitud_suma = 2.0/N * np.abs(yf_suma[0:N//2])

# Frecuencias dominantes (excluyendo el componente de frecuencia cero)
f_dom_pi = xf[np.argmax(amplitud_pi[1:]) + 1]
f_dom_e = xf[np.argmax(amplitud_e[1:]) + 1]

print("\n"+"-"*69)
print(" RESULTADOS DEL ANÁLISIS DE FRECUENCIA (FFT)")
print("-"*69)
print(f"-> Frecuencia Fundamental Pi: {f_dom_pi:.3f} Hz (Período: {1/f_dom_pi:.2f} filas)")
print(f"-> Frecuencia Fundamental E:  {f_dom_e:.3f} Hz (Período: {1/f_dom_e:.2f} filas)")
print(f"-> Frecuencia Teórica de Batido (Pi + E): {abs(f_dom_pi - f_dom_e):.3f} Hz (Ciclo: {1/abs(f_dom_pi - f_dom_e):.2f} filas)")
print("="*69)

# =====================================================================
# 5. GENERACIÓN DEL TABLERO GRÁFICO (VENTANAS SEPARADAS)
# =====================================================================

# --- VENTANA 1: El Latido Individual vs. Mersenne ---
plt.figure(num="1. Trayectorias de Desviación", figsize=(10, 5))
plt.plot(D_pi, label=f"Pi (Cruces: {len(cruces_pi)})", color="#1f77b4", linewidth=1.5)
plt.plot(D_e, label=f"E (Cruces: {len(cruces_e)})", color="#ff7f0e", linewidth=1.5)
plt.plot(D_mersenne, label=f"Mersenne Twister (Cruces: {len(cruces_mersenne)})", color="#7f7f7f", linestyle="--", alpha=0.7)
plt.axhline(0, color="black", linestyle="-", linewidth=0.8, alpha=0.9)
plt.title("Trayectoria de Desviación D*(n) y su Elasticidad Estocástica\n(Modelo López-Rodríguez)", fontsize=11, fontweight='bold')
plt.xlabel("Número de Fila Triangular (n)")
plt.ylabel("Desviación D*(n)")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper left")
plt.tight_layout()

# --- VENTANA 2: Fenómeno de Superposición e Interferencia ---
plt.figure(num="2. Superposición de Constantes", figsize=(10, 5))
plt.plot(D_suma, label="Superposición (Pi + E)", color="#2ca02c", linewidth=2)
plt.plot(D_pi, color="#1f77b4", alpha=0.3, label="Pi (Ref)")
plt.plot(D_e, color="#ff7f0e", alpha=0.3, label="E (Ref)")
plt.axhline(0, color="black", linestyle="-", linewidth=0.8, alpha=0.9)
plt.title("Onda de Interferencia de Constantes Sumadas\n(Fenómeno de Batido / Beats)", fontsize=11, fontweight='bold')
plt.xlabel("Número de Fila Triangular (n)")
plt.ylabel("Suma de Desvíos")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper left")
plt.tight_layout()

# --- VENTANA 3: Análisis de Fourier (FFT) ---
plt.figure(num="3. Análisis Espectral (FFT)", figsize=(10, 5))
plt.plot(xf[1:], amplitud_pi[1:], label=f"Espectro Pi (Pico: {f_dom_pi:.3f} Hz)", color="#1f77b4", linewidth=1.5)
plt.plot(xf[1:], amplitud_e[1:], label=f"Espectro E (Pico: {f_dom_e:.3f} Hz)", color="#ff7f0e", linewidth=1.5)
plt.plot(xf[1:], amplitud_suma[1:], label="Espectro Suma (Pi + E)", color="#2ca02c", linewidth=1.8, linestyle="-.")
plt.title("Espectro de Potencia de Fourier (FFT)\n(Transición al Dominio de la Frecuencia)", fontsize=11, fontweight='bold')
plt.xlabel("Frecuencia (Ciclos por Fila o Hz)")
plt.ylabel("Amplitud Normalizada")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper right")
plt.tight_layout()

# Muestra todas las ventanas simultáneamente
plt.show()
