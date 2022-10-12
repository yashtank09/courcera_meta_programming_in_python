"""
    Python Functions is a block of statements that return the specific task.

    Syntax: Python Function

        def function_name (parameters):
            # statement
            return expression
    More about functions: https://www.geeksforgeeks.org/python-functions/
"""


# Creating a function
def fun():
    print("Welcome to Functions")


fun()


# Creating a function that will take input parameter and produce the output string
def foo(name):
    print("Hello! " + name + ". How can I help you?")


foo("Yash")
foo("Aastik")

# Calculating tax slabs using  normal procedure
bill = 175.00

tax_rate = 15

total_Tax = (bill * tax_rate) / 100.00

print('Total tax', total_Tax)


# We can not calculate this for bulk of bills, we move forward to the function where we can calculate the same way using functions

# Creating a function for calculating tax slabs
def calculate_tax(customer_bill, Tax_slab):
    # round function will give float point number from the decimal value to the closest multiple of 10.
    return round((customer_bill * Tax_slab) / 100.00, 2)


# printing tax slab for first customer
print('Total tax is: ', calculate_tax(165, 12.5))
# printing tax slab for second customer
print('Total tax is: ', calculate_tax(5000, 20.01))
