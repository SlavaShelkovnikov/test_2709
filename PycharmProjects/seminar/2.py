string = input()
counter = 0
currentLetter = string[0]
maxSubstring = ''
max2Substring = ''
for i in range(len(string)):
    if string[i] == currentLetter:
        counter += 1
    elif len(maxSubstring) < counter:
        max2Substring = maxSubstring
        maxSubstring = currentLetter * counter
        counter = 1
        currentLetter = string[i]
    elif len(max2Substring) < counter <= len(maxSubstring):
        max2Substring = counter * currentLetter
        counter = 1
        currentLetter = string[i]
if len(maxSubstring) < counter:
    max2Substring = maxSubstring
    maxSubstring = currentLetter * counter
    counter = 1
    currentLetter = string[i]
elif len(max2Substring) < counter < len(maxSubstring):
    max2Substring = counter * currentLetter
    counter = 1
    currentLetter = string[i]
print(max2Substring)
