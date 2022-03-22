keys = [
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c'
    ,'v', 'b', 'n', 'm'
]

plainText = input('Enter message: ')

cipherText = ""

for i in plainText:
    cipherText = cipherText + keys[(int(ord(i)) - 97) % 26]

print("Encoded message is: " + cipherText)

decodedText = ""

for i in cipherText:
    decodedText = decodedText + chr(int(keys.index(i)) + 97)

print("Decoded Text is: " + decodedText)





















#print("key: ", end='')
#for i in keys:
#    print(i, end='')

#print()