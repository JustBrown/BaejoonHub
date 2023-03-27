for _ in range(int(input())):
    binary = bin(int(input()))[2:][::-1]
    print(' '.join(str(i) for i in range(len(binary)) if binary[i]=='1'))