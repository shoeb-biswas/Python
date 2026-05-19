# Create a slightly larger synthetic dataset
from sklearn.datasets import make_classification

x_big, y_big = make_classification(
  n_samples = 400,
  n_features = 5,
  n_informative = 3,
  n_redundant = 0,
  n_classes=2,
  random_state=42,
  )

x_train_big, x_test_big, y_train_big, y_test_big = train_test_split(
    x_big, y_big, test_size = 0.3, random_state=42
)
x_train_big.shape, x_test_big.shape

deep_tree = DecisionTreeClassifier(random_state=42)
deep_tree.fit(x_train_big, y_train_big)

pruned_tree = DecisionTreeClassifier(max_depth=3, random_state=42)
pruned_tree.fit(x_train_big, y_train_big)

y_train_pred_deep = deep_tree.predict(x_train_big)
y_test_pred_deep = deep_tree.predict(x_test_big)

y_train_pred_pruned = pruned_tree.predict(x_train_big)
y_test_pred_pruned = pruned_tree.predict(x_test_big)

print('Deep tree - train accuracy:', round(accuracy_score(y_train_big, y_train_pred_deep),3))
print('Deep tree - train accuracy:', round(accuracy_score(y_test_big, y_test_pred_deep),3))
print()
print('Pruned tree - train accuracy:', round(accuracy_score(y_train_big, y_train_pred_pruned),3))
print('Pruned tree - train accuracy:', round(accuracy_score(y_test_big, y_test_pred_pruned),3))


# Plot deep tree (Full)
plt.figure(figsize=(10,6))
plot_tree(deep_tree, filled=True, rounded= True)
plt.title("Deep tree (top 3 levels)")
plt.show()

# Plot deep tree (showing only top levels for readability)
plt.figure(figsize=(10,6))
plot_tree(deep_tree, filled=True, rounded= True, max_depth=3)
plt.title("Deep tree (top 3 levels)")
plt.show()

# Plot pruned tree (showing only top levels for readability)
plt.figure(figsize=(10,6))
plot_tree(pruned_tree, filled=True, rounded= True, max_depth=3)
plt.title("Deep tree (top 3 levels)")
plt.show()
