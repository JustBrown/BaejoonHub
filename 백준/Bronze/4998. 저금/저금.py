while True:
    try:
        input_data = input()
    except EOFError:
        break
    n, b, m = map(float, input_data.split())
    cnt = 0
    while n<=m:
        n *= (1+0.01*b)
        cnt += 1
    print(cnt)