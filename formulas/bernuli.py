from math import factorial as fact
from inequality_operations import InequalityOperations


class BernuliCalcul:
    def comb(self, m, n) -> int:
        if m > n:
            return 0
        return fact(n) / (fact(n - m) * fact(m))

    def bernuli(self, n: int, m: int, p: float) -> float:
        q = 1 - p
        return self.comb(m, n) * p**m * q**(n-m)

    def bernuli_in_range(self, n: int, m1: int, m2: int, p: float) -> float:
        return sum(self.bernuli(n, m, p) for m in range(m1, m2+1))

    def bernuli_calcul(self, n: int, m1: int, m2: int, p: float, operation: InequalityOperations) -> float:
        match operation:
            case InequalityOperations.equal:
                return self.bernuli(n, m1, p)
            case InequalityOperations.less:
                return self.bernuli_in_range(n, 0, m1-1, p)
            case InequalityOperations.more_or_equal:
                return self.bernuli_in_range(n, m1, n, p)
            case InequalityOperations.between:
                return self.bernuli_in_range(n, m1, m2, p)

    def bernuli_polynomial(self, m: list[int], p: list[float]) -> float:
        n = sum(m)

        mult1 = 1
        for i in m:
            mult1 *= fact(i)

        mult2 = 1
        for i, j in zip(m, p):
            mult2 *= j**i

        return fact(n) / mult1 * mult2