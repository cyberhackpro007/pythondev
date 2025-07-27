# if condition:
#     # code block to be executed if condition is True
# Explanation:
# if keyword: This initiates the conditional statement.
# condition: This is a Boolean expression that evaluates to either True or False. It can involve comparisons (e.g., x > 5), logical operators (e.g., a and b), or function calls that return a Boolean value.
# Colon (:): This marks the end of the if statement's header.
# Indented code block: The lines of code immediately following the if statement and indented at the same level constitute the "body" of the if statement. This block is executed only if the condition is True. If the condition is False, this block is skipped, and the program continues execution with the first statement after the if block (at the same indentation level as the if keyword).
# Example:
# Python
#
# age = 18
#
# if age >= 18:
#     print("You are eligible to vote.")
# print("This statement is always executed.")
# In this example, "You are eligible to vote." is printed because age >= 18 evaluates to True. "This statement is always executed." is printed regardless of the condition, as it is outside the if block's indentation.

age = int(input("Enter your age: "))

if age >= 100:
    print("You are tool old to sign up")
elif age >= 18:
    print("You are now signed up")
elif age <=0:
    print("You are not yet born")
else:
    print("You must be 18+ to sign up")


response = input("Do you have any question? (y/n): ")
if response == "y":
    print("We will answer")
else:
    print("We will not answer")

name = input("What is your name? ")

if name == "":
    print("You didn't enter a name")
else:
    print(f"Your name is {name}" )

#use of boolean

for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")

