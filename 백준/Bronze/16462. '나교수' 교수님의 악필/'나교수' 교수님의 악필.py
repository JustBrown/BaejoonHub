import sys
input = sys.stdin.readline

scores = []
for _ in range(int(input())):
    score = int(input()[:-1].replace('0', '9').replace('6', '9'))
    scores.append(100 if score>=100 else score)
result = sum(scores)/len(scores)

print(round(result) if result-int(result)!=0.5 else int(result)+1)