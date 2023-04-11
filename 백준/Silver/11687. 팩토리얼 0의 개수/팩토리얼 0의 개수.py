def binary_search(start, end):
    
    # N!의 오른쪽 0의 개수 = N을 대상으로 5로 나눈 몫들의 합
    medium = (start+end)//2
    end_zero_cnt, temp = 0, medium
    while temp!=0:
        end_zero_cnt += temp//5
        temp //= 5

    # 결과 판단
    if start>=end:
        if end_zero_cnt == m: 
            return medium
        else:
            return -1
    
    # 재귀 판단 
    if end_zero_cnt >= m:
        return binary_search(start, medium)
    else:
        return binary_search(medium+1, end)

    
m = int(input())
result = binary_search(1, 5*10**8+1)
print(result)