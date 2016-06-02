import random

def max3(i):
    m = 0
    
    for t in range(len(i)):
        if i[t] > i[m]: m = t
    
    return m

#print(max3(3,4,5))

def rps(smart_choose, hist=[0, 0, 0]):

    print(hist)

    def choose():
        if smart_choose:
            if hist[0] == hist[1] == hist[2]:
                return random.randint(0, 2)
            else:
                return max3(hist)
    
    choices = ['rock', 'paper', 'scissors']

    p_choice = raw_input("Rock, Paper, or Scissors?: ")

    if p_choice in choices:
        hist[int(p_choice)] += 1
        p_choice = choices.index(int(p_choice))
        print("you chose " + choices[int(p_choice)])
        a_choice = choose()
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
    
    return hist


    
hist = rps(True)

while True:
    print("")
    again = raw_input("Do you want to play again? (y/n): ")
    print("")
    if again == 'y' or again == 'yes': rps(True, hist)
    else: break
        

