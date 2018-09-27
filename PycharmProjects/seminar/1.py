string = input()
counter = 0
currentLetter = string[0]
for i in range(len(string)):
    if string[i] == currentLetter:
        counter += 1
    else:
        print(currentLetter, counter, sep='', end='')
        counter = 1
        currentLetter = string[i]
print(currentLetter, counter, sep='')
