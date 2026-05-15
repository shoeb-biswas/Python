# Binning Age into categories (Young, Middle, Old)
df_heart_encoded["Age_bin"] = pd.cut(
    df_heart_encoded["Age"],
    bins=[0,30,50,100],
    labels=["Young","Middle","Old"]
)
print(df_heart_encoded[["Age", "Age_bin"]].head(50))
