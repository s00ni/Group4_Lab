from menuItem import MenuItem
from restaurant import Restaurant

"""Main driver."""
def main():

    """Create list of MenuItem objects to use as an argument."""
    menu_items = [MenuItem("Hamburger", 13.00),
                    MenuItem("Hotdog", 7.99),
                    MenuItem("Milkshake", 12.99),
                    MenuItem("Cookies", 10.50),
                    MenuItem("Spaghetti", 14.99),
                    MenuItem("Pretzel", 5.00),
                    MenuItem("Quiche", 12.50),
                    MenuItem("Omelette", 8.99),
                    MenuItem("Boba Tea", 6.99),
                    MenuItem("Fried Chicken", 13.99)]

    """Create new Restaurant object while passing menu_items list."""
    main_restaurant = Restaurant(menu_items)
    print("Welcome to the Junk Food Central! Please see the menu below")
    
    """Outer loop to display menu if user wishes to submit another order."""
    while True:
        main_restaurant.display_menu()
    
        """Inner loop builds order_list attribute with user input."""
        while True:
            choice = input("Please enter the number of the item to add it to your order. When you are finished, enter 0: ") 

            """Ends the order."""
            if choice == '0' or int(choice) <= 0 :
                break

            """User input validation."""
            try:
                choice = int(choice)
            except ValueError:
                print("Please enter a valid number")
                continue 
            try:
                main_restaurant.add_order(menu_items[choice-1])
            except IndexError:
                print("Please enter a valid number")
                continue         
        
        """Displays order information."""
        print("Below is your entire order")
        main_restaurant.display_order()

        """Display total cost of order."""
        total_price = main_restaurant.calculate_total()
        print(f"Total Price is ${total_price:.2f}")

        """Prompts user to start another order."""
        new_order = input("Do you want to start a new order? Enter 'yes' to make another order or anything else to quit: ")

        """Ends program and clears order_list if user does not wish to continue."""
        if new_order != 'yes':
            print("Thank you!")
            break
        main_restaurant.clear_order()

if __name__ == '__main__':
    main()
