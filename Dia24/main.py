#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER="[name]"

with open("C:/Users/ramos/OneDrive/Documentos/Udemy/100-Days-of-Code---The-Complete-Python-Pro-Bootcamp/Dia24/Input/Names/invited_names.txt") as names_file:
    names = [name.strip() for name in names_file.readlines()]

with open("C:/Users/ramos/OneDrive/Documentos/Udemy/100-Days-of-Code---The-Complete-Python-Pro-Bootcamp/Dia24/Input/Letters/starting_letter.txt") as letter_file:
    letter_content=letter_file.read()
    for name in names:
        striptname=name.strip()
        new_letter=letter_content.replace(PLACEHOLDER, name)
        with open(f"C:/Users/ramos/OneDrive/Documentos/Udemy/100-Days-of-Code---The-Complete-Python-Pro-Bootcamp/Dia24/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)