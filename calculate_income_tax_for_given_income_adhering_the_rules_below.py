# Calculate income tax for the given income by adhering to the rules below
# Execise 12

# Creating pseudocode

# Creating a code to present the taxable income
taxable_income = int(input("Please enter the taxable income: "))

# Create a code that will assess if the income is taxable

# Create a code that will assess if the income is less than 10000
if taxable_income < 10000:
    tax = 0
    
# Create a code else if income is less than 20000
elif taxable_income < 20000:
    tax = (taxable_income - 10000) * 0.1

# Code else
else:
    tax = 10000 * 0 + 10000 * 0.1 + (taxable_income - 20000) * 0.2


