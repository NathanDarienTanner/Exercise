def prime(x):
    y = True
    for i in range(2, x):
        if x % i == 0:
            y = False
            break
    if x == 1:
        y = False
    return y

print(prime(1))