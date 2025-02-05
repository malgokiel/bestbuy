from termcolor import colored

invalid_input = colored("Invalid option was given.", color='light_red')
order_error = colored("Error when placing order. Try again.", color='light_red')
decorator = "^" * 30