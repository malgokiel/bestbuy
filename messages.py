from termcolor import colored

ERROR_COLOR_THEME = 'light_red'

invalid_input = colored("Invalid option was given.", color=ERROR_COLOR_THEME)
order_error = colored("Error when placing order:", color=ERROR_COLOR_THEME)
decorator = "^" * 30