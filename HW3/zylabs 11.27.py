# Zachary Arroyo
# UHID 1810267

roster = {}

for x in range(5):
    jersey = int(input(f"Enter player {x+1}'s jersey number:\n"))
    rating = int(input(f"Enter player {x+1}'s rating:\n"))
    print()
    roster[jersey] = rating

print("ROSTER")
for number, rating in sorted(roster.items()):
    print(f"Jersey number: {number}, Rating: {rating}")

print('\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit')
choice = input("\nChoose an option:\n")
while choice != 'q':
    if choice == 'a':
        jersey = int(input(f"Enter a new player's jersey number:\n"))
        rating = int(input(f"Enter the player's rating:\n"))
        print()
        roster[jersey] = rating
        print(
            '\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit')
        choice = input("\nChoose an option:\n")
    elif choice == 'd':
        delete = int(input('Enter a jersey number:\n'))
        roster.pop(delete)
        print(
            '\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit')
        choice = input("\nChoose an option:\n")
    elif choice == 'u':
        update = int(input('Enter a jersey number:\n'))
        roster[update] = int(input('Enter a new rating for player:\n'))
        print(
            '\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit')
        choice = input("\nChoose an option:\n")
    elif choice == 'r':
        rate = int(input('Enter a rating:\n'))
        print(f"\nABOVE {rate}")
        for number, rating in sorted(roster.items()):
            if rating > rate:
                print(f"Jersey number: {number}, Rating: {rating}")
        print(
            '\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit')
        choice = input("\nChoose an option:\n")
    elif choice == 'o':
        print("ROSTER")
        for number, rating in sorted(roster.items()):
            print(f"Jersey number: {number}, Rating: {rating}")
        print(
            '\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit')
        choice = input("\nChoose an option:\n")
    else:
        choice = input('\nChoose an option:\n')