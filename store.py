from products import Product

class Store:

    def __init__(self, product_list):
        self.products = product_list

    def add_product(self, product):
        for item in product:
            self.products.append(item)
        return self.products

    def remove_product(self, product):
        self.products.pop(product)
        return self.products

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.products:
            total_quantity += Product.get_quantity(product)
        return total_quantity

    def get_all_products(self):
        # active_products = [product for product in self.products if product.is_active()]
        # return active_products
        active_products = {}
        product_number = 1
        for product in self.products:
            if product.is_active():
                description = product.show()
                active_products[product_number] = description
                product_number += 1
        return active_products

    def order(self, shopping_list):
        price = 0
        for i in range(len(shopping_list)):
            product_to_buy, quantity = shopping_list[i][0], shopping_list[i][1]
            sub_price = Product.buy(product_to_buy, quantity)
            price += sub_price
        print(f"Order placed. Total cost: {price} dollars.")