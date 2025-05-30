#get user input
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
#calculate montly savings FIRST
monthly_savings = monthly_income - monthly_expenses
#Then calculate annual savings
annual_savings = (monthly_savings * 12) * 1.05
# Display results
print(f"Your monthly savings are ${monthly_savings:2f}.")
print(f"Projected savings after one year, with interest, is: ${annual_savings:.2f}.")
