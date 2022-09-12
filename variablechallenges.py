#variable challenge
firstname = input("What is ur first name? ")
# ask a user to enter their first name and store it in a variable
lastname = input("What is ur last name? ")
# ask a user to enter their last name and store it in a variable
print(firstname + lastname)
# print their full name
print(firstname + " " + lastname)
# Make sure you have a space between first and last name
print(firstname.capitalize() + " " + lastname.capitalize())
# Make sure the first letter of first name and last name is uppercase
# Make sure the rest of the name is lowercase
num1 = int(input("Enter a number: "))
# Ask a user to enter a number
num2 = int(input("Enter a second nunmber: "))
# Ask a user to enter a second number
result = num1 + num2
# Calculate the total of the two numbers added together
print(str(num1) + " + " + str(num2) + " = " + str(result))
# Print 'first number + second number = answer'
# For example if someone enters 4 and 6 the output should read
# 4 + 6 = 10
result = num1 - num2
print(str(num1) + " - " + str(num2) + " = " + str(result))
result = num1 * num2
print(str(num1) + " * " + str(num2) + " = " + str(result))
result = num1 / num2
print(str(num1) + " / " + str(num2) + " = " + str(result))
# Continue these steps for subtraction, multiplication, and division