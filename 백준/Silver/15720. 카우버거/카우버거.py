B, C, D = map(int, input().split())
B_price = sorted(list(map(int, input().split())), reverse=True)
C_price = sorted(list(map(int, input().split())), reverse=True)
D_price = sorted(list(map(int, input().split())), reverse=True)

sale_num = min(B, C, D)
result = sum(B_price[:sale_num] + C_price[:sale_num] + D_price[:sale_num]) * 0.9 \
         + sum(B_price[sale_num:] + C_price[sale_num:] + D_price[sale_num:])
print(sum(B_price + C_price + D_price))
print(int(result))