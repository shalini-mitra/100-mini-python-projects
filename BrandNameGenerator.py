#task - 1
import random
#User input

print("Welcome to the Band Name Generator. 🐾✨") # It will print the welcome message.
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