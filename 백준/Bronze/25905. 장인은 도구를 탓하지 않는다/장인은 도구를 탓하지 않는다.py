P = sorted([float(input()) for _ in range(10)])[1:]
result = 1
for i, p, in enumerate(P, 1):
    result *= p/i*10
print(f'{result:.7}')