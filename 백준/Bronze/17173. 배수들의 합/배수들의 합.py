n, m = map(int, input().split())
nums = [False] * (n+1)
for i in map(int, input().split()):
    for j in range(i, n+1, i):
        if not nums[j]: 
            nums[j] = True

result = 0
for i in range(2, n+1):
    if nums[i]:
        result += i
print(result)