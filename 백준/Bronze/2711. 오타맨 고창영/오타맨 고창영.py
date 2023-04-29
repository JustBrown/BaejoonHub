import sys 
input = sys.stdin.readline

for _ in range(int(input())):
    input_data = input().split()
    idx = int(input_data[0])-1
    print(input_data[1][:idx]+input_data[1][idx+1:])