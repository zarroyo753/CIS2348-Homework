# Zachary Arroyo
# UHID 1810267

x1 = int(input())
y1 = int(input())
z1 = int(input())
x2 = int(input())
y2 = int(input())
z2 = int(input())
solved = False

for x in range(-10, 11):
    for y in range(-10, 11):
        if ((x1 * x + y1 * y) == z1) and ((x2 * x + y2 * y) == z2):
            print(x, y)
            solved = True

if not solved:
    print("No solution")