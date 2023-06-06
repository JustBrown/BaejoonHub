import sys
input = sys.stdin.readline

result = 0
for _ in range(int(input())):
    dices = list(map(int, input().split()))
    cnt_dice = [0 for i in range(7)]
    for d in dices:
        cnt_dice[d] += 1

    if 3 in cnt_dice:
        temp = 10000+1000*cnt_dice.index(3)
    elif 2 in cnt_dice:
        temp = 1000+100*cnt_dice.index(2)
    else:
        temp = max(dices)*100
    
    result = max(result, temp)

print(result)