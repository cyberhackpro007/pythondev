#Varible = A container for a value (string, integer, float, boolean)
#          A variable behaves as if it was the value it contains
from xml.dom.minidom import ProcessingInstruction

first_name=("Cyber")

food = ("pizza")

print(first_name)


print(f"Hello {first_name}")

print(f"I like {food}")

name = "CyberPro"
age = 30
message = f"My name is {name} and I am {age} years old."
print(message)
# Output: My name is Alice and I am 30 years old.

# Embedding an expression
result = f"The sum of 5 and 7 is {5 + 7}."
print(result)
# Output: The sum of 5 and 7 is 12.

#String : String is character, which includes letter, numbers and symbols
fist_name = "Cyber"
food = ("pizza")
email = "cryberpro@gmail.com"

#Intergers is whole number
age = 45
quantity = 3

print(age)
print(f"You are {age} years old.")
print(f"You are buying {quantity} dollars.")

#Float a Float is number but contain decimal portion

price = 10.99
gpa = 3.2

print(f"The price is ${price} dollars.")
print(f"Your gpa is {gpa}")

#Boolean - Boolean is either True or False

is_student = False

print(f"Are you a student ? {is_student}")

if is_student:
    print("You are a student")
else:
    print("Are you NOT a student")

