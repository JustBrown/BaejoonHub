import sys
input = sys.stdin.readline

for _ in range(int(input())):
    missions = []
    for _ in range(int(input())):
        missions.append(list(map(int, input().split())))
    k, d, a = map(int, input().split())
    
    result = 0
    for k_m, d_m, a_m in missions:
        result += max(0, k*k_m-d*d_m+a*a_m)
    
    print(result)