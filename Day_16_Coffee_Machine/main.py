from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

app_status = True

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

while app_status:
    choice = input(f"What would you like to have? ({menu.get_items()}): ")
    if choice == "off":
        app_status = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

