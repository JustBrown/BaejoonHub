n = int(input())
string = input()
B, S, idx = 0, 0, 0

for _ in range(n):
    idx = string.find('bigdata', idx)
    if idx == -1:
        S = n - B
        break
    B += 1
    idx+=1

print('bigdata?' if B>S else ('security!' if B<S else 'bigdata? security!'))