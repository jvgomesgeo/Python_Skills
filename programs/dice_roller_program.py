import random 


#print("\u25CF \u250C \u2500 \u2510 \u2514 \u2518")

# ● ┌ ┌ ┐ └ ┘


"┌─────────────┐"
"|             |"
"|             |"
"|             |"
"|             |"
"└─────────────┘"

dice_art = {
            1: ("┌────────────┐", 
                "|            |",
                "|            |",
                "|      ●     |",
                "|            |",
                "|            |",
                "└────────────┘",
                ),
            2: ("┌────────────┐", 
                "|  ●         |",
                "|            |",
                "|            |",
                "|            |",
                "|         ●  |",
                "└────────────┘",   
            ),

            3: ("┌────────────┐", 
                "|  ●         |",
                "|            |",
                "|      ●     |",
                "|            |",
                "|         ●  |",
                "└────────────┘"
                ),
            
            4: ("┌────────────┐", 
                "|  ●      ●  |",
                "|            |",
                "|            |",
                "|            |",
                "|  ●      ●  |",
                "└────────────┘"
                ),
            5: ("┌────────────┐", 
                "|  ●      ●  |",
                "|            |",
                "|      ●     |",
                "|            |",
                "|  ●      ●  |",
                "└────────────┘"
                ),
            6: ("┌────────────┐", 
                "|  ●     ●   |",
                "|            |",
                "|  ●     ●   |",
                "|            |",
                "|  ●      ●  |",
                "└────────────┘"
                )

}

dice = []
total = 0
num_of_dice = int(input("How many dices?: "))


for d in range(1, num_of_dice+1):
    dice.append(random.randint(1,6))

#for index in range(num_of_dice):
#    for line in dice_art.get(dice[index]):
#        print(line)


#printing in a sigle line
for line in range(7):
    for die in dice:
        print(dice_art.get(die)[line], end= "")
    print()



for x in dice:
    total += x

print(f"The total is {total}")
    