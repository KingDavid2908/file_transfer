menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}

def calculate_subtotal(order):
    """ Calculates the subtotal of an order

    Function: 
        Adds up the prices of all the items in the order and returns the sum
    
    Args:
        order: list of dicts that contain an item name and price

    Returns:
        float = The sum of the prices of the items in the order
    """
    print('Calculating bill subtotal...')
    sum = 0
    for item in order:
        sum += item["price"]
    return round(sum, 2)


def calculate_tax(subtotal):
    """ Calculates the tax of an order

    Function:
        Multiplies the subtotal by 15% and returns the product rounded to two decimals.

    Args:
        subtotal: the price to get the tax of

    Returns:
        float - The tax required of a given subtotal, which is 15% rounded to two decimals.
    """
    print('Calculating tax from subtotal...')
    tax = round((((subtotal)*15)/100), 2)
    return tax


def summarize_order(order):
    """ Summarizes the order

    Function:
        1. Calculate the total (subtotal + tax) and store it in a variable named total (rounded to two decimals)
        2. Store only the names of all the items in the order in a list called names
        3. Return names and total.

    Args:
        order: list of dicts that contain an item name and price

    Returns:
        tuple of names and total. The return statement should look like 
        
        return names, total

    """
    print_order(order)

    subtotal = calculate_subtotal(order)
    tax = calculate_tax(subtotal)

    total = round(subtotal + tax, 2)
    names = []
    for item in order:
        names.append(item["name"])
    return names, total



def print_order(order):
    """
    Function:
        Prints the items in an order

    Args:
        Takes in an order

    Returns:
        Returns the order
    """
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order


def display_menu():
    """
    Function:
        It displays the menu in a nice format.
    
    Args:
        It takes no argument

    Returns:
        It returns no value
    """
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

def take_order():
    """
    Function:
        1. It calls the display menu function and asks user for their order selection.
        2. The user is allowed to make three selctions and appends the selection to an order
        3. It returns the selected order

    Args:
        It takes no argument

    Returns:
        It returns the order the user selected which is a list
    """
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order


def main():
    """A function that calls the individual functions"""
    order = take_order()
    # print_order(order)

    # subtotal = calculate_subtotal(order)
    # print("Subtotal for the order is: " + str(subtotal))

    # tax = calculate_tax(subtotal)
    # print("Tax for the order is: " + str(tax))

    # It assigns items and subtotal to the summary of the user order for easy calculations
    items, subtotal = summarize_order(order)
    print("Total bill generated is:", subtotal)

if __name__ == "__main__":
    main()