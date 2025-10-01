# src/menu.py

from decimal import Decimal

class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = Decimal(str(cost))
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    def __init__(self):
        self.menu = [
            MenuItem("latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem("espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem("cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]


    def show_menu(self):
        print("\n" + "-"*20 + " MENU " + "-"*20)
        for item in self.menu:
            print(f"{item.name.title():<12} - ${item.cost}")
        print("-"*50)


    def find_drink(self, order_name):
        for item in self.menu:
            if item.name.lower() == order_name.lower():
                return item
        return None