# Collection = single "Variable" used to store multiple values
# List    = [] ordered and changeable. Duplicates OK
# Set     = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple   = () ordered and unchangeable. Duplicates OK. Faster

fruits = ["apple", "banana", "cherry", "coconut"]

print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("pineapple" in fruits)

fruits[0] = "pineapple"
fruits.append("pineapple")
print(fruits)

fruits.remove("pineapple")
print(fruits)

fruits.clear()
print(fruits)

fruits.insert(0, "pineapple")
print(fruits)

fruits.sort()

fruits.reverse()
print(fruits)




print(fruits)
print(fruits[0])
print(fruits[::2])
print(fruits[::-1])

for x in fruits:
    print(x, end=" ")

