# Demonstrating python conditional statements of if, else and elif

# `if` using light and switch example

# Light is currently off
current = False

if current:
    current = False
    print("Turning light off")

if not current:
    current = True
    print("Turning light on")

# output: Turning light on

# if else
current2 = False

if current2:
    current2 = False
    print("Turning light off")
else:
    current2 = True
    print("Turning light on")

# elif using loyalty customer program
loyalty_customer = True
total_bill = 124

if loyalty_customer and total_bill > 100:
    # give 20% discount
    total_bill = total_bill - (float(total_bill)/100) * 20
elif total_bill > 100:
    # give 10% discount
    total_bill = total_bill - (float(total_bill) / 100) * 10
else:
    # sorry no discount, 5% service charge
    print("Sorry, no discount...")

print('Total Bill: ', float(total_bill))
