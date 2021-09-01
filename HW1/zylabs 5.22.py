# Zachary Arroyo
# UHID 1810267

# Homework 1 - Zylabs 5.22
print('Davy\'s auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n')
ser1 = input("Select first service:\n")
ser2 = input("Select second service:\n")

services = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-': 0}
total = services[ser1] + services[ser2]
print(f"\nDavy's auto shop invoice\n")
if ser1 == '-':
    print(f"Service 1: No service")
else:
    print(f"Service 1: {ser1}, ${services[ser1]}")
if ser2 == '-':
    print(f"Service 2: No service")
else:
    print(f"Service 2: {ser2}, ${services[ser2]}")
print(f"\nTotal: ${total}")

