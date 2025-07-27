# while loop = execute come code WHILE some condition remains true


# name = input("Enter your name: ")
#
# while name == "":
#     print("Your name is empty")
#     name = input("Enter your name: ")
#     print(f"Your name is {name}")

# age = int(input("Enter Your Age: "))
#
# while age < 0:
#     print("Sorry, you are not allowed to go below zero.")
#     age = int(input("Enter Your Age: "))
#     print(f"Your Age is {age} years old")

food = input("Enter a food you like (q to quit): ")
while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you like (q to quit): ")

print("Thank you")
