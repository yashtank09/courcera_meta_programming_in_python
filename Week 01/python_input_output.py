# Taking user input
A = input()
print(A)

# Using input indentation
str1 = input('Enter your first name: ')
str2 = input('Enter your last name: ')

print("Hello ", str1, str2)

# print variable using .formatting method
print("Hello, How are you {0} {1}".format(str1, str2))

# print using concatenating using `+` operator
print("Hello " + str1 + " " + str2 + ", How are you!")

# Arithmatic operations using inputs
numb1 = input('Enter first number: ')
numb2 = input('Enter second number: ')

# input only take string values
print(numb2)
print(numb2)

# it will concatenate the user input
print(numb1 + numb2)

# arithmatic operations by typecast the input
print(float(numb1) * float(numb2))
print(int(numb1) - int(numb2))

# printing it in better format
SumNum = int(numb1) + int(numb2)
print("The sum of: " + numb1 + " and " + numb2 + " is " + str(SumNum) + ".")
