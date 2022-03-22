message = input("Enter message: ")
key = input("Enter Key: ")

if len(message) != len(key):
    print("message length and key length should be same")
else:
    cipherText = ""

    for i in range(len(message)):
        cipherText = cipherText + chr((((int(ord(message[i])) - 97) + (int(ord(key[i])) - 97)) % 26) + 97)

    print("Cipher Text is: " + cipherText)

    decodedText = ""

    for i in range(len(cipherText)):
        decodedText = decodedText + chr((((int(ord(cipherText[i])) - 97) - (int(ord(key[i])) - 97)) % 26) + 97)

    print("Decoded Text is: " + decodedText)