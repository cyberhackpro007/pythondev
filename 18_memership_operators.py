# Membershio operators = used to test whether a value or vaiable is found in a sequence
#                       (string, list, tuple, set, or dictionary)
#                       1. in
#                       2. not in


word = "APPLE"

while True:
    letter = input("Guess a letter in secrete word: ")
    if letter in word:
        print(f"{letter} is in the word.")
    else:
        print(f"{letter} is not in the word.")
    print()


print("Thank you for playing!")
