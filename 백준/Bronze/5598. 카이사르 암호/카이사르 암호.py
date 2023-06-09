word = [ord(c)-3 for c in input()]
print(''.join([chr(c+26) if c<65 else chr(c) for c in word]))