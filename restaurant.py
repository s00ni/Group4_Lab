class Restaurant: 
  def __init__(self):
    self.menu_items = []
    self.order_list = []

  def display_menu(self):
    for i in self.menu_items:
      print (i)
  
  def add_order(self, menuItem_object):
    self.order_list.append(menuItem_object)
    
  def calculate_total(self):
    total_price = 0 
    for item in self.order_list:
      total_price = total_price + item.price
    return total_price

  def display_order(self):
    for i in self.order_list:
      print (i)
    
  def clear_order(self):
    self.order_list.clear()

