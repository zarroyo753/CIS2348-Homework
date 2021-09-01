# Zachary Arroyo
# UHID 1810267

# Homework 1 - Zylabs 2.19
juice = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
agave = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make?\n"))
print(f"\nLemonade ingredients - yields {'{:.2f}'.format(servings)} servings\n{'{:.2f}'.format(juice)} cup(s) lemon juice\n{'{:.2f}'.format(water)} cup(s) water\n{'{:.2f}'.format(agave)} cup(s) agave nectar\n")

newservings = float(input("How many servings would you like to make?\n"))
ratio = newservings/servings
juice *= ratio
water *= ratio
agave *= ratio
print(f"\nLemonade ingredients - yields {'{:.2f}'.format(newservings)} servings\n{'{:.2f}'.format(juice)} cup(s) lemon juice\n{'{:.2f}'.format(water)} cup(s) water\n{'{:.2f}'.format(agave)} cup(s) agave nectar")
juice /= 16
water /= 16
agave /= 16
print(f"\nLemonade ingredients - yields {'{:.2f}'.format(newservings)} servings\n{'{:.2f}'.format(juice)} gallon(s) lemon juice\n{'{:.2f}'.format(water)} gallon(s) water\n{'{:.2f}'.format(agave)} gallon(s) agave nectar")
