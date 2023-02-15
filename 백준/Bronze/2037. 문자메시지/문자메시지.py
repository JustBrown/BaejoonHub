import sys
input = sys.stdin.readline

p, w = map(int, input().split())
msg = input()[:-1]
num_alpha = {
    ' ':(1,1),
    'A':(2,1), 'B':(2,2), 'C':(2,3),
    'D':(3,1), 'E':(3,2), 'F':(3,3),
    'G':(4,1), 'H':(4,2), 'I':(4,3), 
    'J':(5,1), 'K':(5,2), 'L':(5,3),
    'M':(6,1), 'N':(6,2), 'O':(6,3),
    'P':(7,1), 'Q':(7,2), 'R':(7,3), 'S':(7,4),
    'T':(8,1), 'U':(8,2), 'V':(8,3),
    'W':(9,1), 'X':(9,2), 'Y':(9,3), 'Z':(9,4)
}

result = 0
for i in range(len(msg)):
    if i==0:
        result += p*num_alpha[msg[i]][1]
        continue

    if msg[i]!=' ' and num_alpha[msg[i-1]][0]==num_alpha[msg[i]][0]:
        result += w+p*num_alpha[msg[i]][1]
    else:
        result += p*num_alpha[msg[i]][1]

print(result)