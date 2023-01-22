#List of drinks and snacks with their corresponding codes and prices
items = {
    'A1': {'name': 'Pepsi', 'price': 1.50},
    'A2': {'name': 'Fanta', 'price': 1.50},
    'A3': {'name': '7UP', 'price': 1.50},
    'A4': {'name': 'Chips', 'price': 0.75},
    'A5': {'name': 'Cashews', 'price': 0.50},
    'A6': {'name': 'Water', 'price': 1.00}
}


#Function to display the menu of drinks and snacks
def menu_items():
    print('\n--- Welcome to the vending machine! ---')
    print('\n-- Here is a list of our drinks and snacks: --')
    for code, item in items.items():
        print(code + ': ' + item['name'] + ' (' + str(item['price']) + ')')

#Function to get user selection and money
def user_selection(money):
    selection = input("Please choose an item to purchase or press X to quit:")
    if selection == "X":
        print("Your total money is "+ str(money) +".")
        return
    if selection in items:
        # Get the price of the selected item
        price = items[selection]['price']
        # Check if the user has enough money
        if money >= price:
            print("Dispensing "+ items[selection]['name'])
            money-= price
            print("Your remaining balance is: "+ str(money))
            user_selection(money)
        else:
            print("Insuffucient funds. Please enter more money...")
            user_selection(money)
    else:
        print("Invalid selection.")
        user_selection(money)

menu_items()
money = float(input('Enter the amount of money: '))
user_selection(money)