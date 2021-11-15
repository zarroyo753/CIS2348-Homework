# Zachary Arroyo
# UHID 1810267

# This file serves as the file to run to utilize most of the program's functions.

import csv
from datetime import datetime
from FinalProjectInput import items     # imports datetime methods for service date review and the items dictionary from last file

class WriteList:
    def __init__(self,dict):
        self.dict = dict     # makes dictionary within WriteList object equal to the dictionary given in the parameter.

    def writefull(self):
        sortdict = dict(sorted(self.dict.items(), key=lambda x: (x[1]['manufacturer'])))     # used in each WriteList method to sort dictionary based on required sorting
        fullinven = csv.writer(open('FullInventory.csv', 'w+', newline=''))
        for ID in sortdict:
            towrite = (f"{ID},{sortdict[ID].get('manufacturer')},{sortdict[ID].get('type')},{sortdict[ID].get('price')},{sortdict[ID].get('service date')},{sortdict[ID].get('damaged')}").split(',')      # f-string used to easily add each required value to the string
            fullinven.writerow(towrite)

    def writetype(self):
        types = []                   # separate list used to store each unique item type
        sortdict = dict(sorted(self.dict.items(), key=lambda x: [x]))
        for ID in sortdict:
            if sortdict[ID].get('type').capitalize() not in types:      # item types are capitalized in list to ensure proper file name capitalization
                types.append((sortdict[ID].get('type').capitalize()))
        for type in types:
            filename = (f"{type}Inventory.csv")
            typelist = csv.writer(open(filename, 'w+', newline=''))

            for ID in sortdict:
                if sortdict[ID].get('type').capitalize() == type:
                    towrite = (f"{ID},{sortdict[ID].get('manufacturer')},{sortdict[ID].get('price')},{sortdict[ID].get('service date')},{sortdict[ID].get('damaged')}").split(',')
                    typelist.writerow(towrite)

    def writepastservice(self):
        pastservice = csv.writer(open('PastServiceDateInventory.csv', 'w+', newline=''))
        sortdict = dict(sorted(self.dict.items(), key=lambda x: datetime.strptime(x[1]['service date'],'%m/%d/%Y')))  # converts the time for each service date to a time readable by datetime, then sorts by the numerical value
        for ID in sortdict:
            servdate = sortdict[ID].get('service date')
            if datetime.today() > datetime.strptime(servdate,'%m/%d/%Y'):
                towrite = (f"{ID},{sortdict[ID].get('manufacturer')},{sortdict[ID].get('type')},{sortdict[ID].get('price')},{sortdict[ID].get('service date')},{sortdict[ID].get('damaged')}").split(',')
                pastservice.writerow(towrite)

    def writedamaged(self):
        damaged = csv.writer(open('DamagedInventory.csv', 'w+', newline=''))
        sortdict = dict(sorted(self.dict.items(), key=lambda x: int(x[1]['price'])))       # sorts by price before checking for damaged parts
        for ID in sortdict:
            if sortdict[ID].get('damaged') == 'damaged':
                towrite = (f"{ID},{sortdict[ID].get('manufacturer')},{sortdict[ID].get('type')},{sortdict[ID].get('price')},{sortdict[ID].get('service date')}").split(',')
                damaged.writerow(towrite)


# creates WriteList object. uses the items list from FinalProjectInput.py for the dictionary in initialization.

instance = WriteList(items)
instance.writefull()
instance.writetype()
instance.writepastservice()
instance.writedamaged()


# beginning of the query for part 2
query = input("What manufacturer and item are you looking for? Alternatively, type q to quit.\n")

while query != 'q':         # runs program continuously until input is q.
    querylist = query.split()       # splits query into list with individual words
    itemfound = False     # boolean used when an exact match is found
    itemids = []          # list used to store each matching item ID.
    for item in items:
        manufound = False   # two separate booleans for the manufacturer and type
        typefound = False
        for word in querylist:
            if word.lower() == items[item]['manufacturer'].lstrip().rstrip().lower():   # checks each word provided to see if that word matches the manufacturer or type. lstrip, rstrip
                manufound = True                                                        # lstrip, rstrip, and lower are used to ensure there is no error due to a leading/trailing space or a difference in capitalization.
            if word.lower() == items[item]['type'].lstrip().rstrip().lower():
                typefound = True
        if manufound and typefound:     # if both booleans are true, then the item was found and this block runs
            itemfound = True
            itemids.append(item)

    if not itemfound:       # if itemfound is never turned true, the else block will never run.
        print("No such item in inventory")
    else:
        altid = 0       # initializes variable to store alternate product ID.
        highestid = itemids[0]  # used to store the most expensive product's id. starts with the first id.

        for id in itemids:
            # checks if a product is either damaged or past service date using datetime. if either are true, it is removed from the list of itemids.
            if items[id]['damaged'] == 'damaged' or datetime.strptime(items[id]['service date'], '%m/%d/%Y') < datetime.today():
                itemids.remove(id)

        for id in itemids:   # second for loop used for the itemids that remain after removing all damaged/past service items.
            if int(items[id]['price']) > int(items[highestid]['price']):  # checks the price between the current ID's price and the highest id's price. if it is greater, it replaces the highest ID.
                highestid = id

        lowprice = int(items[highestid]['price']) - (float(items[highestid]['price']) / 10)           # finds lowest and highest price within a 10% range
        highprice = int(items[highestid]['price']) + (float(items[highestid]['price']) / 10)

        for id in items:        # searches each item for a potential alternate candidate. split into three different if statements to make it look better.
            if lowprice <= int(items[id]['price']) <= highprice:   # checks if item in question is within price range
                if id != highestid and items[highestid]['manufacturer'] != items[id]['manufacturer']:      # checks that item is not from the same manufacturer
                    if items[id]['type'] == items[highestid]['type']:           # checks that item is the same item type
                        altid = id

        if len(itemids) == 0:   # checks if itemids is empty. if so, which happens after all items are removed due to being damages or out of service, then it informs the user.
            print("\nNo such working item in inventory")
        else:
            print(f"\nYour item is: ID: {highestid}, Manufacturer: {items[highestid]['manufacturer']}, Item type: {items[highestid]['type']}, Price: ${items[highestid]['price']}.")

        if altid == 0:     # if no alternative product is found, altid stays at 0. therefore, no similar item will be found.
            print('No similar items found')
        else:              # if an alternate product is found, outputs the information
            print(f"You may also consider: ID: {altid}, Manufacturer: {items[altid]['manufacturer']}, Item type: {items[altid]['type']}, Price: ${items[altid]['price']}.")

    query = input("\nWhat other manufacturer and item are you looking for? Alternatively, type q to quit.\n")       # ends program if input is q.