print("Missing values per column: ")
df_titanic.isnull().sum()

from sklearn.preprocessing import LabelEncoder

# Load Heart Dataset
heart_path = "/heart.csv"
df_heart = pd.read_csv(heart_path)

print("First 10 row of heart dataset: ")
display(df_heart.head(10))

print("\nColumn data types:")
display(df_heart.dtypes)
