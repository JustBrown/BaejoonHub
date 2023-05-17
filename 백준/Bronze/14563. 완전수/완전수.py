t = int(input())
nums = list(map(int, input().split()))
for n in nums:
    sum_fac = 0
    for i in range(1, n):
        if n%i==0:
            sum_fac+=i
    print('Perfect' if sum_fac==n else ('Deficient' if sum_fac<n else 'Abundant'))