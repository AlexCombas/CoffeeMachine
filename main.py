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

funds = 0.0


def print_report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {round(funds, 2)}")


def check_resources(drink_choice):
    if drink_choice != "espresso":
        # for latte or cappuccino
        water = MENU[drink_choice]['ingredients']['water']
        milk = MENU[drink_choice]['ingredients']['milk']
        coffee = MENU[drink_choice]['ingredients']['coffee']
        if resources['water'] >= water:
            if resources['milk'] >= milk:
                if resources['coffee'] >= coffee:
                    return True
                else:
                    print("Sorry there is not enough coffee.")
                    return False
            else:
                print("Sorry there is not enough milk.")
                return False
        else:
            print("Sorry there is not enough water.")
            return False
    else:
        # for espresso
        water = MENU[drink_choice]['ingredients']['water']
        coffee = MENU[drink_choice]['ingredients']['coffee']
        if resources['water'] >= water:
            if resources['coffee'] >= coffee:
                return True
            else:
                print("Sorry there is not enough coffee.")
                return False
        else:
            print("Sorry there is not enough water.")
            return False


def provide_change(quart, nick, dime, cost):
    t_cost = cost * 1.0
    t_quart = quart * 1.0
    t_nick = nick * 1.0
    t_dime = dime * 1.0
    close_enough = False
    while not close_enough:
        if t_cost >= 0.25 and t_quart != 0:
            t_cost -= 0.25
        elif t_cost >= 0.1 and t_dime != 0:
            t_cost -= 0.1
        elif t_cost >= 0.05 and t_nick != 0:
            t_cost -= 0.05
        elif t_cost <= 0:
            close_enough = True
    change = (t_quart * 0.25) + (t_nick * 0.05) + (t_dime * 0.1)
    print(f"Here is ${round(change, 2)} in change")


def process_coins(drink_choice):
    global funds
    cost = MENU[drink_choice]['cost']
    print("Please insert coins")
    quart = int(input("Quarters: "))
    nick = int(input("Nickels: "))
    dime = int(input("Dimes: "))
    total = (quart * 0.25) + (nick * 0.05) + (dime * .1)
    if total >= cost:
        funds += cost
        provide_change(quart, nick, dime, cost)
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_drink(the_drink):
    global resources
    if the_drink != "cappuccino":
        resources['water'] -= MENU[the_drink]['ingredients']['water']
        resources['milk'] -= MENU[the_drink]['ingredients']['milk']
        resources['coffee'] -= MENU[the_drink]['ingredients']['coffee']
    else:
        resources['water'] -= MENU[the_drink]['ingredients']['water']
        resources['coffee'] -= MENU[the_drink]['ingredients']['coffee']


turn_off = False
while not turn_off:
    drink = input("What would you like? (espresso/latte/cappuccino): ")

    if drink == "espresso" or drink == "latte" or drink == "cappuccino":
        if check_resources(drink):
            if process_coins(drink):
                make_drink(drink)
                print(f"Here is your {drink}. Enjoy!\n")
    elif drink == "report":
        print_report()
    elif drink == "off":
        print("Goodbye")
        turn_off = True
    else:
        print("input error")
