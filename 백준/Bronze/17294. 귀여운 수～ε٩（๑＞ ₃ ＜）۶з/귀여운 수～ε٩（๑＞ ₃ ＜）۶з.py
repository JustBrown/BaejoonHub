number = list(map(int, list(input())))
d = set([number[i]-number[i+1] for i in range(len(number)-1)])
print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!' if len(d)<=1 else '흥칫뿡!! <(￣ ﹌ ￣)>')