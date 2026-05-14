# Histograms for numeric features
df["Age"].hist(bins=20, figsize=(8,4))
plt.suptitle("Histograms of Numerical Feature Age", fontsize=14)
plt.tight_layout()
plt.show()

df["Cholesterol"].hist(bins=20, figsize=(8,4))
plt.suptitle("Histograms of Numerical Feature Cholesterol", fontsize=14)
plt.tight_layout()
plt.show()

df[numeric_cols].hist(bins=20, figsize=(12,8))
plt.suptitle("Histograms of Numerical Feature", fontsize=14)
plt.tight_layout()
plt.show()
