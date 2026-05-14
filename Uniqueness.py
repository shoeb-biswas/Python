df_titanic.shape
print("Unique values per column:")
df_titanic.nunique()

print("Missing values per column: ")
df_titanic.isnull().sum()
