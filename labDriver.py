from menuItem import MenuItem
from restaurant import Restaurant


def main():
    """Main driver."""

    menu_items = [
        MenuItem("Hamburger", 13.00),
        MenuItem("Hotdog", 7.99),
        MenuItem("Milkshake", 12.99),
        MenuItem("Cookies", 10.50),
        MenuItem("Spaghetti", 14.99),
        MenuItem("Pretzel", 5.00),
        MenuItem("Quiche", 12.50),
        MenuItem("Omelette", 8.99),
        MenuItem("Boba Tea", 6.99),
        MenuItem("Fried Chicken", 13.99)
    ]

    main_restaurant = Restaurant(menu_items)

    print("Welcome to the Junk Food Central! Please see the menu below")

    while True:
        main_restaurant.display_menu()

        while True:
            choice = input(
                "Please enter the number of the item to add to your order. "
                "When you are finished, enter 0: "
            )

            try:
                choice = int(choice)
            except ValueError:
                print("Please enter a valid number.")
                continue

            if choice == 0:
                break

            if choice < 1 or choice > len(menu_items):
                print("Please enter a number from the menu.")
                continue

            main_restaurant.add_order(menu_items[choice - 1])

        print("Below is your entire order")
        main_restaurant.display_order()

        total_price = main_restaurant.calculate_total()
        print(f"Total Price is ${total_price:.2f}")

        new_order = input(
            "Do you want to start a new order? "
            "Enter 'yes' to make another order or anything else to quit: "
        )

        if new_order.lower() != "yes":
            print("Thank you!")
            break

        main_restaurant.clear_order()


if __name__ == "__main__":
    main()