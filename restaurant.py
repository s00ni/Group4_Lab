class Restaurant: 

  """Takes a list as an attribute."""
  def __init__(self, menu_items:list):
    self.menu_items = menu_items
    self.order_list = []

  """Prints a menu with visible indexes starting at 1."""
  def display_menu(self):
    for index, i in enumerate(self.menu_items, start=1):
      print (f"{index}. {i}")
  
  """Returns None but adds value to order list attribute."""
  def add_order(self, menuItem_object):
    self.order_list.append(menuItem_object)
    
  """Returns total price of order."""
  def calculate_total(self):
    total_price = 0 
    for item in self.order_list:
      total_price = total_price + item.price
    return total_price

  """Prints entire order."""
  def display_order(self):
    for i in self.order_list:
      print (i)

  """Clears order list"""  
  def clear_order(self):
    self.order_list.clear()
