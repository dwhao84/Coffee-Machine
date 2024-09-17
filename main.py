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

# 製作 3種口味 (Makes 3 hot flavours)
# 1. Expresso
# 2. Latte
# 3. Cappuccino

# Coin Operated
# Quarter: $0.25
# Dime:    $0.1
# Nickel:  $0.05
# Penny:   $0.01

# Requirements
# TODO: 1. Print report
# TODO: 2. Check resources sufficient? 確認資源是否足夠
# TODO: 3. Process coin
# TODO: 4. Check transaction successful?
# TODO: 5. Make coffee.

result = input("What would you like? ( Expresso / Latte / Cappuccino): ")
print("Please insert coins.")
print("How many quarters?")
print("How many dime?")
print("How many nickel?")
print("How many penny?")
