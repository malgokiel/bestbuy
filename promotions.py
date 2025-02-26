from abc import ABC, abstractmethod

@abstractmethod
class Promotion(ABC):

    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotion):

    def apply_promotion(self, product, quantity):
        no_of_discounted_items = quantity // 2

        full_price_items = quantity - no_of_discounted_items
        full_price = full_price_items * product.price
        discounted = (no_of_discounted_items * product.price) / 2

        discounted_price = full_price + discounted

        return discounted_price


class ThirdOneFree(Promotion):

    def apply_promotion(self, product, quantity):
        no_of_discounted_items = quantity // 3
        pay_for = quantity - no_of_discounted_items

        discounted_price = pay_for * product.price
        return discounted_price


class PercentDiscount(Promotion):

    discount = 0.8

    def apply_promotion(self, product, quantity):
        discounted_price = (product.price * quantity) * discount

        return discounted_price