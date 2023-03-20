import sys
input = sys.stdin.readline

gandalph = [1, 2, 3, 3, 4, 10]
thauron = [1, 2, 2, 2, 3, 5, 10]

for i in range(int(input())):
    g_score = 0
    for g, n in zip(gandalph, map(int, input().split())):
        g_score += g*n
    t_score = 0
    for t, n in zip(thauron, map(int, input().split())):
        t_score += t*n

    print(f'Battle {i+1}:', 'Good triumphs over Evil' if g_score > t_score 
          else ('Evil eradicates all trace of Good' if g_score < t_score else 'No victor on this battle field'))