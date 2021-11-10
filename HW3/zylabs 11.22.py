# Zachary Arroyo
# UHID 1810267

words = input().split(' ')
wordamt = {}
for word in words:
    if word not in wordamt.keys():
        wordamt[word] = 1
    else:
        wordamt[word] += 1

for word in words:
    print(f'{word} {wordamt[word]}')