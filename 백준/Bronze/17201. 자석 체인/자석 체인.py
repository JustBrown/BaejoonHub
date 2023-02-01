n = int(input())
mag = input()

isconnect = True
for i in range(2*n-1):
    if mag[i]==mag[i+1]:
        isconnect = False
        break

print('Yes' if isconnect else 'No')