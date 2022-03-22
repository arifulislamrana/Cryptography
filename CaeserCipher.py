plainText = input('Enter the text to encrypt: ')

shift = int(input('Enter shift amount :'))

cipherText = ""

for i in plainText:
    cipherText = cipherText + chr((((int(ord(i))-97) + shift) % 26) + 97)

print("Encrypted text is: " + cipherText)

decodedText = ""

for i in cipherText:
    decodedText = decodedText + chr((((int(ord(i)) - 97) - shift) % 26) + 97)

print("Decrypted text is: " + decodedText)


