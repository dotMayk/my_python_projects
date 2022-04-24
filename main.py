import art
import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']


def encode(w, s):
    endText = ""
    for char in w:
        if char in alphabet:
            position = alphabet.index(char)
            newPosition = position + s
            endText += alphabet[newPosition]
        else:
            endText += char
    os.system('clear')
    print(art.logo)
    print(f"Here is the ENCRYPTED word: {endText}")


def decode(w, s):
    endText = ""
    for char in w:
        if char in alphabet:
            position = alphabet.index(char)
            newPosition = position - s
            endText += alphabet[newPosition]
        else:
            endText += char
    os.system('clear')
    print(art.logo)
    print(f"Here is the DECRYPTED word: {endText}")


isOn = True
word = ""
shift = 0
restart = ""

while isOn:
    os.system('clear')
    print(art.logo)
    print("Type 'encode' to encrypt.")
    print("Type 'decode' to decrypt.")
    print("Type 'exit' to to finish the program.")
    choice = input(">>> ").lower()
    if choice == "encode":
        os.system('clear')
        print(art.logo)
        print("Please, type the word to ENCODE")
        word = input(">>> ").lower()
        print("Please, type the SHIFT number")
        shift = int(input(">>> "))
        encode(word, shift)
        print("Would you like to restart the program? (Y / N)")
        restart = input(">>> ").lower()
        if restart == "y":
            isOn = True
        else:
            os.system('clear')
            print(art.logo)
            print("Thanks for using me!")
            isOn = False
    elif choice == "decode":
        os.system('clear')
        print(art.logo)
        print("Please, type the word to DECODE")
        word = input(">>> ").lower()
        print("Please, type the SHIFT number")
        shift = int(input(">>> "))
        decode(word, shift)
        print("Would you like to restart the program? (Y / N)")
        restart = input(">>> ").lower()
        if restart == "y":
            isOn = True
        else:
            os.system('clear')
            print(art.logo)
            print("Thanks for using me!")
            isOn = False
    elif choice == "exit":
        os.system('clear')
        print(art.logo)
        print("Thanks for using me!")
        isOn = False
