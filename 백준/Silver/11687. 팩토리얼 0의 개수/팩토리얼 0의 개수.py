def binary_search(start, end):
    medium = (start+end)//2
    end_zero_cnt, temp = 0, medium
    while temp!=0:
        end_zero_cnt += temp//5
        temp //= 5

    if start>=end:
        if end_zero_cnt == m: 
            return medium
        else:
            return -1

    if end_zero_cnt >= m:
        return binary_search(start, medium)
    else:
        return binary_search(medium+1, end)

m = int(input())
result = binary_search(1, 400000016)
print(result)