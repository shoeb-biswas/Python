import numpy as np
import pandas as pd

np.random.seed(42)

ids = np.arange(1, 11)
ages = np.random.randint(18, 60, 10)
salaries = np.random.randint(30000, 90000, 10)
departments = np.array(["HR", "IT", "Finance", "IT", "HR", "Sales", "Finance", "IT", "Sales", "HR"])

DF = pd.DataFrame({
"id": ids,
"age": ages,
"salary": salaries,
"dept": departments
})

DF.to_csv("employees.csv", index=False)
print("Sample Data Created and Saved as employees.csv")
