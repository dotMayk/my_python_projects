import random
import art
import word_list
import os

print(art.logo)
isOn = True
lives = len(art.stages) - 1
toContinue = ""

chosenWord = random.choice(word_list.word_list)
wordLenght = len(chosenWord)

display = []
for _ in range(wordLenght):
    display += "_"

while isOn:
    guess = input("Please, guess a letter: ").lower()
    os.system('clear')
    if guess in display:
        print(f"You already guessed {guess}")

    for position in range(wordLenght):
        letter = chosenWord[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosenWord:
        print("Letter not in the word.")
        lives -= 1

    if lives == 0:
        os.system('clear')
        print(f"The word was: {chosenWord}")
        toContinue = input("YOU LOSE. Would you like to try again? (Y / N) ").lower()
        if toContinue == "y":
            chosenWord = random.choice(word_list.word_list)
            wordLenght = len(chosenWord)
            lives = len(art.stages) - 1
            display = []
            for _ in range(wordLenght):
                display += "_"
        else:
            print("THANKS FOR PLAYING!")
            isOn = False
    elif not "_" in display:
        toContinue = input("YOU WIN. Would you like to go again? (Y / N) ")
        if toContinue == "y":
            chosenWord = random.choice(word_list.word_list)
            wordLenght = len(chosenWord)
            lives = len(art.stages) - 1
            display = []
            for _ in range(wordLenght):
                display += "_"
        else:
            print("THANKS FOR PLAYING!")
            isOn = False
    print(art.stages[lives])
