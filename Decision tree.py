import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import(
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_curve,
    auc,
)
# Make plots a bit large by default
plt.rcParams['figure.figsize'] = (7,5)

# Create a small synthetic dataset
data = {
    'weather': ['Sunny', 'Rainy', 'Sunny','Sunny', 'Rainy','Rainy', 'Sunny','Rainy'],
    'windy': [0,1,0,1,0,1,0,1],
    'play': [1,0,1,1,0,0,1,0]
}
df_synthetic = pd.DataFrame(data)
df_synthetic

# Encode categorical feature and prepare x,y
df_synthetic['weather_num'] = df_synthetic['weather'].map({'Sunny':1, 'Rainy':0})
x_syn = df_synthetic[['weather_num', 'windy']]
y_syn = df_synthetic['play']
print(x_syn)
print(y_syn)

# Train a simple decision tree
tree_syn = DecisionTreeClassifier(max_depth=3, random_state=42)
tree_syn.fit(x_syn, y_syn)
tree_syn

# Visualize the tree
plt.figure(figsize=(8,6))
plot_tree(
    tree_syn,
    feature_names = ['weather_num', 'windy'],
    class_names = ['No', 'Yes'],
    filled = True,
    rounded = True,
)
plt.title("Decision Tree-Synthetic Play Exercise")
plt.show()


# Example: Sunny (1), not windy (0)
example_1 = pd.DataFrame([[1, 0]], columns=['weather_num', 'windy'])
pred_1 = tree_syn.predict(example_1)[0]
print('Sunny, not windy -> play prediction:', pred_1)

# Example: Rainy (0), windy (1)
example_2 = pd.DataFrame([[0, 1]], columns=['weather_num', 'windy'])
pred_2 = tree_syn.predict(example_2)[0]
print('Rainy, windy -> play prediction:', pred_2)
