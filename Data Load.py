import pandas as pd
titanic_path = "/Titanic-Dataset.csv"
df_titanic = pd.read_csv(titanic_path)

print("First 10 row of Titanic dataset")
df_titanic.head(10)
