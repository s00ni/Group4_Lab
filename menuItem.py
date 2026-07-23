class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    def get_name(self) -> str:
        """Returns the name of the menu item."""
        return self.name
    def get_price(self) -> float:
        """Returns the price of the menu item."""
        return self.price
    def __str__(self) -> str:
        """Returns a string representation for displaying the item."""
        return f"{self.name} - ${self.price:.2f}"
