B = tuple(map(int, input().split()))
D = tuple(map(int, input().split()))
J = tuple(map(int, input().split()))

B_dist = max(abs(J[0]-B[0]), abs(J[1]-B[1]))
D_dist = abs(J[0]-D[0]) + abs(J[1]-D[1])

print('tie' if B_dist==D_dist else ('bessie' if B_dist<D_dist else 'daisy'))