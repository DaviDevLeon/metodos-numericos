import math
from factory import SolverFactory

def main():
    print("========================================")
    print("   EQUIPO 3 SOLVER DE MÉTODOS NUMÉRICOS ")
    print("   Arquitectura con POO y SOLID         ")
    print("========================================")

    def mi_funcion(x):
        return x**3 - x - 2

    def mi_derivada(x):
        return 3*(x**2) - 1

    print("\nFunción a resolver: f(x) = x^3 - x - 2")
    print("1. Bisección")
    print("2. Newton-Raphson")
    
    opcion = input("\n¿Cuál método quieres resolver hoy? (1/2): ").strip()

    try:
        if opcion == '1':
            solver = SolverFactory.get_solver('biseccion')
            raiz = solver.solve(mi_funcion, a=1, b=2, tol=1e-5)
            
        elif opcion == '2':
            solver = SolverFactory.get_solver('newton')
            raiz = solver.solve(mi_funcion, df=mi_derivada, x0=1.0, tol=1e-5)
            
        else:
            print("No mames, escoge 1 o 2.")
            return

        print(f"\n>>> RESULTADO FINAL: La raíz es aproximadamente {raiz:.6f}")
        print(">>> Estado: Éxito. Arquitectura validada.")

    except Exception as e:
        print(f"\n!!! ERROR CRÍTICO EN EL SISTEMA: {e}")

if __name__ == "__main__":
    main()