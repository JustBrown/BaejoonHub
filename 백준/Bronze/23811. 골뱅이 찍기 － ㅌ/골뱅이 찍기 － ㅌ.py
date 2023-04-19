n = int(input())
for i in range(5):
    for _ in range(n):
        print('@'*n*5 if i==0 or i==2 or i==4 else '@'*n)