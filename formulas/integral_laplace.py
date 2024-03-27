from math import factorial as fact
from math import pi


class IntegralLaplace:
    def integral_term(self, n: int, t) -> float:
        term = ((-1)**n * t**(2*n)) / (2**n * fact(n))
        return term * t / (2 * n + 1)

    def integral(self, x1, x2) -> float:
        integral1 = sum(self.integral_term(n, x1) for n in range(150))
        integral2 = sum(self.integral_term(n, x2) for n in range(150))
        return integral1 - integral2

    def laplace(self, n: int, m1: int, m2: int, x: int, p: float) -> float:
        q = 1 - p

        x1 = (m1 - n*p) / (n * p * q)**0.5
        x2 = (m2 - n*p) / (n * p * q)**0.5

        integral = self.integral(x2, x1)

        return 1 / ((2*pi)**0.5) * integral
