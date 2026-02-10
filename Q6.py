import pandas as pd
df = pd.read_csv("employees.csv")
first_5_rows = df.head(5)
info = df.info()
summary = df.describe()

print("\nFirst 5 rows:\n",first_5_rows)
print("\nInfo:\n",info)
print("\nSummary statistics:\n",summary)
