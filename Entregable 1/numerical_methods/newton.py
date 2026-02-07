from .base import NumericalMethodStrategy
from typing import Callable

class NewtonRaphsonSolver(NumericalMethodStrategy):
    def solve(self, f: Callable[[float], float], **kwargs) -> float:
        x0 = kwargs.get('x0')
        df = kwargs.get('df') # Derivada de f
        tol = kwargs.get('tol', 1e-6)
        max_iter = kwargs.get('max_iter', 100)

        if x0 is None:
            raise ValueError("Necesito un punto inicial 'x0' para empezar.")
        if df is None:
            raise ValueError("Newton-Raphson necesita la derivada 'df'.")

        print(f"\n--- Iniciando Newton-Raphson desde x0 = {x0} ---")

        x = x0
        for i in range(max_iter):
            fx = f(x)
            dfx = df(x)

            if dfx == 0:
                raise ValueError("La derivada es cero. División por cero inminente. Cancelando.....")

            x_new = x - (fx / dfx)
            error = abs(x_new - x)

            self._log_step(i + 1, x_new, error)

            if error < tol:
                print("Convergencia alcanzada.")
                return x_new
            
            x = x_new

        return x