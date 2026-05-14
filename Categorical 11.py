# Categorical Feature Exploration
for c in Categorical_cols:
  plt.figure(figsize=(5,4))
  df[c].value_counts().plot(kind="bar")
  plt.title(f"Value counts for {c}")
  plt.ylabel("count")
  plt.tight_layout()
  plt.show()

# Pairplot for a Subset of Features
sns.pairplot(df[["Age", "Cholesterol", "MaxHR", "Oldpeak", "HeartDisease"]], hue="HeartDisease", diag_kind = "hist")
plt.show()

