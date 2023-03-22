n = int(input())
origin = f'{n} bottles' if n!=1 else f'{n} bottle'
for k in range(n, -1, -1):
    if k>0:
        beer_k = f'{k} bottles' if k > 1 else ('1 bottle' if k == 1 else 'no more bottles')
        beer_k_Minus1 = f'{k-1} bottles' if k-1 > 1 else ('1 bottle' if k-1 == 1 else 'no more bottles')
        lyrics = f'{beer_k} of beer on the wall, {beer_k} of beer. \nTake one down and pass it around, {beer_k_Minus1} of beer on the wall.\n'
    else:
        lyrics = f'No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, {origin} of beer on the wall.'
    print(lyrics)