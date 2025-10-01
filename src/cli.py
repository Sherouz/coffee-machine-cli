# cli.py
from src.menu import Menu
from src.coffee_maker import CoffeeMaker
from src.money_machine import MoneyMachine


def handle_choice(choice, menu, coffee_maker, money_machine):
    """Process user input choice and execute the corresponding action."""
    if choice == 'off':
        print("Shutting down machine...\n")
        return False  # Signal to stop main loop
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
        return True

    drink = menu.find_drink(choice)
    if drink is None:
        print("Invalid selection. Please choose a drink from the menu.")
        return True

    if coffee_maker.is_resource_sufficient(drink):
        if money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    return True


def run_coffee_machine():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    is_on = True
    try:
        while is_on:
            menu.show_menu()
            try:
                choice = input("\nSelect your drink (or 'report'/'off'): ").strip().lower()
                is_on = handle_choice(choice, menu, coffee_maker, money_machine)
            except KeyboardInterrupt:
                print("\nOperation cancelled. Going back to main menu.")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Goodbye!")
