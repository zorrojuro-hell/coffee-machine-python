menu = {
    "espresso": {
        "ingrediants":{
            "water": 50,
            "coffee":18
        },
        "cost": 150,
    },
    "latte": {
        "ingrediants":{
            "water": 200,
            "coffee":24,
            "milk":150
        },
        "cost": 250,

    },
    "cappuccino": {
        "ingrediants":{
            "water": 250,
            "coffee":24,
            "milk":100,
        },
        "cost": 300,
    }      
    
}

profit = 0


resources = {
    "water":500,
    "coffee":100,
    "milk": 400
}


def stock(order_ingrediants):
    for items in order_ingrediants:
        if order_ingrediants[items] >= resources[items]:
            print(f'Sorry there is not enough {items}.')
            return False
    return True

def process_money():
        print("please insert money : ")
        total = int(input("how many 10 rupees coins "))*10
        total = int(input("how many 100 rupees notes "))*100
        total = int(input("how many 200 rupees notes "))*200
        return total

def transaction_successful(money_received , drink_cost):
    if money_received >= drink_cost: 
        change =round( money_received - drink_cost , 2)
        print(f"here is the change{change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry that's not enough money. Money Refunded")
        return False



def make_coffee(drink_name , order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name}")




while True:
    order = input("what would you like ? espresso/latte/cappucino : ")
    if order == "off":
        break
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = menu[order]
        if stock(drink["ingrediants"]):
            payment = process_money()
            if transaction_successful(payment , drink["cost"]):
                make_coffee(order , drink["ingrediants"])