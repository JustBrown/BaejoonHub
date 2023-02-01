def solution(s):
    answer = list(map(int, s.split()))
    return " ".join(map(str, [min(answer), max(answer)]))
