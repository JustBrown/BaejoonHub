arr = input()
stack = ''
result = 0
for i in range(len(arr)):
    if not stack or stack[-1]!=arr[i]:
        result += 10
    else:
        result += 5
    stack += arr[i]

print(result)