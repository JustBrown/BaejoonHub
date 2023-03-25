A = input()
B = input()
numbers = ''.join(a+b for a, b in zip(A,B))
while len(numbers)>2:
    numbers = ''.join(str((int(numbers[i])+int(numbers[i+1]))%10) for i in range(len(numbers)-1))
print(numbers)