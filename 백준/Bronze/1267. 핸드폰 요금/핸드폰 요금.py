n = int(input())
times = list(map(int, input().split()))
Y = sum([10*(int(t/30)+1) for t in times])
M = sum([15*(int(t/60)+1) for t in times])
print('Y', Y) if Y<M else (print('Y', 'M', Y) if Y==M else print('M', M))
