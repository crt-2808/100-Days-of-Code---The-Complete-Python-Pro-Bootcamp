import art
import data
import random

print(art.logo)

MAX_SCORE=0
continue_game=False

celeb1=random.randint(0,49)
celeb2=random.randint(0,49)
while not continue_game:    
    print(f"Compare A {data.data[celeb1]["name"]}, a {data.data[celeb1]["description"]} from {data.data[celeb1]["country"]}")
    print(art.vs)
    print(f"Compare B {data.data[celeb2]["name"]}, a {data.data[celeb2]["description"]} from {data.data[celeb2]["country"]}")
    user_input=input("Select A or B: ")
    if user_input=="A":
        if data.data[celeb1]["follower_count"]>=data.data[celeb2]["follower_count"]:
            MAX_SCORE+=1
        else:
            print(f"You guess it wrong, your score was: {MAX_SCORE}")
            continue_game=True
    elif user_input=="B":
        if data.data[celeb2]["follower_count"]>=data.data[celeb1]["follower_count"]:
            MAX_SCORE+=1
            celeb1=celeb2
        else:
            print(f"You guess it wrong, your score was: {MAX_SCORE}")
            continue_game=True
    celeb2=random.randint(0,49)