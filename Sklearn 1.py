from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Assume df_heart_encoded is our working dataframe with target 'HeartDisease'
target_col = "HeartDisease"
x = df_heart_encoded.drop(columns=[target_col])
y = df_heart_encoded[target_col]

x_train, x_test, y_train, y_test  = train_test_split(x,y, test_size = .25, random_state = 42)

# Standard Scaling
scaler_sd = StandardScaler()
x_train_std = scaler_sd.fit_transform(x_train) # mean and SD will be Calculated from x_train
x_test_std = scaler_sd.transform(x_test)

# MinMax scaling
scaler_mm = MinMaxScaler()
x_train_mm = scaler_mm.fit_transform(x_train)
x_test_mm = scaler_mm.fit_transform(x_test)

print("\n--- Displaying Standard Scaled Data ---")
# Convert scaled arrays back to Dataframe for batter visualization with column names
x_train_std_df = pd.DataFrame(x_train_std, columns = x_train.columns, index = x_train.index)
x_test_std_df = pd.DataFrame(x_test_std, columns = x_test.columns, index = x_test.index)
print("\nFirst 5 rows of x_train (Standard Scaled)")
display(x_train_std_df.head())
display(x_test_std_df.head())


x_train_mm_df = pd.DataFrame(x_train_mm, columns = x_train.columns, index = x_train.index)
x_test_mm_df = pd.DataFrame(x_test_mm, columns = x_test.columns, index = x_test.index)

print("\nFirst 5 rows of x_train (Minmax Scaled)")
display(x_train_mm_df.head())
display(x_test_mm_df.head())
