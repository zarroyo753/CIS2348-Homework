# Zachary Arroyo
# UHID 1810267

import csv


class ReadList:
    def __init__(self, file):         # initialization, calls read method a single time upon creation.
        self.dict = {}
        self.read(file)

    def read(self, file):
        reader = csv.reader(open(file, 'r'), delimiter=',')  # reads selected file based on parameter
        if file == 'ManufacturerList.csv':
            for line in reader:
                self.dict[line[0]] = {'manufacturer': line[1], 'type': line[2], 'damaged': line[3]}    # adds manufacturer, type, and damaged to nested dictionary based on ID
        elif file == 'PriceList.csv':                                                                  # if item is damaged, then the 'damaged' key is filled in with 'damaged'. if the item is not damaged, the 'damaged' key is left empty.
            for line in reader:
                self.dict[line[0]]['price'] = line[1]
        elif file == 'ServiceDatesList.csv':
            for line in reader:
                self.dict[line[0]]['service date'] = line[1]


# creates ReadList object, then calls read method for each input file

instance = ReadList('ManufacturerList.csv')
instance.read('PriceList.csv')
instance.read('ServiceDatesList.csv')


# copies dictionary from ReadList object to an external dictionary. this will be used later in FinalProjectOutput.py
items = instance.dict
