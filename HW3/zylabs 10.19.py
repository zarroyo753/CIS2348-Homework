# Zachary Arroyo
# UHID 1810267

# Type code for classes here
class ItemToPurchase:
    def __init__(self, itemname='none', price=0, quantity=0, description='none'):
        self.item_name = itemname
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    def __init__(self, name, date):
        self.customer_name = name
        self.current_date = date
        self.cart_items = []

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, itemname):
        loc = -1
        for item in self.cart_items:
            if item.item_name == itemname:
                loc = self.cart_items.index(item)
        if loc == -1:
            print('Item not found in cart. Nothing removed.')
        else:
            self.cart_items.pop(loc)

    def modify_item(self, ItemToPurchase):
        for item in self.cart_items:
            if item.item_name == ItemToPurchase.item_name:
                item.item_quantity = ItemToPurchase.item_quantity

    def get_num_items_in_cart(self):
        totalitems = 0
        for item in self.cart_items:
            totalitems += item.item_quantity
        return totalitems

    def get_cost_of_cart(self):
        total = 0
        for item in self.cart_items:
            total += item.item_price * item.item_quantity
        return total

    def print_total(self):
        print()
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY\n\n Total: $0')
        else:
            total = 0
            for item in self.cart_items:
                total += item.item_price * item.item_quantity
            print(total)

    def print_descriptions(self):
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


if __name__ == "__main__":

    def print_menu(cart):
        print("\nMENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items' "
              "descriptions\no - Output shopping cart\nq - Quit")
        choice = input('\nChoose an option:\n')
        while choice != 'q':
            if choice == 'a':
                print('ADD ITEM TO CART')
                itemname = input('Enter the item name:\n')
                desc = input('Enter the item description:\n')
                price = int(input('Enter the item price:\n'))
                quantity = int(input('Enter the item quantity:\n'))
                item = ItemToPurchase(itemname, price, quantity, desc)
                cart.add_item(item)
                print(
                    "\nMENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items' "
                    "descriptions\no - Output shopping cart\nq - Quit")
                choice = input('\nChoose an option:\n')
            elif choice == 'r':
                print('REMOVE ITEM FROM CART')
                itemname = input('Enter name of item to remove:\n')
                cart.remove_item(itemname)
                print(
                    "\nMENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items' "
                    "descriptions\no - Output shopping cart\nq - Quit")
                choice = input('\nChoose an option:\n')
            elif choice == 'c':
                print('CHANGE ITEM QUANTITY')
                itemname = input('Enter the item name:\n')
                loc = -1
                for item in cart.cart_items:
                    if item.item_name == itemname:
                        loc = cart.cart_items.index(item)
                if loc == -1:
                    newitem = cart.cart_items[loc]
                    newitem.item_quantity = int(input('Enter the new quantity:\n'))
                    print('Item not found in cart. Nothing modified.')
                else:
                    newitem = cart.cart_items[loc]
                    newitem.item_quantity = int(input('Enter the new quantity:\n'))
                    cart.modify_item(newitem)
                print(
                    "\nMENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items' "
                    "descriptions\no - Output shopping cart\nq - Quit")
                choice = input('\nChoose an option:\n')
            elif choice == 'i':
                print(f"OUTPUT ITEMS' DESCRIPTIONS\n{name}'s Shopping Cart - {date}\n\nItem Descriptions")
                cart.print_descriptions()
                print(
                    "\nMENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items' "
                    "descriptions\no - Output shopping cart\nq - Quit")
                choice = input('\nChoose an option:\n')
            elif choice == 'o':
                print(f"OUTPUT SHOPPING CART\n{name}'s Shopping Cart - {date}")
                print(f"Number of Items: {cart.get_num_items_in_cart()}\n")
                for item in cart.cart_items:
                    item.print_item_cost()
                if cart.get_num_items_in_cart() == 0:
                    print('SHOPPING CART IS EMPTY')
                print(f"\nTotal: ${cart.get_cost_of_cart()}")
                print(
                    "\nMENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items' "
                    "descriptions\no - Output shopping cart\nq - Quit")
                choice = input('\nChoose an option:\n')
            else:
                choice = input('Choose an option:\n')


    name = input("Enter customer's name:\n")
    date = input("Enter today's date:\n")
    print(f"\nCustomer name: {name}\nToday's date: {date}")
    cart = ShoppingCart(name, date)
    print_menu(cart)
