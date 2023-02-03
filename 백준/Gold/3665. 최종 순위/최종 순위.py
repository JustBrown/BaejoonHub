import sys
from collections import deque
input = sys.stdin.readline


def topology_sort():
    result = []
    q = deque()
    visit = [True]+[False]*n

    for i in range(1,n+1):
        if not indegree[i]:
            q.append(i)
            visit[i] = True
            
    while q:
        node = q.popleft()
        result.append(node)
        for e in graph[node]:
            indegree[e]-=1
            if not indegree[e]:
                q.append(e)
                visit[e] = True
    
    if False in visit:
        return 'IMPOSSIBLE'
    return ' '.join(map(str, result))


test_case = int(input())
for _ in range(test_case):
    # input data & initialization
    n = int(input())
    ranking = [0]+list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(i+1, n+1):
            graph[ranking[i]].append(ranking[j])
    m = int(input())
    dict_rank = {ranking[i]:i for i in range(1, n+1)}
    for _ in range(m):
        a, b = map(int, input().split())
        high, low = (a, b) if dict_rank[a] < dict_rank[b] else (b, a) 
        graph[high].remove(low)
        graph[low].append(high)

    # indegree set
    indegree = [0]*(n+1)
    for i in range(1, n+1):
        for e in graph[i]:
            indegree[e]+=1

    # run topology sort
    result = topology_sort()

    # print result
    print(result)