import locale

class Product:
     def __init__(self, name, price, quantity):
        is_name = isinstance(name, str)
        is_price = isinstance(price, (int, float))
        is_quantity = isinstance(quantity, int)
        try:
            if not is_name or not is_price or not is_quantity or len(name) <= 1:
                self.active = False
                self.name = None
                self.quantity = 0
                self.price = 0
                raise ValueError(f"Invalid parameter(s). {name} not added to the store")

            self.name = name
            self.price = price
            self.quantity = quantity
            self.active = True
        except ValueError as parameter_error:
            print(parameter_error)

     def get_quantity(self):
         return float(self.quantity)


     def set_quantity(self, quantity):
         self.quantity = quantity
         if self.quantity == 0:
             self.active = False
             return self.active


     def is_active(self):
         return self.active


     def show(self):
         return f"{self.name}, Price: {locale.currency(self.price, grouping=True)}, Quantity: {int(self.quantity)}"


     def buy(self, quantity):
         if quantity > self.get_quantity():
             print(f"Not enough units in store:\n{self.name} X {quantity} units was removed from the bill.\n")
             return 0
         else:
             self.quantity = self.get_quantity() - quantity
             self.set_quantity(self.quantity)
             purchase_price = self.price * quantity
             return purchase_price