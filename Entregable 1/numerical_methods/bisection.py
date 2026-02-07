from .base import NumericalMethodStrategy
from typing import Callable

class BisectionSolver(NumericalMethodStrategy):
    def solve(self, f: Callable[[float], float], **kwargs) -> float:
        a = kwargs.get('a')
        b = kwargs.get('b')
        tol = kwargs.get('tol', 1e-6)
        max_iter = kwargs.get('max_iter', 100)

        if a is None or b is None:
            raise ValueError("Para bisección necesito los límites 'a' y 'b'.")

        if f(a) * f(b) >= 0:
            raise ValueError("El intervalo no sirve, la función no cruza el eje X ahí.")

        print(f"\n--- Iniciando Bisección en el intervalo [{a}, {b}] ---")
        
        c_old = a
        for i in range(max_iter):
            c = (a + b) / 2
            error = abs(c - c_old)
            
            self._log_step(i + 1, c, error)
            
            if f(c) == 0 or error < tol:
                print("Raíz encontrada")
                return c
            
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
            
            c_old = c
            
        print("Se acabaron las iteraciones.")
        return c