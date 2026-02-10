import pandas as pd
IT_employees = df.loc[df["dept"] == "IT"]

print("Result:\n",IT_employees)
print("\nTotal number of IT employees:",len(IT_employees))
