from menu import MENU

# 製作 3種口味 (Makes 3 hot flavours)
# 1. Expresso
# 2. Latte
# 3. Cappuccino

# Coin Operated
# Quarter: $0.25
# Dime:    $0.1
# Nickel:  $0.05
# Penny:   $0.01

# print(MENU)

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 50
}

current_money = resources["money"]
selected_drinks_cost = 0
user_selection = ""

# 顯示目前庫存數:
def show_report():
    water  = resources["water"]
    milk   = resources["milk"]
    coffee = resources["coffee"]
    money  = resources["money"]
    print(f"Water:{ water }ml \nmilk: { milk }ml \ncoffee: { coffee }g \nmoney: $ {money}")

# 判斷要產生哪一種功能:
def check_input(entered_prompt):
    if entered_prompt == "expresso":
        print(MENU["espresso"]["ingredients"])
        selected_drinks_cost = MENU["espresso"]["cost"]
        print(selected_drinks_cost)

    elif entered_prompt == "latte":
        print(MENU["latte"]["ingredients"])
        selected_drinks_cost = MENU["latte"]["cost"]
        print(selected_drinks_cost)

    elif entered_prompt == "cappuccino":
        print(MENU["cappuccino"]["ingredients"])
        selected_drinks_cost = MENU["cappuccino"]["cost"]
        print(selected_drinks_cost)

    elif entered_prompt == "report":
        show_report()

    elif entered_prompt == "off":
        print("Coffee Machine is turning off.")

    else:
        print("Wrong entering")



# 計算價錢
def calculate(quarters, dimes, nickels, pennys, drinks_cost):
    total = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennys * 0.01)
    print(f"USD $ { total }")
    print(drinks_cost)

    if current_money > total and total >= drinks_cost:
        print("Is enough money")
        print(current_money, total, drinks_cost)

    elif current_money == total and total == drinks_cost:
        print("Just enough")
        print(current_money, total, drinks_cost)

    else:
        print("Sorry that's not enough money. Money refunded.")


# Requirements
# TODO: 1. Print report
prompt = input("What would you like? ( Expresso / Latte / Cappuccino): ").lower()
user_selection = prompt
check_input(prompt)

# TODO: 2. Check resources sufficient? 確認資源是否足夠



# TODO: 3. Process coin
print("Please insert coins.")
quarter = int(input("How many quarters ? $ "))
dime    = int(input("How many dime ? $ "))
nickel  = int(input("How many nickel ? $ "))
penny   = int(input("How many penny ? $ "))
calculate(quarters=quarter, dimes=dime, nickels=nickel, pennys=penny, drinks_cost=selected_drinks_cost)

# TODO: 4. Check transaction successful?

# TODO: 5. Make coffee.
print(f"Here is your { user_selection }. Enjoy!")