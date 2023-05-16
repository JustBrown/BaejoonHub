from math import ceil

m = int(input())
n = int(input())

PSM = []
for i in range(ceil(m**.5), int(n**.5)+1):
    PSM.append(i**2)

print(-1) if len(PSM)==0 else print(sum(PSM), PSM[0])