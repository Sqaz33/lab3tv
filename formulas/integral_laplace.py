from math import factorial as fact
from math import pi


class IntegralLaplace:
    def integral_term(self, n: int, t) -> float:
        term = ((-1)**n * t**(2*n)) / (2**n * fact(n))
        return term * t / (2 * n + 1)

    def integral(self, x1, x2) -> float:
        integral1 = sum(self.integral_term(n, x1) for n in range(70))
        integral2 = sum(self.integral_term(n, x2) for n in range(70))
        return integral1 - integral2

    def x1(self, n: int, p: float, m1: int) -> float:
        q = 1 - p
        return (m1 - n*p) / (n * p * q)**0.5

    def x2(self, n: int, p: float, m2: int) -> float:
        q = 1 - p
        return (m2 - n*p) / (n * p * q)**0.5

    def laplace_integer(self, n: int, m1: int, m2: int, p: float) -> float:
        q = 1 - p

        x1 = self.x1(n, p, m1)
        x2 = self.x2(n, p, m2)

        integral = self.integral(x2, x1)

        return 1 / ((2*pi)**0.5) * integral
