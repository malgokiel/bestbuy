from products import Product

class Store:
    products = []
    def add_product(self, product):
        for item in product:
            self.products.append(item)
        return self.products

    def remove_product(self, product):
        self.products.pop(product)

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.products:
            total_quantity += Product.get_quantity(product)
        return total_quantity

    def get_all_products(self):
        active_products = [product for product in self.products if product.is_active()]
        return active_products

    def order(self, shopping_list):
        for i in range(len(shopping_list)):
            product_to_buy, quantity = shopping_list[i][0], shopping_list[i][1]
            price = Product.buy(product_to_buy, quantity)
            print(f"Order cost: {price} dollars.")