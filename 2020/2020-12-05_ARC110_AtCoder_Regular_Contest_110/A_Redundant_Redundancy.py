def compute_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def compute_lcm(x, y):
    lcm = (x * y) // compute_gcd(x, y)
    return lcm


N = int(input())
x_num = 1
for number in range(1, N + 1):
    x_num = compute_lcm(x_num, number)
print(x_num + 1)
