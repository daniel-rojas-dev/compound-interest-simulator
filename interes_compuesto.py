def calcular_interes_compuesto(capital_inicial, tasa_interes, frecuencia, tiempo_años):
    """
    Calcula el monto final utilizando la fórmula est'andar del interés compuesto: A = P * (1 + r / n) ** (n * t)

    Parámetros:
    capital_inicial (float): El capital inicial invertido.
    tasa_interes (float): La tasa de interés anual en forma decimal (por ejemplo, 0.05 para 5%).
    frecuencia (int): El número de veces que se capitaliza el interés por año.
    tiempo_años (float): El tiempo en años que el dinero está invertido.

    Retorna:
    float: El monto final después de aplicar el interés compuesto.
    """
    monto_final = capital_inicial * (1 + tasa_interes / frecuencia) ** (frecuencia * tiempo_años)
    return monto_final

def main():
    """Punto de entrada principal de la aplicación."""
    try:
        print("--- Calculador de interes compuesto ---")
        capital_inicial = float(input("Ingrese el capital inicial: "))
        tasa_interes_entera = int(input("Ingrese la tasa de interés anual (Ej. 5%): "))
        frecuencia = int(input("Ingrese la frecuencia de capitalización anual: "))
        tiempo_años = float(input("Ingrese el tiempo en años: "))

        tasa_interes = tasa_interes_entera / 100

        monto = calcular_interes_compuesto(capital_inicial, tasa_interes, frecuencia, tiempo_años)
        print(f"\n✅ El monto final después de {tiempo_años} años es: {monto:.2f}")
    except ValueError:
        print("❌ Error: Por favor, ingrese solo valores numéricos.")

if __name__ == "__main__":
    main()