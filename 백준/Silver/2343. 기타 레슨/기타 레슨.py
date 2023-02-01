def binary_search(start, end):
    global result

    if start > end:
        return 
    medium = (start+end)//2
    
    storages = [0]*m
    idx = 0
    for i in range(len(lectures)):
        if idx<m-1:
            storages[idx] += lectures[i]
            if storages[idx] >= medium:
                if storages[idx] > medium:
                    storages[idx]-=lectures[i]
                    storages[idx+1]+=lectures[i]
                idx += 1
        elif idx==m-1:
            storages[idx] += lectures[i]

    # 기준은 storages[-1]과 medium의 대소비교
    result = min(result, max(storages))
    if storages[-1] < medium:      # storage 크기가 널널했다. >> 줄여보자
        end = medium-1
    else:                           # storage 크기가 부족했다. >> 늘려보자
        start = medium+1
    binary_search(start, end)

n, m = map(int, input().split())
lectures = list(map(int,input().split()))

start, end = min(lectures), sum(lectures)
result = end
binary_search(start, end)

print(result)