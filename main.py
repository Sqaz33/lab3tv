from math import factorial as fact
from math import pi


def integral_term(n: int, t) -> float:
    term = ((-1)**n * t**(2*n)) / (2**n * fact(n))
    return term * t / (2 * n + 1)


def integral(x1, x2) -> float:
    integral1 = sum(integral_term(n, x1) for n in range(100))
    integral2 = sum(integral_term(n, x2) for n in range(100))
    return integral1 - integral2


def laplace(x) -> float:
    return 1 / ((2*pi)**0.5) * integral(x, 0)


if __name__ == '__main__':
    print(laplace(1.22))

