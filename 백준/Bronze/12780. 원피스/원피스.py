H = input()
N = input()
result, idx = 0, -1

while True:
    idx = H.find(N, idx+1)
    if idx==-1:
        break
    result +=1

print(result)