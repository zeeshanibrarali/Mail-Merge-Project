# TODO: Create a letter using starting_letter.txt

with open('./Input/Letters/starting_letter.txt') as letter:
    letter_1 = letter.read()

# for each name in invited_names.txt
with open('./Input/Names/invited_names.txt') as names:
    all_names = names.readlines()

for name in all_names:
    stripped_name = name.strip()

    # Replace the [name] placeholder with the actual name.
    new_letter = letter_1.replace('[name]', stripped_name)

    # Save the letters in the folder "ReadyToSend".
    with open(f'./Output/ReadyToSend/letter_for_{stripped_name}.txt', mode='w') as ready:
        ready.write(new_letter)



    
