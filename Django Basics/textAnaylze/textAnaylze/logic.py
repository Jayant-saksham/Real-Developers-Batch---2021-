txt = input("Enter text : ")
countWords = 0
countNum = 0
countSmall = 0
countCaps = 0
countSymbols = 0
countSpaces = 0
countWords = len(txt.split())
symbols = list("!@#$%^&*()_+][-~`'")

for letter in txt:
    if letter == " ":
        countSpaces = countSpaces + 1
    elif letter.isupper():
        countCaps = countCaps + 1
    elif letter.islower():
        countSmall = countSmall + 1
    elif letter in symbols:
        countSymbols = countSymbols + 1
    elif letter.isnumeric():
        countNum = countNum + 1


