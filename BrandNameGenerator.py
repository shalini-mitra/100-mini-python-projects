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

print(f"Your Final Bill: ${bill}")"""


#task 4
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


