# Typecasting = The process of converting a variable from one data type to other
#               str(), int(), float(), bool()

num_int = 10
num_float = 5.5
result = num_int + num_float  # num_int is implicitly converted to float
print(result)
print(type(result))

# Explicit conversion examples
str_num = "123"
int_num = int(str_num)  # Convert string to integer
print(int_num)
print(type(int_num))

float_val = 7.89
int_val = int(float_val)  # Convert float to integer (truncates)
print(int_val)
print(type(int_val))

num = 42
str_val = str(num)  # Convert integer to string
print(str_val)
print(type(str_val))

##########################

name =  "Cyber Pro"
age = 45
gpa = 3.2
is_satisfied = False

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_satisfied))


gpa = int(gpa)
#print(gpa)
#print(type(gpa))

#name = int(name)
#print(name)
#print(type(name))

if is_satisfied:
    print(f"Your age is int{gpa}")
else:
    print(f"You are {age} years old")


age = str(age)
age += "1"

print(age)
print(type(age))

name = bool(name)
print(name)


