n = int(input())
array = [tuple(map(int, input().split())) for _ in range(n)]
sorted_arr = sorted(array, key=lambda x:(-x[0], x[1], x[2]))
print(array.index(sorted_arr[0])+1)