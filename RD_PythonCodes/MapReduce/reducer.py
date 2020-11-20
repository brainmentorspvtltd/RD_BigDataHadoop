import sys

currentWord = None
currentCount = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, count = line.split("\t", 1)
    count = int(count)
    if currentWord == word:
        currentCount += 1
    else:
        if currentWord:
            print("{}\t{}".format(currentWord, currentCount))
        currentCount = count
        currentWord = word
if currentWord == word:
    print("{}\t{}".format(currentWord, currentCount))

