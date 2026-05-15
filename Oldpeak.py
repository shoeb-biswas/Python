col = "Oldpeak"

Q1 = df_heart_encoded[col].quantile(0.25)
Q3 = df_heart_encoded[col].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df_heart_encoded[
    (df_heart_encoded[col] < lower) | 
    (df_heart_encoded[col] > upper)
]

print(f"Number of Detected Outliers in {col}: {len(outliers)}")
