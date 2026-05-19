# Import libraries
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.metrics import mean_squared_error

# Creat the examle dataset
hours = np.array([2, 4, 6, 8, 10]).reshape(-1, 1)
marks = np.array([55, 60, 70, 80, 88])
hours, marks

lin_reg = LinearRegression()
lin_reg.fit(hours, marks)
print("m: ", lin_reg.coef_[0])
print("c: ", lin_reg.intercept_)

# Use a Grediant-Des
sgd_reg = SGDRegressor(
    max_iter = 1000,
    learning_rate = "invscaling",
    eta0=0.01,
    random_state=42
)
sgd_reg.fit(hours, marks)
print("m: ",sgd_reg.coef_[0])
print("c: ", sgd_reg.intercept_[0])

pred_sgd = sgd_reg.predict(hours)
mse_sgd = mean_squared_error(marks,pred_sgd)

print("MSE of SGDRegressor: ", mse_sgd)

# Compare Both Lines Visually
plt.scatter(hours, marks, label="Actual Data")

plt.plot(hours, predicted_marks, label="LinearRegression", linestyle="--")
plt.plot(hours, pred_sgd, label="LSGDRegression", linestyle="-.")

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Linear Regression vs SGDRegressor")
plt.legend()
plt.grid(True)
plt.show()
