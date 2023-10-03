from art import logo
import random

print(logo)

user_score=0
computer_score=0
is_game_over=False

def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10]
    card=random.choice(cards)
    return card

def calculate_score(card_deck):
    if sum(card_deck)==21 and len(card_deck)==2:
        return 0
    
    if 11 in card_deck and sum(card_deck)>21:
        card_deck.remove(11)
        card_deck.append(1)
    return sum(card_deck)


def compare(user_score, computer_score):
    if user_score==computer_score:
        return "It's a Draw"
    elif computer_score==0:
        return "The computer have Blackjack, you lose"
    elif user_score==0:
        return "You have Blackjack, you win"
    elif user_score>21:
        return f"You have {user_score}, you lose"
    elif computer_score>21:
        return f"Computer have {computer_score}, you win"
    elif user_score>computer_score:
        return f"You have win having {user_score} and computer {computer_score}"
    else:
        return f"You lose having {user_score} and computer {computer_score}"

user_cards=[]
computer_cards=[]

for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


while not is_game_over:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)

    print(f"Your cards are {user_cards} and your score is {user_score}")
    print(f"Computer first card is {computer_cards[0]}")

    if user_score==0 or computer_score==0 or user_score>21:
        is_game_over=True
    else:
        user_should_deal=input("Type 'y' to get another card or 'n' to pass: ")
        if user_should_deal=="y":
            user_cards.append(deal_card())
        else:
            is_game_over=True


while computer_score !=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)
    

print(compare(user_score, computer_score))




