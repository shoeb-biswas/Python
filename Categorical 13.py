# Categorical Features vs Target
for c in Categorical_cols:
  ct = pd.crosstab(df[c], df[target_col], normalize="index")
  print(f"\nProportion of HeartDisease within {c}")
  display(ct)
  ct.plot(kind="bar", stacked=True, figsize=(6,4))
  plt.title(f"HeartDisease proportion by {c}")
  plt.ylabel("proportion")
  plt.xticks (rotation=0)
  plt.tight_layout()
  plt.show()
