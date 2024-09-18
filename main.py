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
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 50
}

should_continue = True
current_money = resources["money"]
selected_drinks_cost = 0
inserted_coin = 0
user_selection = ""

# TODO: 1. Print report
def show_report():
    water  = resources["water"]
    milk   = resources["milk"]
    coffee = resources["coffee"]
    money  = resources["money"]
    print(f"Water:{ water }ml \nmilk: { milk }ml \ncoffee: { coffee }g \nmoney: $ {money}")

# TODO: 2. Check resources sufficient? 確認資源是否足夠
def entered_prompt(prompts):
    if MENU[prompts]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
    elif MENU[prompts]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.")
    elif MENU[prompts]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
    else:
        print("We have enough resources, We're ready to go.")

# Make sure the leftover resources.
def calculated_leftover(prompts):
    leftover_water = resources["water"] - MENU[prompts]["ingredients"]["water"]
    leftover_milk = resources["milk"] - MENU[prompts]["ingredients"]["milk"]
    leftover_coffee = resources["coffee"] - MENU[prompts]["ingredients"]["coffee"]
    income         = resources["money"] + MENU[prompts]["cost"]
    print(f"Water:{ leftover_water }ml \nmilk: { leftover_milk }ml \ncoffee: { leftover_coffee }g \ncurrent bank account: $ {income}")

# TODO: 3. Process coin
def insert_coins():
    print("Please insert coins.")
    quarter = int(input("How many quarters ? $ "))
    dime    = int(input("How many dime ? $ "))
    nickel  = int(input("How many nickel ? $ "))
    penny   = int(input("How many penny ? $ "))
    inserted_coins = (quarter * 0.25) + (dime * 0.1) + (nickel * 0.05) + (penny * 0.01)
    print(f"USD $ { inserted_coins }")
    return inserted_coins

# TODO: 4. Check transaction successful?
def transaction_checking(inserted_coin):
    if inserted_coin > selected_drinks_cost:
        print("We've enough money.")
    elif inserted_coin == selected_drinks_cost:
        print("I found just the right amount of money. ")
    else:
        print("Will make your coffee later.")

# ========================================================================================================

while should_continue:
    # Requirements
    prompt = input("What would you like? ( Expresso / Latte / Cappuccino): ").lower()

    # 判斷要產生哪一種功能:
    if prompt == "expresso":
        selected_drinks_cost = MENU[prompt]["cost"]
        print(f"Drink cost $ { selected_drinks_cost }")
        entered_prompt(prompts=prompt)
        inserted_coin = insert_coins()
        
        user_selection = prompt
        
        transaction_checking(inserted_coin=inserted_coin)
        
        calculated_leftover(prompts=prompt)  # 包含selected_drinks_cost
        print(f"Here is your {user_selection}. Enjoy!")
        
    elif prompt == "latte":
        selected_drinks_cost = MENU[prompt]["cost"]
        print(f"Drink cost $ { selected_drinks_cost }")
        entered_prompt(prompts=prompt)
        inserted_coin = insert_coins()
        user_selection = prompt
        
        transaction_checking(inserted_coin=inserted_coin)

        calculated_leftover(prompts=prompt)  # 包含selected_drinks_cost
        print(f"Here is your {user_selection}. Enjoy!")
    
    elif prompt == "cappuccino":
        selected_drinks_cost = MENU[prompt]["cost"]
        print(f"Drink cost $ { selected_drinks_cost }")
        entered_prompt(prompts=prompt)
        inserted_coin = insert_coins()
        
        user_selection = prompt
        transaction_checking(inserted_coin=inserted_coin)
        
        calculated_leftover(prompts=prompt)  # 包含selected_drinks_cost
        print(f"Here is your {user_selection}. Enjoy!")
        
    elif prompt == "report":
        show_report()
    
    elif prompt == "off":
        should_continue = False
        print("Coffee Machine is turning off.")

    else:
        should_continue = False
        print("Wrong entering")

