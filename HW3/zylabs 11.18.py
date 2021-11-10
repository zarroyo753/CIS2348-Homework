# Zachary Arroyo
# UHID 1810267

values = [int(x) for x in input().split(' ')]
values.sort()
for value in values:
    if value >= 0:
        print(value, end=' ')
