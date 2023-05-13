def factorial(N):
    return 1 if N==0 else N*factorial(N-1)
print(factorial(int(input())))