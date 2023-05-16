def isPSM(num):
    factors = []
    # 소인수분해
    d = 2
    while num >= d:
        if num % d == 0:
            factors.append(d)
            num //= d
        else:
            d += 1
    
    # 완전제곱수 여부 확인
    for i in set(factors):
        if factors.count(i)%2!=0:
            return False
    return True

m = int(input())
n = int(input())

PSM = []
for i in range(m, n+1):
    if isPSM(i):
        PSM.append(i)

print(-1) if len(PSM) == 0 else print(sum(PSM), PSM[0], sep='\n')