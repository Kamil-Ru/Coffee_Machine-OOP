from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
machine = CoffeeMaker()
menu_coffee = Menu()

while True:
    user_choice = input(f"What would you like? {menu_coffee.get_items()}: ")
    if user_choice == "q":
        break
    elif user_choice == "report":
        machine.report()
        money_machine.report()
    elif user_choice in ["latte", "espresso", "cappuccino"]:
        order = menu_coffee.find_drink(user_choice)
        if machine.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
            machine.make_coffee(order)