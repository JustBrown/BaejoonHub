import sys
input = sys.stdin.readline

result = 0
for _ in range(int(input())):
    dict_num = {i: 0 for i in range(1, 7)}
    dict_cnt = {i: [] for i in range(5)}
    nums = list(map(int, input().split()))

    for n in nums:
        dict_num[n] += 1
    for n in dict_num:
        dict_cnt[dict_num[n]].append(n)

    if dict_cnt[4]:
        temp = 50000+dict_cnt[4][0]*5000
    elif dict_cnt[3]:
        temp = 10000+dict_cnt[3][0]*1000
    elif dict_cnt[2]:
        if len(dict_cnt[2]) == 2:
            temp = 2000+sum([500*n for n in dict_cnt[2]])
        else:
            temp = 1000+dict_cnt[2][0]*100
    else:
        temp = max(nums)*100
    
    if result < temp:
        result = temp

print(result)