latte = { "water":150,"mile":100,"coffee":10},
espresso = {"water":250,"coffee":15},
cappucino = {"water":130, "milk":120,"coffee":15}


def get_order():
    order = input("what would you like ? espresso/latte/cappucino : ")
    print(order)
    if order == "latte":
        print(latte)
    elif order == "espresso":
        print(espresso)
    elif order == "cappucino":
        print(cappucino)

get_order()