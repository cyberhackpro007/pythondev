# *args     = allow you to pass multiple non-key arguments
# *kwargs   = allow you to pass multiple keywords-arguments
#               *unpacking operator
#   1. positional  2.default 3.keywords  4.arbitrary

# args packed into tuple
# kwargs packed into dictionary

def add(a, b):
    return a + b

print(add(1, 2))

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 100, 33, 44, 55.44))

# parameter name can be any, args is just a standard, you can replace with num
def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(1, 2, 100, 33, 55.44))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Cyber", "Pro", "The", "Other" "ITGUY")
print()


def print_address(**kwargs):
    for value in kwargs.values():
        print(value)

print_address(street="123 Fake St.", city="Plano", state="Tx", Zip= "75024")
print()

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St.", apt="100", city="Plano", state="Tx", Zip= "75024")





