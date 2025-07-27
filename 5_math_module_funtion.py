# math Module Functions:
# The math module provides more advanced mathematical operations and constants. It must be imported before use.
# Constants:
#    math.pi: Represents the mathematical constant Pi (approximately 3.14159).
#   math.e: Represents Euler's number (approximately 2.71828).
# Basic Arithmetic & Power:
#   math.sqrt(x): Returns the square root of x.
#   math.pow(x, y): Returns x raised to the power of y (returns a float).
#   math.factorial(x): Returns the factorial of x.
# Trigonometric Functions (angles in radians):
#   math.sin(x): Returns the sine of x.
#   math.cos(x): Returns the cosine of x.
#   math.tan(x): Returns the tangent of x.
#   math.degrees(x): Converts angle x from radians to degrees.
#   math.radians(x): Converts angle x from degrees to radians.
# Logarithmic Functions:
#   math.log(x, base): Returns the logarithm of x with the specified base (default is natural logarithm).
#   math.log10(x): Returns the base-10 logarithm of x.
#   math.exp(x): Returns e raised to the power of x.
# Rounding and Absolute Value:
#   math.ceil(x): Returns the smallest integer greater than or equal to x.
#   math.floor(x): Returns the largest integer less than or equal to x.
#   math.fabs(x): Returns the absolute value of x (returns a float).

# import math
#
# # Calculate square root
# s = math.sqrt(16)
# print(f"Square root of 16: {s}")
#
# # Calculate sine of 45 degrees
# angle_degrees = 45
# angle_radians = math.radians(angle_degrees)
# sine_value = math.sin(angle_radians)
# print(f"Sine of {angle_degrees} degrees: {sine_value}")
#
# # Get the value of Pi
# print(f"Value of Pi: {math.pi}")


import math
#
# # print(math.pi)
# # print(math.e)
#
# x = 9
#
# result = math.sqrt(x)
#
#
# print(result)

#circumference of circle

radius = float(input("Enter radius of circle: "))

circumference = 2 * math.pi * radius
print(f"Circumference of circle: {round(circumference, 2)}cm")

# area of circle

radius = float(input("Enter radius of circle: "))

area = math.pi * radius ** 2
print(f"Area of circle: {round(area, 2)}cm")

