from collections import Counter

nums = []
for _ in range(10):
    nums.append(int(input()))

print(sum(nums)//10, Counter(nums).most_common()[0][0])