from pickle import FALSE

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

app_status = True
money = 0.0

def resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    total = 0.25*quarters + 0.1*dimes + 0.05*nickels + 0.01*pennies
    return total

def payment_sufficient(payment, drink_cost):
    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        print(f"Here is ${change} change.")
        global money
        money += drink_cost
        return True
    else:
        print(f"Sorry, that's not enough. Money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


while app_status:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice=="off":
        app_status = False
    elif choice=="report":
        print(f"Water: {resources['water']} \nMilk: {resources['milk']} "
              f"\nCoffee: {resources['coffee']} \nMoney: ${money}")
    else:
        drink = MENU[choice]
        if resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if payment_sufficient(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])



