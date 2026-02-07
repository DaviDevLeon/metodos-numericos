from abc import ABC, abstractmethod
from typing import Callable, Optional

class NumericalMethodStrategy(ABC):
    
    @abstractmethod
    def solve(self, f: Callable[[float], float], **kwargs) -> float:
        """
        Método abstracto que todas las implementaciones deben tener.
        f: La función a la que le buscamos la raíz.
        kwargs: Argumentos extra como limites (a, b) o derivadas (df).
        """
        pass

    def _log_step(self, iteration: int, x: float, error: float):
        print(f"[ITERACIÓN {iteration}] x = {x:.6f} | Error aprox = {error:.6f}")