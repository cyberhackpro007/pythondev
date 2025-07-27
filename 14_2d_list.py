
fruits =        ["apple", "banana", "orange", "strawberry"]
vegetables =    ["celery", "lime", "Onions", "beans"]
meats =         ["chicken", "fish", "turkey", "goat"]

groceries = [fruits, vegetables, meats]

print(groceries[2][1])

for collection in groceries:
    print(collection)


num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "3"))

for row in num_pad:
    for num in row:
        print(num, end="   ")
    print()


