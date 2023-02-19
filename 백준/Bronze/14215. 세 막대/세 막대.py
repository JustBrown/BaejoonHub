side = sorted(map(int, input().split()))
if side[2] >= side[0]+side[1]:
    side[2] = side[0]+side[1]-1
print(sum(side))