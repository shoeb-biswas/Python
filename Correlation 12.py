# Correlation matrix and Heatmap
corr_matrix = df[numeric_cols + [target_col]].corr()
plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot = True, cmap = "coolwarm", fmt=".2f", linewidths =0.5)
plt.title("Correlation Heatmap for Numerical Features")
plt.tight_layout()
plt.show()

corr_matrix[target_col].sort_values(ascending=False)
