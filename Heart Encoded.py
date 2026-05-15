df_heart_encoded["Age_bin"] = pd.cut(
    df_heart_encoded["Age"],
    bins=[0,30,50,70,100],
    labels=["Young","Middle","Middle-Old", "Old"]
)
print(df_heart_encoded[["Age", "Age_bin"]].head(50))
