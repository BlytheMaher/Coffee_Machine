coffee_machine = {
    "coffee": 1000,
    "milk": 2000,
    "water": 3000
    } #dictioary for the capacity of the machine
recipes ={
"espresso":{"water":50,"coffee":18},# dictionary nested in dictionary
"latte":{"water":200,"coffee":24,"milk":150},
"cappuccino":{"water":350,"coffee":24,"milk":100}
}

price = {
 "espresso" :  22,
 "latte" : 35,
 "cappuccino" : 38

 }

#deducting whats used from the coffe drink to make the drink
def coffee_used(coffee_type):
    if coffee_type in recipes:
        for ingredient,amount in recipes[coffee_type].items():
            if coffee_machine[ingredient] >= amount:
                coffee_machine[ingredient] -= amount

            else:
                return(f"Not enough {ingredient} to make {coffee_type}")
        return(f"{coffee_type} is ready!")
    else:
        return("Invalid coffee selection")

#dealing with the money
def calculator(coins,coffee_type): 
# R1 R2 R5
   total_change = 0
   if coins < 0:
        return("Please insert coins: R ")

   if coffee_type not in price:
        return "Invalid coffee selection."

   total_change = coins - price[coffee_type]  # Change calculation
   #print(f"R{total_change}")
    
# If not enough money
   while total_change < 0:
       print(f"Not enough money. You need R{abs(total_change)} more")
       try:
            extra_coins = int(input("Please insert more coins: R"))
            coins += extra_coins
            total_change = coins - price[coffee_type]
       except ValueError:
            print("Invalid input! Please enter a number.")

    # abs converts -ve to +ve
   return f"Enjoy your {coffee_type}! Your change is R{total_change}."

# getting users input
while True:
    coffee_type = input("What would you like (espersso/latte/cappuccino): ").strip().lower()

    if coffee_type == "report":
        print(f"Water: {coffee_machine['water']}ml")
        print(f"Milk: {coffee_machine['milk']}ml")
        print(f"Coffee: {coffee_machine['coffee']}g")
        coffee_type = input("What would you like (espersso/latte/cappuccino): ")
        continue

    if coffee_type == "exit":
        print("Thank you for using the coffee machine! ")
        break  # Exit the loop and end program

    if not coffee_type:
        print("Please select a coffee.")
        continue 

    while True:
        try:
            coins = int(input("Please insert coins: R "))  # Converts input to integer
            break  # Exit loop if input is valid
        except ValueError: # handles inappropriate values - user eneters text instaed of integer
            print("Invalid input! Please enter a number.")  # Repeats input prompt

    print(f"You inserted R{coins}")
    print(calculator(coins,coffee_type))

    coffee_used(coffee_type)

    another_coffee = input("Would you like another coffee? Y/N: ").strip().lower()
    if another_coffee == "N":
        print("Thank you for using the coffee machine!")
        break  # Exit loop if user says anything other than "yes"
  
 

       