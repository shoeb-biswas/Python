# Check missing values count per column
df.isna().sum()

# Look at some basic value ranges
df[numeric_cols].agg(["min", "max", "mean", "median"]).T

for c in Categorical_cols:
  print(c, df[c].unique())
