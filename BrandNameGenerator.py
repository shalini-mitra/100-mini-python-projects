#task - 1
import random
#User input

"""print("Welcome to the Band Name Generator. 🐾✨") # It will print the welcome message.
# input is stored in the username variable
city = input("what's the name of the city you grew up in?\n")
petname = input("what's your pet name?\n")
adjectives = ["Fluffy", "Sparkly", "Tiny", "Happy", "Bubbly", "Sweet"]
emojis = ["🐶", "🐱", "🌸", "🍭", "🦄", "💖"]
#print('Your band name could be: ' + city + ' ' + petname)
#random selections
adj = random.choice(adjectives)
emoji = random.choice(emojis)
num = random.randint(1, 99)

print(f'Your band name could be: {adj} {city} {petname}{num}{emoji}')


#task - 2
print("welcome to the tip calculator!")
Bill = float(input("What was the total bill?$ "))
Tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
Tip_as_percent = float(Tip/100)
Split_bill = int(input("How many people to split the bill? "))
Tip_amount = Bill * Tip_as_percent
Total_bill = (Bill + Tip_amount)/Split_bill
print(f'Each person should pay: ${Total_bill:.2f}')"""

#task - 3
print("Welcome to Python Pizza Deliveries!!!")

size = input("What size pizza do you want? S, M Or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y Or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y Or N: ").upper()
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong input!!!")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your Final Bill: ${bill}")