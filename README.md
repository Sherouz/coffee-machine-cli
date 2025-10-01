# Coffee Machine CLI ☕

A beginner-friendly Python project simulating a simple coffee machine in the command line.  
The machine can display a menu, process payments, manage resources (water, milk, coffee), and make drinks.

---

## Features ✨
- Display a menu with available drinks
- Process payments with change calculation
- Track resources (water, milk, coffee)
- Generate machine and profit reports
- Safe handling of invalid input and interruptions

---

## Project Structure 📂
```
.
├── cli.py
├── main.py
├── src
│   ├── coffee_maker.py
│   ├── menu.py
│   └── money_machine.py
└── README.md

````

## Installation & Setup ⚙
Clone the repository:
```bash
git clone https://github.com/Sherouz/coffee-machine-cli.git
cd coffee-machine-cli
````

Run the program:

```bash
python main.py
```

### Requirements 
- Python 3.10 or higher  
- Standard Library only (`decimal` is included in Python)  

No external dependencies are required.

---

## Usage 💻

When running the program, you’ll see a menu like this:

```
-------------------- MENU --------------------
Latte        - $2.5
Espresso     - $1.5
Cappuccino   - $3
--------------------------------------------------
```

### Example interaction:

```
Select your drink (or 'report'/'off'): latte
Please insert $2.5 or more: 3
Here is $0.50 in change.

Here is your latte ☕️. Enjoy!
```

### Commands:

* `latte`, `espresso`, `cappuccino` → order a drink
* `report` → view resources and profit report
* `off` → shut down the machine

---

## Example Reports 📄

```
==================== MACHINE REPORT ====================
Water: 800ml
Milk: 850ml
Coffee: 176g

Profit: $2.5
========================================================
```

---

## Contributing 🤝🏽

This is a beginner project for learning Python OOP and CLI applications.
Feel free to fork, explore, and extend it (e.g., add more drinks, use a JSON menu, or add GUI).

---

## License 📃

Distributed under the [MIT License](LICENSE).# coffee-machine-cli
