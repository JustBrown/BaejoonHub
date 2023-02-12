arr = input()
stack = ''
result = 0
for i in range(len(arr)):
    if i==0:
        result += 10
    else:
        if stack[-1] == arr[i]:
            result += 5
        else:
            result += 10
    stack += arr[i]

print(result)