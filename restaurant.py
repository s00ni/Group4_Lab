<<<<<<< HEAD
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

=======
class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    def get_name(self) -> str:
        return self.name
    def get_price(self) -> float:
        return self.price
    def __str__(self) -> str:
        return f"{self.name} - ${self.price:.2f}"
>>>>>>> origin/main
