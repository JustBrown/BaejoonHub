from math import log10

while True:
    try:
        input_data = input()
    except EOFError:
        break
    n, b, m = map(float, input_data.split())
    print(int((log10(m)-log10(n))/log10(1+0.01*b))+1)