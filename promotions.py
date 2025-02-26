from abc import ABC, abstractmethod

@abstractmethod
class Promotion(ABC):
    """
    Creates an abstract Promotion object.
    Is a parent class for different types of promotions.
    """

    def __init__(self, type):
        self.type = type

    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotion):

    def apply_promotion(self, product, quantity):
        """
        Applies promotions by deducting half a price of every second item.
        """
        no_of_discounted_items = quantity // 2

        full_price_items = quantity - no_of_discounted_items
        full_price = full_price_items * product.price
        discounted = (no_of_discounted_items * product.price) / 2

        discounted_price = full_price + discounted

        return discounted_price


class ThirdOneFree(Promotion):

    def apply_promotion(self, product, quantity):
        """
        Applies promotions by deducting full price of every third item.
        """
        no_of_discounted_items = quantity // 3
        pay_for = quantity - no_of_discounted_items

        discounted_price = pay_for * product.price
        return discounted_price


class PercentDiscount(Promotion):

    def __init__(self, type, percent):
        super().__init__(type)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        """
        Applies promotions by deducting percentage of price of every item.
        """
        discount = (100 - self.percent) / 100
        discounted_price = (product.price * quantity) * discount

        return discounted_price