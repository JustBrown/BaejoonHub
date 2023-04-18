import sys
input = sys.stdin.readline

numbers = set([str(i) for i in range(0, 10)])
while True:
    n = input()[:-1]
    if n == '':
        break
    set_num = set(list(n))
    cnt=1
    while set_num != numbers:
        cnt+=1
        set_num.update(set(list(str(int(n)*cnt))))
    
    print(cnt)