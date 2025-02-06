import sys
from termcolor import colored
import store
import products
from messages import invalid_input, order_error, decorator

VALID_MENU_OPTIONS = [1, 2, 3, 4]
COLOR_THEME = 'magenta'

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
    4. Quit\n""", color=COLOR_THEME, attrs=['bold']))

        user_choice = get_user_input()
        all_products = best_buy.get_all_products()

        if user_choice == 1:
            print_all_products(all_products)

        elif user_choice == 2:
            total = best_buy.get_total_quantity()
            print(f"\nTotal amount of items in store: {int(total)}")

        elif user_choice == 3:
            shopping_list = get_shopping_list(best_buy, all_products)
            print(f"\n{decorator}")
            print(colored("*** SUMMARY ***", color=COLOR_THEME, attrs=['bold']))
            best_buy.order(shopping_list)
            print(decorator)

        elif user_choice == 4:
            print(colored("Thank you for shopping with us!", color=COLOR_THEME, attrs=['bold']))
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
    item_number_to_display = 1
    print(colored("\nOUR PRODUCTS:", color=COLOR_THEME, attrs=['bold']))
    if not all_products:
        print("We are sold out.")
    else:
        for item in all_products.values():
            print(f"{item_number_to_display}. {item}")
            item_number_to_display += 1


def get_shopping_list(best_buy, all_products):
    """
    Asks user to insert the number and the amount of the product they want to purchase.
    returns a list of tuples of the product and the quantity.
    """
    shopping_list = []
    print(colored("\nOUR OFFER: ", color=COLOR_THEME, attrs=['bold']))
    for number, item in all_products.items():
        print(f"{number + 1}. {item}")

    print(colored("\n__Leave at least one of the fields empty if you want to close the bill__",
                  color=COLOR_THEME, attrs=['bold']))
    while True:
        which_product = input("\nEnter a # of the product you want to purchase: ")
        quantity = input("How many units do you want to buy?: ")

        if which_product != "" or quantity != "":
            try:
                which_product = int(which_product)
                quantity = int(quantity)
                product_to_shop = best_buy.products[which_product - 1]
                if products.Product.is_active(product_to_shop) and quantity > 0:
                    shopping_list.append((product_to_shop, quantity))
                else:
                    print(order_error)
            except IndexError:
                print(order_error)
            except ValueError:
                print(order_error)
        else:
            break
    return shopping_list


def main():
    """
    Initializes Store object and runs store simulation
    """
    # setup initial stock of inventory
    product_list = [products.Product("M", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250.99, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]

    # initialises best_buy as a Store object
    best_buy = store.Store(product_list)

    # starts the shop simulator
    start(best_buy)


if __name__ == "__main__":
    main()
