# input() = A function that prompts the user to enter data
#           Returns the entered data as string

#variable_name = input("Optional prompt message:")

name = input("Enter your name: ")
print("Hello, " + name)

age_str = input("Enter your age: ")
# To use age as a number, it needs to be type-casted
age_int = int(age_str)
print(f"You are {age_int} years old.")

####################

name = input("What is your name?")
age = input("How Old are you?:")

age = int(age) + 1


print(f"hello {name}")
print("HAPPY BIRTHDAY")
print(f"You are {age} years old.")

#or
# age = int(input("How Old are you?:"))
# age = age + 1
# print(f"You are {age} years old")

