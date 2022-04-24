import random


def password_randomizer(list):
    randomPasswordList = []
    for i in range(len(list)):
        word = random.choice(list)
        randomPasswordList.append(word)
        list.remove(word)
    randomPassword = ''.join(randomPasswordList)
    return randomPassword


lettersList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbersList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbolsList = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("= = = WELCOME TO THE PASSWORD GENERATOR = = =")
lettersInput = int(input("How many letters would you like your password? "))
numbersInput = int(input("How many numbers would you like in your password? "))
specialInput = int(input("How many special characters would you like in your password? "))

passwordList = []

for i in range(lettersInput):
    passwordList.append(random.choice(lettersList))
for i in range(numbersInput):
    passwordList.append(random.choice(numbersList))
for i in range(specialInput):
    passwordList.append(random.choice(symbolsList))

print(passwordList)

password = password_randomizer(passwordList)
print(f"Your password is: {password}")

