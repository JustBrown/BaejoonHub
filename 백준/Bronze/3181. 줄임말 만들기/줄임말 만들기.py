ignore_word = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
print(''.join(word[0].upper() for i, word in enumerate(input().split()) if word not in ignore_word or i==0))