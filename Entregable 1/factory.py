from numerical_methods.bisection import BisectionSolver
from numerical_methods.newton import NewtonRaphsonSolver
from numerical_methods.base import NumericalMethodStrategy

class SolverFactory:
    @staticmethod
    def get_solver(method_type: str) -> NumericalMethodStrategy:
        if method_type == 'biseccion':
            return BisectionSolver()
        elif method_type == 'newton':
            return NewtonRaphsonSolver()
        else:
            raise ValueError(f"Método '{method_type}' no encontrado.")