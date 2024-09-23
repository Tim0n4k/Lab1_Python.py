import math
n = 2
k = 0
z = 1

while z <= 51:
    k = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            k = k + 1

    if k == 1:
        print(z, n, sep=". ")
        z = z + 1

    n = n + 1