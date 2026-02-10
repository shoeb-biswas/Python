import pandas as pd
last_3_rows = df.tail(3)

print(df.loc[:,["id","age","salary"]])
print("Last 3 rows:\n",last_3_rows)
