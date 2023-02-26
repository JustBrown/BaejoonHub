s1, s2, s3 = map(int, input().split())
nums = [0]*(s1*s2*s3)
for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            nums[i+j+k]+=1

print(nums.index(max(nums)))