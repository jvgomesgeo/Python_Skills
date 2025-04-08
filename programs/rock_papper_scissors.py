import random

lista_choices = ['rock','papper','scissors']

dict_ = {'rock' : 'papper',
         'papper': 'scissors',
         'scissors' : 'rock'}

while True:
    answer = random.choice(lista_choices)
    guess = input("Choose your object: rock, papper or scissors")

    if guess.isalpha():
        
        if  answer == 'rock' and guess == dict_.get(answer):
            print(f"You Win ! {guess} beats {answer}")
            break
        
        elif answer == 'papper' and guess == dict_.get(answer):
            print(f"You Win ! {guess} beats {answer}")
            break
        
        elif answer == 'scissors' and guess == dict_.get(answer):
            print(f"You Win ! {guess} beats {answer}")
            break

        else:
            print(f"You Lose ! {answer} beats {guess}")
        
    else:
        print("Choose a valid value !")
