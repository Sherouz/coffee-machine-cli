# src/coffee_maker.py

class CoffeeMaker:
    def __init__(self):
        self.resources = {"water": 2000, "milk": 2000, "coffee": 1000}


    def report(self):
        print("\n" + "="*20 + " MACHINE REPORT " + "="*20)
        for res, amount in self.resources.items():
            unit = "ml" if res in ["water", "milk"] else "g"
            print(f"{res.title()}: {amount}{unit}")


    def is_resource_sufficient(self, drink):
        for item in drink.ingredients:
            if drink.ingredients.get(item, 0) > self.resources.get(item, 0):
                print(f"Sorry, not enough {item}.")
                return False
        return True


    def make_coffee(self, drink):
        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]
        print(f"Here is your {drink.name} ☕️. Enjoy!")
