from shutil import which

import store
import products
import sys

def start(best_buy):

    actions = {1: best_buy.get_all_products,
               2: best_buy.get_total_quantity,
               3: best_buy.order,
               }

    while True:
        print("""
    STORE MENU:
    1. List all products in store
    2. Show total amount in store
    3. Make an order
    4. Quit\n""")

        while True:
            try:
                user_choice = int(input("Please choose a number: "))
                print()
                if user_choice not in [1, 2, 3, 4]:
                    pass
                else:
                    break
            except ValueError:
                print("Enter a valid option")

        if user_choice == 1:
            all_products = actions[user_choice]()
            number  = 1
            print("OUR PRODUCTS:")
            for item in all_products.values():
                print(f"{number}. {item}")
                number += 1

        elif user_choice == 2:
            total = actions[user_choice]()
            print(f"Total amount of items in store: {int(total)}")

        elif user_choice == 3:
            shopping_list = []
            all_products = actions[1]()
            print("OUR OFFER: ")
            for number, item in all_products.items():
                print(f"{number+1}. {item}")

            print("Leave at least one of the fields empty if you want to close the buy.")
            while True:
                which_product = input("Enter a # of the product you want to purchase: ")
                quantity = input("How many units do you want to buy?: ")
                if which_product == "" or quantity == "":
                    break
                else:
                    try:
                        which_product = int(which_product)
                        quantity = int(quantity)
                        shopping_list.append((best_buy.products[which_product-1], quantity))
                    except IndexError:
                        print("Error when making order.")
                    except ValueError:
                        print("Error when making order.")

            actions[user_choice](shopping_list)

        elif user_choice == 4:
            print("Thank you for shopping with us!")
            sys.exit()



def main():
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]

    best_buy = store.Store(product_list)
    start(best_buy)

if __name__ == "__main__":
    main()