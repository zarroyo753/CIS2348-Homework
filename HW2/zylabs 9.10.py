# Zachary Arroyo
# UHID 1810267

import csv

file = open(input(), 'r')
reader = csv.reader(file, delimiter=',')
words = []
wordamt = {}
for word in list(reader)[0]:
    if word not in wordamt.keys():
        wordamt[word] = 1
        words.append(word)
    else:
        wordamt[word] += 1

for word in words:
    print(f"{word} {wordamt[word]}")