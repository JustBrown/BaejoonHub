n = int(input())
p = int(input())
result = p

if n>=5: result = max(0, min(result, p - 500))
if n>=10: result = max(0, min(result, int(p*0.9)))
if n>=15: result = max(0, min(result, p-2000))
if n>=20: result = max(0, min(result, int(p*0.75)))

print(result)