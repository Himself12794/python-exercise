import random

def max3(v1, v2, v3):
    i = [v1, v2, v3]
    
    m = v1
    
    for t in i:
        if t > m: m = t
    
    return m

#print(max3(3,4,5))

def rps():
    choices = ['rock', 'paper', 'scissors']

    p_choice = input("Rock, Paper, or Scissors?: ")

    if p_choice in choices:
        p_choice = choices.index(p_choice)
        print("you chose " + choices[p_choice])
        a_choice = random.randint(0, 2)
        print("The computer chose " + choices[a_choice])

        if p_choice == a_choice: print("It's a tie!")
        elif p_choice == 0:
            if a_choice == 1: print("You lose!")
            else: print("You win!")
        elif p_choice == 1:
            if a_choice == 0: print("You win!") 
            else: print("You lose!")
        else:
            if a_choice == 0: print("You win!")
            else: print("You lose!")

    else: print("Not a valid choice!")

rps()

while True:
    print()
    again = input("Do you want to play again? (y/n): ")
    print()
    if again == 'y' or again == 'yes': rps()
    else: break
        

