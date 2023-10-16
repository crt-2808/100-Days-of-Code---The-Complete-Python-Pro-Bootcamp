import random

GUESS_NUMBER= random.randint(1,100)

def check_number(number):
    if number>GUESS_NUMBER:
        return("Too high. \nGuess again.")
    elif number<GUESS_NUMBER:
        return("Too low. \nGuess again.")
    
def less_life(attemps):
    attemps-=1
    return attemps

def hard_level():
    player_attemps=5
    while player_attemps!=0:
        print(f"You have {player_attemps} attempts to guess the number.")
        user_guess=int(input("Make a guess: "))
        if user_guess!=GUESS_NUMBER:
            print(check_number(user_guess))
            player_attemps=less_life(player_attemps)
        else:
            return(f"You got it! the number was {GUESS_NUMBER}")
    return(f"You didn't got it, the number was {GUESS_NUMBER}")
        
        
def easy_level():
    player_attemps=10
    while player_attemps!=0:
        print(f"You have {player_attemps} attempts to guess the number.")
        user_guess=int(input("Make a guess: "))
        if user_guess!=GUESS_NUMBER:
            print(check_number(user_guess))
            player_attemps=less_life(player_attemps)
        else:
            return(f"You got it! the number was {GUESS_NUMBER}")
    return(f"You didn't got it, the number was {GUESS_NUMBER}")
                
    
    
print("Welcome To The Guessing Number!")
print("I'm thinking of a number between 1 and 100")
difficult=input("Choose a difficulty. Type 'easy' or 'hard: ")

if difficult.lower() == "easy":
    print(easy_level())
elif difficult.lower()=="hard":
    print(hard_level())