answer_scores = [100, 100, 200, 200, 300, 300, 400, 400, 500]
scores = list(map(int, input().split()))
result = 'draw' if sum(scores)>=100 else 'none'
for a, s in zip(answer_scores, scores):
    if s > a:
        result = 'hacker'
        break
print(result)