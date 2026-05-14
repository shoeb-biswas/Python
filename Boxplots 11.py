# Boxplots to get a sense of spread and possible outliers
plt.figure(figsize=(12,8))
df[numeric_cols].boxplot()
plt.suptitle("Histograms of Numerical Feature", fontsize=14)
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12,8))
df.boxplot(column=numeric_cols[0])
plt.suptitle("Histograms of Numerical Feature", fontsize=14)
plt.xticks(rotation=45)
plt.show()

# Terget Distribution and class Imbalance
plt.figure(figsize=(5,4))
sns.countplot(x=df[target_col])
plt.title("heartDisease Class Distribution")
plt.xlabel("HeartDisease (0= No, 1= Yes)")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

