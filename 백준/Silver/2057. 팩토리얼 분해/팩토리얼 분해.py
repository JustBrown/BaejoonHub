from math import factorial

N = int(input())
isFact = False
factList = [factorial(i) for i in range(0, 20) if factorial(i) <= N]
# print(factList)
while N >= 0:
    factList = list(filter(lambda x: x <= N, factList))
    # print("factList:", factList,"N:", N)
    if len(factList) == 0:
        break
    N -= factList.pop()
    if N <= 0:
        if N == 0:
            isFact = True
        break

print('YES' if isFact else 'NO')