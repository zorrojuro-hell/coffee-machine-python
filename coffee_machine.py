from menu import resources
from menu import menu

while True:
    def get_order():
        order = input("what would you like ? espresso/latte/cappucino : ")
        print(order)
        if order == "latte":
            print(menu.latte)
            print()
        elif order == "espresso":
            print(menu.espresso)
        elif order == "cappucino":
            print(menu.cappucino)
        elif order == "off":
            print("coffee machine is turning off for maintanence")
    get_order()


