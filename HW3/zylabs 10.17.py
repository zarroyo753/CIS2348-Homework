# Zachary Arroyo
# UHID 1810267

# Type code for classes here
class ItemToPurchase:
    def __init__(self, name = 'none', price = 0 , quantity = 0):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity*self.item_price}")
if __name__ == "__main__":
    print('Item 1')
    name1 = input('Enter the item name:\n')
    price1 = int(input('Enter the item price:\n'))
    quantity1 = int(input('Enter the item quantity:\n'))

    print('\nItem 2')
    name2 = input('Enter the item name:\n')
    price2 = int(input('Enter the item price:\n'))
    quantity2 = int(input('Enter the item quantity:\n'))

    item1 = ItemToPurchase(name1,price1,quantity1)
    item2 = ItemToPurchase(name2,price2,quantity2)
    print('\nTOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()
    print(f"\nTotal: ${item1.item_price * item1.item_quantity + item2.item_price * item2.item_quantity}")