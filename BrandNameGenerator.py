
import random


#User input
#task - 1
print("Welcome to the Band Name Generator. 🐾✨") # It will print the welcome message.
# input is stored in the username variable
city = input("what's the name of the city you grew up in?\n")
petname = input("what's your pet name?\n")
adjectives = ["Fluffy", "Sparkly", "Tiny", "Happy", "Bubbly", "Sweet"]
emojis = ["🐶", "🐱", "🌸", "🍭", "🦄", "💖"]
print('Your band name could be: ' + city + ' ' + petname)
 #random selections
adj = random.choice(adjectives)
emoji = random.choice(emojis)
num = random.randint(1, 99)

print(f'Your band name could be: {adj} {city} {petname}{num}{emoji}')


# #task - 2
print("welcome to the tip calculator!")
Bill = float(input("What was the total bill?$ "))
Tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
Tip_as_percent = float(Tip/100)
Split_bill = int(input("How many people to split the bill? "))
Tip_amount = Bill * Tip_as_percent
Total_bill = (Bill + Tip_amount)/Split_bill
print(f'Each person should pay: ${Total_bill:.2f}')

#task - 3
print("Welcome to Python Pizza Deliveries!!!")
size = input("What size pizza do you want? S, M Or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y Or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y Or N: ").lower()
bill = 0

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25
else:
    print("You typed the wrong input!!!")

if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "y":
    bill += 1
print(f"Your Final Bill: ${bill}")


#Challenge Task
print(r"""                           ,~~'''#**..
                        ,"':: ~>!'.!"#**.
                     ,'" '       ~~' <';
              ,P               .MMXRh.>=-.uz~d$WWB$$      ;
             ;"                !XMMXX$$@N*TW4$$$$$$$Ne... ;
            F                  !M!!RMXXS@$$*<$$$$$$$$$$$$!<
          d"        xx         4!K?!XMR$59@$`$$#BQ$$$$$$P'8
         P         d$#         !MX!RM!SM$$$WX$%P"  `("),.:
       ," `        ^ ?        :!X@MXXRMMN9$$S9$     )r#ze
      .F '          k~        'Xt!X%MXHRM8@XR!R     4$@
      R   `         `         '!!XMX!RMMMR!$9!R     ';
      > ~                      XM!>?MXX5!XB?M$t      #WeeWX*.
      f                        ~!X !!R?XXRM@$9!        e"!#\I
      >                        'M! ~!XX%!Xt?M$!L . .. '".o@P
      E                         `! '!`!X!""fMMX$buuuoeeePd'
      E `                        '  ~ !      `#09P
      F                                        (#;,
     d  -                                        #*o,.
     R                                            ^#*$$RR
     F <`                                         ' **'
     >~'                                           `~R;
    #  ~~                                        <~  4?,
   ,F `                                        !<:!X!        '  ~   `!X! ;
        z@$$$$$MUFASA$M@NRF$$TKMM!!RM!X!               ~~~ 8
      .@$$$$$9M@$MMB$MB$R@8AEB$MXRMX!!!X.                 :;
     u$$$$$$R@$RK$$@6$$@B$@$SMZBMXXM?XX?!                 P'
    d$$$$$$$BMM$$M&$$8$$$$$$$A$9&BMXX?MXX                @
   @$$$$$$$$M$B9E$$WB$$$$$$$$$$$$MKRMXX?!>              d'""")

print("Welcome to the Wild Forest 🌲🌲🌲🌲\nA dangerous land where shadows lurk and the mighty Lion King rules supreme... \nYour mission: Survive the hunt, outsmart the King, and find your way to freedom!\n")
direction = str(input("🌲 You stand at a forked path deep in the forest.\nWhich way will you go?\n        Type ‘left’ or ‘right’ to choose your path.")).capitalize()
if direction == 'Left':
    direction = (str(input("🏞 You arrive at a wide pond. \n what would you like to do? 'Swim' Or 'Wait'? \n"))).capitalize()
    if direction == 'Wait':
        direction = str(input("⏳ As you wait, a secret stone bridge slowly rises from the water!\nDo you take the bridge 'Left' or the bridge 'Right'? \n")).capitalize()
        if direction == "Right":
            print("🎉 Victory! The bridge leads you safely out of the forest. You’ve escaped the Lion King’s domain! ")
        else:
            print("🦁 Suddenly, the Lion King blocks your path!\nYou fought bravely, but this time… the forest wins. Game Over.")
    else:
        print("🐊 A giant crocodile lunges from the pond!\nYou never stood a chance. Game Over.")
else:
    print("🌑 The forest grows darker... too dark. Suddenly—\n🦁 The Lion King pounces from the shadows!\nGame Over.")

#Task - 4

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_list = [rock, paper, scissors]

try:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if user_choice < 0 or user_choice > 2:
        print("You typed invalid number. Please Enter 0, 1 or 2 Try again!!!")
    else:
        print(game_list[user_choice])
        print("Computer chose:")
        computer_choice = random.randint(0, 2)
        print(game_list[computer_choice])
        if user_choice == computer_choice:
            print("It's a draw!")
        elif user_choice == 0 and computer_choice == 2:
            print("You won!")
        elif user_choice == 2 and computer_choice ==0:
            print("You lose!")
        elif user_choice == 2 and computer_choice == 1:
            print("You won!")
        else:
            print("You lose!")
except ValueError:
    print("Invalid Input!! Please Enter 0, 1 or 2")

#Task 5
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
while True:
    nr_letters = input("How many letters would you like in your password?\n")
    if nr_letters.isdigit() and int(nr_letters) > 0:
        nr_letters = int(nr_letters)
        break
    else:
        print("Invalid Input!!! Please enter numbers that are greater than Zero ")
while True:
    nr_symbols = input("How many symbols would you like?\n")
    if nr_symbols.isdigit() and int(nr_symbols) > 0:
        nr_symbols = int(nr_symbols)
        break
    else:
        print("Invalid Input!!! Please enter numbers that are greater than Zero ")

while True:
    nr_numbers = input("How many numbers would you like?\n")
    if nr_numbers.isdigit() and int(nr_numbers) > 0:
        nr_numbers = int(nr_numbers)
        break
    else:
        print("Invalid Input!!! Please enter numbers that are greater than Zero ")

password = []

for l in range(nr_letters):
        password.append(random.choice(letters))

for s in range(nr_symbols):
        password.append(random.choice(symbols))

for n in range(nr_numbers):
        password.append(random.choice(numbers))

random.shuffle(password)
password_string = ''.join(password)
print(f'Here is your unique password: {password_string}')

# practice work from https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# This code works in above site
# # Task 6 :
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# while front_is_clear():
#     move()
# turn_left()
#
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()

#Task 7

import random
import hangman_words
from hangman_art import stages, logo
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print(f"****************************<???>/ {lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in correct_letters:
        print(f"You've already guessed: {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter

        else:
            display += "_"


    print("Word to guess: " + display)

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word:
        lives -= 1
        print(f" You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"***********************IT WAS {chosen_word}! YOU LOSE!!!! Try Again **********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
    print(stages[lives])
