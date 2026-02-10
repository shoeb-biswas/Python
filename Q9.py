import pandas as pd
descending_order = df.sort_values("salary",ascending = False)
df2 = pd.DataFrame(descending_order)
highest_paid_employees = df2.head(3)
three_highest_paid_employees = highest_paid_employees.loc[:,["dept","age"]]

print("Salary in descending order:\n\n",descending_order)
print("\nTop 3 highest-paid employees\n\n",three_highest_paid_employees)
