# modify number gussing GAME
import random
winning_number=random.randint(1,100)
guess=1
number=int(input("guess a number between 1 to 100"))
game_over=False
while not game_over:
    if number==winning_number:
        print(f"you win, and you guessed this number in {guess} times")
        game_over=True
    else:
        if number<winning_number:
            print("too low")
            guess=guess+1
            number=int(input("again guess"))
        else:
            print("too high")
            guess=guess+1
            number=int(input("again guess"))



#dry principle = don't repeat yourself 
#last code game can be written like this
# modify number gussing GAME
import random
winning_number=random.randint(1,100)
guess=1
number=int(input("guess a number between 1 to 100"))
game_over=False
while not game_over:
    if number==winning_number:
        print(f"you win, and you guessed this number in {guess} times")
        game_over=True
    else:
        if number<winning_number:
            print("too low")
            
        else:
            print("too high")
    guess=guess+1# ye dono line phle do bar thi ab ek bar hi he if else loop se bahr niukal kr
    number=int(input("again guess"))




