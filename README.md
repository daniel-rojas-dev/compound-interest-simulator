# compound-interest-simulator
Motor de cálculo financiero desarrollado en Python enfocado en buenas prácticas de programación, manejo de excepciones y documentación técnica.

# 📈 Financial Logic Engine - Python

Este proyecto es una demostración de **limpieza de código (Clean Code)**, manejo de excepciones y documentación técnica en Python. El objetivo principal es mostrar una estructura de software profesional y mantenible.

## 🎯 Propósito del Proyecto
Demostrar habilidades en:
* **Robustez:** Uso de bloques `try-except` para validación de entradas.
* **Documentación:** Docstrings (PEP 257) detallados para mantenimiento.
* **Modularidad:** Separación de la lógica de cálculo y la interfaz.
* **Buenas Prácticas:** Nomenclatura semántica y uso de `if __name__ == "__main__":`.

## 🛠️ Tecnologías
* **Lenguaje:** Python 3.x
* **Paradigma:** Programación Modular.

## 📋 Ejemplo de Ejecución
```
--- Calculador de interés compuesto ---
Ingrese el capital inicial: 1000
Ingrese la tasa de interés anual (Ej. 5%): 5
Ingrese la frecuencia de capitalización: 2
Ingrese el tiempo en años: 12

✅ Resultado: El monto final acumulado es: 1808.73
```

## 🏗️ Lógica del Algoritmo
El motor utiliza la fórmula financiera estándar de interés compuesto:

```text
A = P * (1 + r/n)^(nt)
```
Donde:

  * **A**: Monto final.

  * **P**: Capital inicial.

  * **r**: Tasa de interés (decimal).

  * **n**: Frecuencia de capitalización.

  * **t**: Tiempo en años.

## 🧠 Reflexión Técnica
Se priorizó la legibilidad sobre la brevedad. Un código bien documentado reduce costos de mantenimiento y facilita el trabajo en equipo en entornos de ingeniería de software.
