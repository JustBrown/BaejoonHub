from itertools import product

def get_max_num(length):
    return sorted(list(map(lambda x:int(''.join(x)), product(nums, repeat=length))), reverse=True)

n, k = map(int, input().split())
nums = sorted(input().split(), reverse=True)

result = -1
num_len = len(str(n))
isdone = False
while result == -1:
    numbers = get_max_num(num_len)
    for number in numbers:
        if number <= n:
            isdone = True
            print(number)
            break
    if isdone:
        break
    num_len -= 1