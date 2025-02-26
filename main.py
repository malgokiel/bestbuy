import sys
from termcolor import colored
import store
import products
import promotions
from messages import invalid_input, order_error, decorator
from products import NonStockedProduct

VALID_MENU_OPTIONS = [1, 2, 3, 4]
STORE_COLOR_THEME = 'magenta'
ERROR_COLOR_THEME = 'light_red'

def start(best_buy):
    """
    Handles main dynamics of the shop.
    Displays menu to the user and handles user's choice.
    """
    while True:
        print(colored("""
    STORE MENU:
    1. List all products in store
    2. Show total amount in store
    3. Make an order
    4. Quit\n""", color=STORE_COLOR_THEME, attrs=['bold']))

        user_choice = get_user_input()

        if user_choice == 1:
            all_products = best_buy.get_all_products()
            print_all_products(all_products)

        elif user_choice == 2:
            total = best_buy.get_total_quantity()
            print(f"\nTotal amount of items in store: {int(total)}")

        elif user_choice == 3:
            all_products = best_buy.get_all_products()
            shopping_list = get_shopping_list(best_buy, all_products)
            print(f"\n{decorator}")
            print(colored("*** SUMMARY ***", color=STORE_COLOR_THEME, attrs=['bold']))
            best_buy.order(shopping_list)
            print(decorator)

        elif user_choice == 4:
            print(colored("Thank you for shopping with us!", color=STORE_COLOR_THEME, attrs=['bold']))
            sys.exit()


def get_user_input():
    """
    Gets, validates and returns user input.
    """
    while True:
        try:
            user_choice = int(input("Please choose a number: "))
            if user_choice not in VALID_MENU_OPTIONS:
                print(invalid_input)
            else:
                return user_choice
        except ValueError:
            print(invalid_input)


def print_all_products(all_products):
    """
    Displays a list of products available in the store.
    """
    print(colored("\nOUR PRODUCTS:", color=STORE_COLOR_THEME, attrs=['bold']))
    if not all_products:
        print("We are sold out.")
    else:
        for i, item in enumerate(all_products.values(), 1):
            print(f"{i}. {item}")


def get_shopping_list(best_buy, all_products):
    """
    Asks user to insert the number and the amount of the product they want to purchase.
    returns a list of tuples of the product and the quantity.
    """
    shopping_list = []
    print(colored("\nOUR OFFER: ", color=STORE_COLOR_THEME, attrs=['bold']))
    for number, item in all_products.items():
        print(f"{number + 1}. {item}")

    print(colored("\n__place your order__",
                  color=STORE_COLOR_THEME, attrs=['bold']))

    bought_in_session = {}
    while True:
        which_product = input("\nEnter a # of the product you want to purchase: ")
        quantity = input("How many units do you want to buy?: ")

        try:
            which_product = int(which_product)
            quantity = int(quantity)
            product_to_shop = best_buy.products[which_product - 1]

            if products.Product.is_active(product_to_shop) and not isinstance(product_to_shop, NonStockedProduct) and quantity > 0:

                current_availability = products.Product.get_quantity(product_to_shop)
                availability_in_session = current_availability - quantity - bought_in_session.get(which_product-1, 0)
                if availability_in_session >= 0:
                    if isinstance(product_to_shop, products.LimitedProduct) and quantity > 1:
                        print("Shipping can only be purchased once per order, we adjusted it for you.")
                        quantity = 1

                    shopping_list.append((product_to_shop, quantity))

                    if which_product-1 in bought_in_session.keys():
                        bought_in_session[which_product - 1] += quantity
                    else:
                        bought_in_session[which_product-1] = quantity
                else:
                    print(colored(
                        f"Not enough units in stock. Still available: "
                        f"{int(current_availability) - bought_in_session.get(which_product-1, 0)}"
                        , color=ERROR_COLOR_THEME))
            elif isinstance(product_to_shop, NonStockedProduct):
                shopping_list.append((product_to_shop, quantity))
            else:
                print(order_error)
                print(colored("Incorrect product ID or negative quantity.", color=ERROR_COLOR_THEME))
        except IndexError:
            print(order_error)
            print(colored("Invalid product number.", color=ERROR_COLOR_THEME))
        except ValueError:
            print(order_error)
            print(colored("You missed a field or did not enter a number.", color=ERROR_COLOR_THEME))

        checkout = input(colored("Checkout? [y, n]: ", color=STORE_COLOR_THEME, attrs=['bold']))
        while checkout.lower() not in ["y", "n"]:
            checkout = input(colored("Checkout? [y, n]: ", color=STORE_COLOR_THEME, attrs=['bold']))
        if checkout.lower() == "n":
            continue
        else:
            break

    return shopping_list


def main():
    """
    Initializes Store object and runs store simulation
    """
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)

    # starts the shop simulator
    start(best_buy)

if __name__ == "__main__":
    main()
