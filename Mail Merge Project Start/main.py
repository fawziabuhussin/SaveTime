
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
    letter  = letter_file.read()

for name in names:
        #strip "\n"
        new_name = name.strip("\n")
        #replace the names.
        with open(f"./Output/ReadyToSend/letter_for_{new_name}", "w") as new_file:
            new_file.write(letter.replace(PLACEHOLDER, new_name))



