def modularExponentiation(x, n, MM):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return modularExponentiation((x * x) % MM, n / 2, MM)
    else:
        return (x * modularExponentiation((x * x) % MM, (n - 1) / 2, MM)) % MM


def modInverse(x, MM):
    x = x % MM
    for b in range(1, MM):
        if (x * b) % MM == 1:
            return b
    return -1


# N, M = map(int, input().split())
# amodc = modularExponentiation(10, N, M)
# invmmodm = modInverse(M, M)
# print(invmmodm)
# res = (amodc * invmmodm) % M
# print(res)
