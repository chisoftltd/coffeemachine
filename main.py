from data import MENU, resources

drink = {}
profit = 0


def is_resource_sufficient(order_ingredients):
    """Method returns True if resources is sufficient and False is not"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


def process_coins():
    """Return total amount of coins inserted"""
    print("Please insert coins.")
    total = int(input("How many £2?: ")) * 2
    total += int(input("How many £1?: ")) * 1
    total += int(input("How many 50p?: ")) * 0.50
    total += int(input("How many 20p?: ")) * 0.20
    total += int(input("How many 10p?: ")) * 0.10
    total += int(input("How many 2p?: ")) * 0.02
    total += int(input("How many 1p?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is enough, and False when it is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Please have £{change} as your change.")
        global profit
        profit += drink_cost
        return True
    else:
        reply = input("Do you add more money? 'y' or 'no': ").lower()
        if reply == "y":
            if is_resource_sufficient(drink['ingredients']):
                payment2 = process_coins()
                if is_transaction_successful(payment2, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"And here is your {drink_name} ☕. Enjoy")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino/report/off): ").lower()
    if choice == "off":
        print("Thank you for stopping, Bye!")
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: £{profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            print(f"Your {choice} cost {drink['cost']}")
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
