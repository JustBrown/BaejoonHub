d, m = map(int, input().split())
D = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = {0:'Wednesday' , 1:'Thursday' , 2:'Friday' , 3:'Saturday', 4:'Sunday', 5:'Monday', 6:'Tuesday' } 
print(week[(d+sum(D[:m]))%7])