# Zachary Arroyo
# UHID 1810267

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

