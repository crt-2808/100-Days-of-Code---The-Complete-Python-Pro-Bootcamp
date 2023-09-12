import random
word_list=["camello", "perro","gato"] 
selected_word=random.choice(word_list)
guess=input("Dime una letra que pueda estar en la palabra: ").lower()
for letter in selected_word:
    if letter==guess:
        print(f"There is a {guess}")
    else:
        print("You lost one part")