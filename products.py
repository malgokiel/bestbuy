
class Product:
     def __init__(self, name, price, quantity):

         try:
             self.name = name
             self.price = price
             self.quantity = quantity
             self.active = True
         except ValueError:
             print("One or more values is incorrect")

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
         return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

     def buy(self, quantity):
         #self.quantity = self.set_quantity(self, quantity)
         self.quantity = self.get_quantity() - quantity
         self.set_quantity(self.quantity)
         purchase_price = self.price * quantity
         return purchase_price



def main():
    # TESTING:

    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    print(bose.show())
    print(mac.show())

    bose.set_quantity(1000)
    print(bose.show())


if __name__ == "__main__":
    main()