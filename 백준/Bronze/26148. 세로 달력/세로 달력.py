n = int(input())
start = int(input())
isleap = (n%4==0 and n%100!=0) or n%400==0
dict_day = {1:31, 2: 29 if isleap else 28, 3:31, 4:30, 
            5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

result = 0
for m in range(1, 13):
    for i in range(1, 8):
        if i+28 <= dict_day[m]:
            result += 1

print(result)