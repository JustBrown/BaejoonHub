n = int(input()) 
[[print('@'*n*5 if i==0 or i==4 else '@'*n) for _ in range(n)] for i in range(5)]