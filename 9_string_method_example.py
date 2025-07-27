# Validate user input exercide
#
# 1. username is not more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter your username: ")



if len(username) > 12:
    print("Your username is too long")
elif not username.find(" ") == -1:
    print("Your username must not contain space")
elif not username.isalpha():
    print("Your username must contain letters")
else:
    print(f"Your username is {username}")