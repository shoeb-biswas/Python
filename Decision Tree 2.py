np.random.seed(42)
n_samples = 300

age = np.random.randint(30, 80, size = n_samples)
chol = np.random.randint(150, 300, size = n_samples)
thalach = np.random.randint(90, 200, size = n_samples)

# We create a simple rule-based probability for disease. just for realism
risk_score = 0.03 * (age - 40) + 0.02 * (chol - 200) -0.02 * (thalach - 140)
prob = 1/(1+np.exp(-0.05 * risk_score))

target = (prob>np.median(prob)).astype(int)

df_heart = pd.DataFrame({
    'age': age,
    'chol': chol,
    'thalach': thalach,
    'target': target
})
df_heart.head()

# Train-test split and model training
x_heart = df_heart[['age','chol','thalach']]
y_heart = df_heart[['target']]

x_train_h, x_test_h, y_train_h, y_test_h = train_test_split(
    x_heart, y_heart, test_size=0.2, random_state=42
)

tree_heart = DecisionTreeClassifier(max_depth=4, random_state=42)
tree_heart.fit(x_train_h, y_train_h)

# Confusion metrix
y_pred_h = tree_heart.predict(x_test_h)

cm = confusion_matrix(y_test_h, y_pred_h)
print(cm)

# Plot of confusion matrix
fig, ax = plt.subplots()
im = ax.imshow(cm, interpolation= 'nearest')
ax.set_title("Confusion Matrix")
ax.set_xlabel("Predicted label")
ax.set_ylabel("True label")

# Show all tricks and label them
ax.set_xticks([0,1])
ax.set_yticks([0,1])
ax.set_xticklabels(["No disease", 'Disease'])
ax.set_yticklabels(["No disease", 'Disease'])

# Loop over data dimensions and create text annotations.
for i in range(cm.shape[0]):
  for j in range(cm.shape[1]):
    ax.text(j,i,cm[i,j], ha= 'center', va='center')

plt.colorbar(im)
plt.show()

# Accuracy, precision, recall, F1
acc = accuracy_score(y_test_h, y_pred_h)
prec = precision_score(y_test_h, y_pred_h)
rec = recall_score(y_test_h, y_pred_h)
f1 = f1_score(y_test_h, y_pred_h)

print('Accuracy :', round(acc, 3))
print('Precision :', round(prec, 3))
print('Accuracy :', round(rec, 3))
print('Accuracy :', round(f1, 3))
