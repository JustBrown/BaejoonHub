n, p = map(int, input().split())
temp = (n*n)%p
nums = [n, temp]
while True:
    temp = (temp*n)%p
    if temp in nums:
        print(len(nums[nums.index(temp):]))
        break
    nums.append(temp)