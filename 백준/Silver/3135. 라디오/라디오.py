A, B = map(int, input().split())
N, N_Hz = int(input()), [A]
for i in range(N):
    N_Hz.append(int(input()))

subB = [abs(B-i) for i in N_Hz]
closest_idx = subB.index(min(subB))
print(subB[closest_idx] if closest_idx == 0 else subB[closest_idx]+1)