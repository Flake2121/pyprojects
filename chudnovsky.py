import math
from decimal import Decimal, getcontext

def chudnovsky_algorithm(n):
    getcontext().prec = n + 2
    C, M, L, X, S = 426880 * Decimal(math.sqrt(10005)), Decimal(1), Decimal(13591409), Decimal(1), Decimal(13591409)
    for k in range(1, n + 1): M, L, X, S = M * -(6 * k - 5) * (2 * k - 1) * (6 * k - 1), L + 545140134, X * -262537412640768000, S + Decimal(M * L) / Decimal(10005 ** k) / X
    return str(C / S)[:-1]
n = 100
print(chudnovsky_algorithm(n))
