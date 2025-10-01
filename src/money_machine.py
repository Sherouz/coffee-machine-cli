# src/money_machine.py

from decimal import Decimal, InvalidOperation

class MoneyMachine:
    CURRENCY = "$"

    def __init__(self):
        self.profit = Decimal("0.00")

    def report(self):
        print(f"\nProfit: {self.CURRENCY}{self.profit}")
        print("="*65, "\n")

    def make_payment(self, cost):
        cost = Decimal(str(cost))
        while True:
            try:
                user_input = input(f"Please insert ${cost} or more: ").strip()
                money_received = Decimal(user_input)
                if money_received < cost:
                    print("Not enough money. Please insert the correct amount.")
                    continue
                break
            except (InvalidOperation, ValueError):
                print("Invalid input. Enter a number (e.g. 2.5).")
            except KeyboardInterrupt:
                print("\nPayment cancelled by user.")
                return False

        change = (money_received - cost).quantize(Decimal("0.01"))
        self.profit += cost
        if change > 0:
            print(f"\nHere is {self.CURRENCY}{change} in change.")
        return True