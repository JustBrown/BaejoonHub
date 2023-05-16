from math import ceil

m = int(input())
n = int(input())

sum_sqr, min_sqr = 0, 0
for i in range(ceil(m**.5), int(n**.5)+1):
    sqr = i**2
    if min_sqr == 0:
        min_sqr = sqr
    sum_sqr += sqr
    

print(-1) if sum_sqr==0 else print(sum_sqr, min_sqr, sep='\n')