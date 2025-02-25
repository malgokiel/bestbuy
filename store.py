import locale
from termcolor import colored
from products import Product

# Set the local currency to US dollars
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

COLOR_THEME = 'magenta'

class Store:
    """
    Creates a Store object but adding Product objects to the inventory.
    Has modules responsible for:
    adding a product into a store,
    removing a product,
    fetching information about current amount of products in the inventory.
    Allows to place an order.
    """
    def __init__(self, product_list):
        """
        Constructor. Initializes products based on a passed product list.
        """
        self.products = product_list


    def add_product(self, product):
        """
        Adds a product into a store, returns updated products list.
        """
        self.products.append(product)
        return self.products


    def remove_product(self, product):
        """
        Removes a product from a list and returns updated list.
        """
        updated_products = []
        for element in self.products:
            if element != product:
                updated_products.append(element)

        self.products = updated_products
        return self.products


    def get_total_quantity(self):
        """
        Fetches current total amount of products in store.
        """
        total_quantity = 0
        for product in self.products:
            total_quantity += Product.get_quantity(product)
        return total_quantity


    def get_all_products(self):
        """
        Returns a list of all currently active products in store.
        """
        active_products = {}
        product_number = 1
        for i, product in enumerate(self.products):
            if product.is_active():
                description = product.show()
                active_products[i] = description
                product_number += 1
        return active_products


    def order(self, shopping_list):
        """
        Handles user order.
        Loops through all the products specified in a shopping_list,
        keeps track of price.
        Prints order confirmation or cancellation.
        """
        price = 0
        bought_items = []
        for i, _ in enumerate(shopping_list):
            product_to_buy, quantity = shopping_list[i][0], shopping_list[i][1]
            sub_price = product_to_buy.buy(quantity)
            if sub_price > 0:
                bought_items.append([product_to_buy.name, quantity, sub_price])
            price += sub_price

        if price == 0:
            print("The shopping list is empty. Order cancelled.")
        else:
            print(f"Order placed. Total cost: {locale.currency(price, grouping=True)}")
            print(colored("details:", color=COLOR_THEME, attrs=['bold']))
            for bought_item in bought_items:
                print(f"{bought_item[0]} X {bought_item[1]} "
                      f"units -> {locale.currency(bought_item[2], grouping=True)}")
