from menu import MENU

print(MENU)

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# 製作 3種口味 (Makes 3 hot flavours)
# 1. Expresso
# 2. Latte
# 3. Cappuccino

# Coin Operated
# Quarter: $0.25
# Dime:    $0.1
# Nickel:  $0.05
# Penny:   $0.01

# 判斷要產生哪一種功能:
def check_input(input):
    if input == "expresso":
        print("Expresso")
    elif input == "latte":
        print("latte")
    elif input == "cappuccino":
        print("cappuccino")
    elif input == "result":
        print("Result")
    else:
        print("Wrong entering")

# 計算價錢
def calculate(quarter, dime, nickel, penny):
    total = (quarter * 0.25) + (dime * 0.1) + (nickel * 0.05) + (penny * 0.01)
    print(f"USD $ { total }")
    return total

# Requirements
# TODO: 1. Print report
result = input("What would you like? ( Expresso / Latte / Cappuccino): ").lower()

# TODO: 2. Check resources sufficient? 確認資源是否足夠
check_input(result)

# TODO: 3. Process coin
print("Please insert coins.")
quarter = int(input("How many quarters ? $ "))
dime    = int(input("How many dime ? $ "))
nickel  = int(input("How many nickel ? $ "))
penny   = int(input("How many penny ? $ "))
calculate(quarter=quarter, dime=dime, nickel=nickel, penny=penny)

# TODO: 4. Check transaction successful?


# TODO: 5. Make coffee.