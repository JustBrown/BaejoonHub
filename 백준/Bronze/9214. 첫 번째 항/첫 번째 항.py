no = 1
while True:
    n = input()
    if n=='0': break

    if len(n)%2==1:
        print(f'Test {no}: {n}')
        no += 1
        continue

    nx_n = ''
    while True:
        nx_n = ''.join([int(n[i])*n[i+1] for i in range(0,len(n),2)])
        if len(nx_n)%2==1 or n==nx_n: 
            break
        n = nx_n
    
    print(f'Test {no}: {nx_n}')
    no += 1