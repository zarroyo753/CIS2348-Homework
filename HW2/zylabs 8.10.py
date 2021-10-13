# Zachary Arroyo
# UHID 1810267

word1 = input()
word2 = word1.replace(" ", "")
listword = [char for char in word2]
reverseword = []
reverseword.extend(listword)
reverseword.reverse()

if listword == reverseword:
    print(f"{word1} is a palindrome")
else:
    print(f"{word1} is not a palindrome")