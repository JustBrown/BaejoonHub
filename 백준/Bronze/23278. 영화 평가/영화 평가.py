n, l, h = map(int, input().split())
scores = sorted(map(int, input().split()))[l if l!=0 else 0:-h if h!=0 else None]
print(sum(scores)/len(scores))