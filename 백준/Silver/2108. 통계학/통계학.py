import sys
input = sys.stdin.readline

n = int(input())
nums, dict_nums = [], {i: 0 for i in range(-4000, 4001)}
mean, median, mode, ran = 0, 0, 0, 0
for _ in range(n):
    num = int(input())
    nums.append(num)
    dict_nums[num] += 1
nums.sort()

print(round(sum(nums)/len(nums)))                                   # 산술평균
print(nums[len(nums)//2])                                           # 중앙값
max_count = dict_nums[max(dict_nums, key=lambda x: dict_nums[x])]   # 최빈값
modes = [i for i in range(-4000, 4001) if dict_nums[i]==max_count]
print(modes[0] if len(modes)==1 else modes[1])                    
print(max(nums)-min(nums))                                          # 범위