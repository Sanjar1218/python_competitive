def digital_root(n):
    while len(str(n))!=1:
        n = sum(map(int, list(str(n))))
    return n

print(digital_root(942))