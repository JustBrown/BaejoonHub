import sys
input = sys.stdin.readline

result = 0
for _ in range(int(input())):
    input_data = input().split()
    h, m = map(int, input_data[0].split(':'))
    start = h*60 + m
    end = start + int(input_data[1])

    if start>=420 and end<1140:
        result += 10*(end-start)
    elif start<420 and 420<=end<1140:
        result += 5*(420-start)+10*(end-420)
    elif 420<=start<1140 and end>=1140:
        result +=10*(1140-start)+5*(end-1140)
    else:
        result += 5*(end-start)

print(result)