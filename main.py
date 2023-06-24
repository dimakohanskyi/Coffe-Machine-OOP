from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True


coffee_maker.report()
money_machine.report()




while is_on:
    options = menu.get_items()
    chooice = input(f"What would you like? ({options}): ")
    if chooice == "off":
        is_on = False
    elif chooice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(chooice)                    #save our result from input in variable
        if coffee_maker.is_resource_sufficient(drink):      #Check resources sefficient ###
            if money_machine.make_payment(drink.cost):      ### check transaction
                coffee_maker.make_coffee(drink)             ## result ready rorder





