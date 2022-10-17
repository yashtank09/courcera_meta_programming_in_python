"""
    Instance method
"""


class Payslip:
    # __init__ method for taking employee details as an argument
    def __init__(self, name, payment, amount):
        self.name = name
        self.payment = payment
        self.amount = amount

    # pay() method for pay to employee also this is an instance method
    def pay(self):
        self.payment = "yes"

    # this method will give status of employee payment is done or not
    def status(self):
        if self.payment == "yes":
            return self.name + " is paid " + str(self.amount)
        else:
            return self.name + " is not paid yes."


# creating two employee name 'Nathan' and 'Rogger'.
nathan = Payslip("Nathan", "no", 3500)
rogger = Payslip("Rogger", "no", 3000)

print(nathan.status())
print(rogger.status())

# now we are paying to rogger
rogger.pay()
print("\nAfter Payment")
print(nathan.status())
print(rogger.status())

