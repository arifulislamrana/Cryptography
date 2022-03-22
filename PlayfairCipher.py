from collections import Counter

text = "ariifulislaamarif"
key = "letitbedone"
table = [i for i in Counter(key)]

for i in range(ord('a'), ord('z') + 1):
    if chr(i) not in table:
        if chr(i) == 'j':
            continue
        table.append(chr(i))

print(len(table), table)

matrix = [[], [], [], [], []]

i = 0
j = 0
while i < len(table):
    matrix[j].append(table[i])
    matrix[j].append(table[i+1])
    matrix[j].append(table[i+2])
    matrix[j].append(table[i+3])
    matrix[j].append(table[i+4])
    j += 1
    i += 5


def printKeyMatrix(matrix):
    for i in range(5):
        for j in matrix[i]:
            if j == 'i':
                print("i/j" + "   ", end="")
                continue
            print(j + "   ", end="")

        print()


printKeyMatrix(matrix)


def makePair(text):
    textPair = []
    counter = 0

    while counter < len(text):
        if (counter+1) >= len(text) or text[counter] == text[counter+1]:
            textPair.append(text[counter] + 'x')
            counter += 1
        else:
            textPair.append(text[counter] + text[counter+1])
            counter += 2

    return textPair


print(makePair(text))


def encode(pairtext, matrix):
    encodedText = ""

    for i, j in pairtext:
        if i == 'j':
            i = 'i'
        if j == 'j':
            j = 'i'

        x1, y1 = None, None
        x2, y2 = None, None

        for p in range(5):
            if i in matrix[p]:
                x1, y1 = p, matrix[p].index(i)
            if j in matrix[p]:
                x2, y2 = p, matrix[p].index(j)

        if x1 == x2:
            y1 = (y1 + 1) % 5
            y2 = (y2 + 1) % 5
            encodedText += matrix[x1][y1] + matrix[x2][y2]
        elif y1 == y2:
            x1 = (x1 + 1) % 5
            x2 = (x2 + 1) % 5
            encodedText += matrix[x1][y1] + matrix[x2][y2]
        else:
            encodedText += matrix[x1][y2] + matrix[x2][y1]
    return encodedText


print(encode(makePair(text), matrix))


def decode(pairtext, matrix):
    encodedText = ""

    for i, j in pairtext:
        if i == 'j':
            i = 'i'
        if j == 'j':
            j = 'i'

        x1, y1 = None, None
        x2, y2 = None, None

        for p in range(5):
            if i in matrix[p]:
                x1, y1 = p, matrix[p].index(i)
            if j in matrix[p]:
                x2, y2 = p, matrix[p].index(j)

        if x1 == x2:
            y1 = (y1 - 1) % 5
            y2 = (y2 - 1) % 5
            encodedText += matrix[x1][y1] + matrix[x2][y2]
        elif y1 == y2:
            x1 = (x1 - 1) % 5
            x2 = (x2 - 1) % 5
            encodedText += matrix[x1][y1] + matrix[x2][y2]
        else:
            encodedText += matrix[x1][y2] + matrix[x2][y1]
    return encodedText


o = encode(makePair(text), matrix)

print(decode(makePair(o), matrix))