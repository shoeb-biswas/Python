# Train-test split using original df_heart (not already encoded)

X = df_heart.drop(columns=[target_col])
y = df_heart[target_col]

x_train_pipe, x_test_pipe, y_train_pipe, y_test_pipe = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Fit the full pipeline
clf.fit(x_train_pipe, y_train_pipe)

# Predict and evaluate
from sklearn.metrics import accuracy_score

y_pred_pipe = clf.predict(x_test_pipe)

acc = accuracy_score(y_test_pipe, y_pred_pipe)

print("Logistic Regression with preprocessing pipeline:", acc)
