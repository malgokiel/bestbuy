import locale

class Product:
    """
    Creates a Product object of parameters name, price and quantity.
    Has various methods to:
    extract product's quantity,
    set the quantity,
    show if a product is active,
    display info about a product and
    updates a product in case of purchase.
    """
    def __init__(self, name, price, quantity):
        """
        Constructor, checks if passed parameters
        are correct and creates a new product.
        """
        self.active = None
        try:
            if not self.are_args_valid(name, price, quantity):
                Product.deactivate(self)
                self.name = None
                self.quantity = 0
                self.price = 0
                raise ValueError(f"Invalid parameter(s). {name} not added to the store")
            else:
                self.name = name
                self.price = price
                self.quantity = quantity
                Product.activate(self)
        except ValueError as parameter_error:
            print(parameter_error)


    def are_args_valid(self, name, price, quantity):
        is_name = isinstance(name, str)
        is_price = isinstance(price, (int, float))
        is_quantity = isinstance(quantity, int)

        if not is_name or not is_price or not is_quantity or len(name) <= 1 or price <= 0 or quantity <= 0:
            args_valid = False
        else:
            args_valid = True

        return args_valid


    def get_quantity(self):
        """
        Gets product's quantity
        """
        return float(self.quantity)


    def set_quantity(self, quantity):
        """
        Sets new quantity and if new quantity drops to zero deactivates product
        """
        self.quantity = quantity
        if self.quantity == 0:
            Product.deactivate(self)


    def is_active(self):
        """
        Returns a bool True if product is active and False if not.
        """
        return self.active


    def activate(self):
        """
        Activates a product.
        """
        self.active = True


    def deactivate(self):
        """
        Deactivates a product
        """
        self.active = False


    def show(self):
        """
        Returns a string representation of a product showing its attributes.
        :return:
        """
        return (f"{self.name}, "
                f"Price: {locale.currency(self.price, grouping=True)}, "
                f"Quantity: {int(self.quantity)}")


    def buy(self, quantity):
        """
        Checks if there is enough units to purchase a product,
        if yes calls a function to update the quantity,
        Calculates and returns a price of a purchase.
        """
        if quantity > self.get_quantity() and not isinstance(self, NonStockedProduct):
            print(f"Not enough units in store:\n"
                f"{self.name} X {quantity} units was removed from the bill.\n")
            return 0
        else:
            self.quantity = self.get_quantity() - quantity
            self.set_quantity(self.quantity)
            purchase_price = self.price * quantity

            return purchase_price


class NonStockedProduct(Product):
    def __init__(self, name, price, quantity=0):
        super().__init__(name, price, quantity)


    def are_args_valid(self, name, price, quantity):
        args_valid = super().are_args_valid(name, price, quantity)
        if quantity == 0:
            args_valid = True

        return args_valid

    def show(self):
        """
        Returns a string representation of a product showing its attributes.
        """
        return (f"{self.name}, "
                f"Price: {locale.currency(self.price, grouping=True)}")

    def buy(self, quantity):
        purchase_price = self.price * quantity
        return purchase_price


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum=1):
        super().__init__(name, price, quantity)
        self.maximum = maximum


    def show(self):
        """
        Returns a string representation of a product showing its attributes.
        """
        return (f"{self.name}, "
                f"Price: {locale.currency(self.price, grouping=True)}, "
                f"Maximum: {self.maximum}")


    def buy(self, quantity):
        purchase_price = self.price * quantity
        return purchase_price