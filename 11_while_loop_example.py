# Python compound interest Calculator

principle = 0
rate = 0
time = 0

# while principle <= 0:
#     principle = float(input("Enter a principle: "))
#     if principle <= 0:
#         print("Please enter a number greater than zero")
#
# while rate <= 0:
#     rate = float(input("Enter a rate of interest: "))
#     if principle <= 0:
#         print("Please enter a number greater than zero")
#
# while time <= 0:
#     time = int(input("Enter a time in years: "))
#     if time <= 0:
#         print("Please enter a number greater than zero")
#
# total = principle * pow((1 + rate / 100), time)
#
# print(f"Total Amount after {time}/s: {total:.2f}")


while True:
    principle = float(input("Enter a principle: "))
    if principle <= 0:
        print("Please enter a number greater than zero")
    else:
        break

while True:
    rate = float(input("Enter a rate of interest: "))
    if principle <= 0:
        print("Please enter a number greater than zero")
    else:
        break

while True:
    time = int(input("Enter a time in years: "))
    if time <= 0:
        print("Please enter a number greater than zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)

print(f"Total Amount after {time}/s: {total:.2f}")