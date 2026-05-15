numeric_cols = ["Age", "RestingBP", "Cholesterol", "MaxHR", "Oldpeak"]

plt.figure(figsize=(10, 6))

sns.boxplot(data=df_heart_encoded[numeric_cols])

plt.title("Boxplots for Selected Numeric Features")
plt.show()
