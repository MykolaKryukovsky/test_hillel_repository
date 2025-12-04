import math


# squaring a number
print("SQUARING A NUMBER")
user_input = float(input("Please enter the number to recognize squares: "))
print(math.pow(user_input, 2))


# arithmetic mean of three numbers
print("ARITHMETIC MEAN OF THREE NUMBERS")
user_input1 = float(input("Please enter the first number out of three to find out the arithmetic mean: "))
user_input2 = float(input("Second number: "))
user_input3 = float(input("Third number: "))
average = (user_input1 + user_input2 + user_input3 ) / 3
print(f"Arithmetic average of entered numbers: {average:.2f}")


# convert Minutes to Hours ///////////////////////////////
print("CONVERT MINUTES TO HOURS")
m = float(input("Please enter the number of minutes you would like to convert: "))
minutes = int(m)
hours = minutes // 60
remaining_minutes = minutes % 60
print(f" {hours} hours and {remaining_minutes} minutes ")


# discount calculation
print("DISCOUNT CALCULATION")
price_product = float(input("Please enter the price of the product: "))
discount_percentage = float(input("Please enter the discount percentage % :"))
decimal_fraction = discount_percentage / 100
multiplier = 1 - decimal_fraction
discount = price_product * multiplier
print(f"Your price is reduced: {discount} ")


# stop digit number
print("STOP DIGIT NUMBER")
some_number = int(input("Please enter a some number: "))
last_digit = some_number % 10
print(f"Last digit is {last_digit}")


# perimeter of a rectangle
print("FINDING THE PERIMETER OF A RECTANGLE :" )
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
perimeter = 2 * (length + width)
print(f"The perimeter of the rectangle is {perimeter}")


# entering numbers into the column
print("ENTERING NUMBERS INTO THE COLUMN")
number_column = int(input("Please enter any four-digit number: "))

quotient, remainder = divmod(number_column, 1000)
print(f" {quotient}")

quotient_1, remainder_1 = divmod(remainder, 100)
print(f" {quotient_1}")

quotient_2, remainder_2 = divmod(remainder_1, 10)
print(f" {quotient_2}")
print(f" {remainder_2}")


