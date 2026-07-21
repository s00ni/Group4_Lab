# Group4_Lab
Repository for CSC 157 Group 4 Lab 

## File layout 
Group4_lab
├── menuItem.py      # contains the MenuItem class
├── restaurant.py     # contains the Restaurant class
├── labDriver.py      # contains main program logic 
└── README.md

## Restaurant Ordering System
### Purpose of the Project
The purpose of this project is to create a simple restaurant ordering system. The program lets customers view the menu, choose food items, and see the total cost of their order. This project helps us practice the Python skills we learned in class, such as classes, loops, lists, and decision statements.

### Main Features
The program includes the following features:
• Display a restaurant menu.
• Let the customer choose food items.
• Allow the customer to order more than one item.
• Calculate the total price.
• Show an order summary.
• Let the customer place another order or quit the program.

### Classes Used in the Program
Menu Item: This class stores information about one menu item.
Attributes:
• name
• price
Methods:
• get_name()
• get_price()
• str()

Restaurant: This class manages the menu and customer orders.
Attributes:
• menu_items
• order_list
Methods:
• display_menu()
• add_order()
• calculate_total()
• display_order()
• clear_order()
