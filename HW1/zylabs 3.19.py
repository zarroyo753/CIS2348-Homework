# Zachary Arroyo
# UHID 1810267

# Homework 1 - Zylabs 3.19
import math

height = int(input("Enter wall height (feet):\n"))
width = int(input("Enter wall width (feet):\n"))
area = height * width
print(f"Wall area: {area} square feet")

gallons = area / 350
print(f"Paint needed: {'{:.2f}'.format(gallons)} gallons")

cans = math.ceil(gallons)
print(f"Cans needed: {cans} can(s)")

color = input("\nChoose a color to paint the wall:\n")
prices = {'red': 35, 'blue': 25, 'green': 23}
cost = prices[color] * cans

print(f"Cost of purchasing {color} paint: ${cost}")

# print('{:.2f}'.format(your_value))