# budget_calculator.py - Personal Finance Calculator
# Starter code for e002-exercise-python-intro

"""
Personal Finance Calculator
---------------------------
This program helps users understand their monthly budget by collecting
income and expense information and displaying a formatted summary.

Complete the TODO sections below to finish the program.
"""

print("=" * 44)
print("       PERSONAL FINANCE CALCULATOR")
print("=" * 44)
print()

# =============================================================================
# TODO: Task 1 - Collect User Information
# =============================================================================
# Get the user's name
# Example: name = input("Enter your name: ")


# Get monthly income (as a float)
# Remember to convert the input to a float!


# Get expenses for at least 4 categories:
# - rent: Rent/Housing
# - utilities: Utilities (electric, water, internet)
# - food: Food/Groceries
# - transportation: Transportation (gas, public transit)


# =============================================================================
# TODO: Task 2 - Perform Calculations
# =============================================================================
# Calculate total expenses


# Calculate remaining balance (income - expenses)


# Calculate savings rate as a percentage
# Formula: (balance / income) * 100


# Determine financial status
# - If balance > 0: status = "in the green"
# - If balance < 0: status = "in the red"
# - If balance == 0: status = "breaking even"


# =============================================================================
# TODO: Task 3 - Display Results
# =============================================================================
# Create a formatted budget report
# Use f-strings for formatting
# Dollar amounts should show 2 decimal places: f"${amount:.2f}"
# Percentages should show 1 decimal place: f"{rate:.1f}%"

# Example structure:
# print("=" * 44)
# print("       MONTHLY BUDGET REPORT")
# print("=" * 44)
# print(f"Name: {name}")
# ... continue building the report ...


# =============================================================================
# TODO: Task 4 - Add Validation (Optional Enhancement)
# =============================================================================
# Add these validations before calculations:
# - If name is empty, use "Anonymous"
# - If income is <= 0, print error and exit
# - If any expense is negative, treat as 0


# =============================================================================
# STRETCH GOAL: Category Percentages
# =============================================================================
# Add a section showing what percentage each expense is of total income
# Example: print(f"  - Rent/Housing:    {(rent/income)*100:.1f}% of income")

def financialStatus(balance):

    # Compare the remaining balance in relation to 0 and return the status
    if balance > 0:
        status = "in the green"
    elif balance < 0: 
        status = "in the red"
    else:
        status = "breaking even"

    return status

def main():
    
    # Allows the user to input their information
    name = input("Enter your name: ")
    income = float(input("Enter your monthly income: "))
    rent = float(input("Enter your expenses for rent: "))
    utilities = float(input("Enter your expenses for utilities: "))
    food = float(input("Enter your expenses for food: "))
    transportation = float(input("Enter your expenses for transportation: "))

    # Calculate balance
    total_expenses = rent + utilities + food + transportation
    balance = income - total_expenses

    # Calculate savings rate (display with a % attached)
    savings_rate = (balance/income) * 100

    # Based on calculations, determine the financial status
    status = financialStatus(balance)

    # Display the results for the user based on their inputs
    print()
    print("=" * 44)
    print("       PERSONAL FINANCE CALCULATOR")
    print("=" * 44)
    print(f"Name: {name}")
    print(f"Monthly Income: ${income}")
    print()
    print("EXPENSES:")
    print(f"  - Rent / Housing:    ${rent:.2f}")
    print(f"  - Utilities:         ${utilities:.2f}")
    print(f"  - Food / Groceries:  ${food:.2f}")
    print(f"  - Transportation:    ${transportation:.2f}")
    print("-" * 22)
    print(f"Total Expenses:        ${total_expenses:.2f}")
    print(f"Remaining Balance:     ${balance:.2f}")
    print(f"Savings Rate:          {savings_rate:.1f}%")
    print()
    print(f"Status: You are {status}!")
    

if __name__ == "__main__":
    main()