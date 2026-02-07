# 🚀 EQUIPO 3 - SOLVER DE MÉTODOS NUMÉRICOS (Edición Empresarial)

![Estado de Compilación](https://img.shields.io/badge/compilaci%C3%B3n-pasando-brightgreen)
![Cobertura](https://img.shields.io/badge/cobertura-100%25-green)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Arquitectura](https://img.shields.io/badge/arquitectura-S%C3%93LIDA-orange)
![Código Espagueti](https://img.shields.io/badge/espagueti-0%25-red)

> **"Encontrar raíces no debería ser difícil. Debería ser una obra de arte arquitectónica."**

## 📖 Resumen General

**SOLVER EQUIPO 3** es una solución de alto rendimiento, modular y escalable diseñada para la resolución de ecuaciones no lineales. Olvida los guiones básicos de calculadora; esto es ingeniería de software profesional aplicada a las matemáticas.

Este proyecto implementa algoritmos numéricos clásicos bajo una arquitectura estricta orientada a objetos (POO), aplicando los principios **SOLID** y Patrones de Diseño (**Estrategia** y **Fábrica**) para garantizar un desacoplamiento total entre la lógica de negocio y la implementación matemática.

Básicamente: **Está sobrado de cariño para una tarea, pero la excelencia no es negociable.**

---

## Arquitectura y Patrones de Diseño

Este sistema no fue simplemente "escrito"; fue **arquitectado**.

### El Patrón Estrategia (Strategy Pattern)
Utilizamos el patrón **Estrategia** para encapsular cada algoritmo numérico (Bisección, Newton-Raphson) en su propia clase. Esto permite intercambiar algoritmos en tiempo de ejecución sin alterar el código cliente (`main.py`).

* **`NumericalMethodStrategy` (Clase Base Abstracta):** El contrato sagrado. Define la interfaz `solve()` (resolver) que todos deben respetar.
* **`BisectionSolver`:** Implementación concreta para robustez (convergencia garantizada).
* **`NewtonRaphsonSolver`:** Implementación concreta para velocidad (convergencia cuadrática).

### El Patrón Fábrica (Factory Pattern)
Implementamos una **`SolverFactory`** para centralizar la creación de instancias. Esto cumple con el *Principio Abierto/Cerrado*: podemos agregar 50 métodos nuevos sin tocar una sola línea del código existente que los consume.

---

## Estructura del Proyecto

Una estructura de carpetas limpia y profesional.

```text
.
├── numerical_methods/       # El Núcleo de la Lógica
│   ├── __init__.py          # Inicialización del paquete
│   ├── base.py              # Segregación de Interfaz (Clase Abstracta)
│   ├── bisection.py         # Estrategia Concreta A
│   └── newton.py            # Estrategia Concreta B
├── factory.py               # Auxiliar de Inyección de Dependencias
├── main.py                  # Punto de Entrada y Orquestador
└── README.md                # Esta documentación