# Import libraries
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Fit linear Regression
model= LinearRegression()
model.fit(hours,marks)
pred = model.predict(hours)
print(pred)


mae = mean_absolute_error(marks, pred)
mse = mean_squared_error(marks, pred)
rmse = np.sqrt(mse)
r2 = r2_score(marks, pred)

#print Result
print("MAE: ", mae)
print("MSE: ", mse)
print("RMSE: ", rmse)
print("R²: ", r2)

plt.scatter(hours, marks, label="Actual Data")

plt.plot(hours, pred,color="red", label="Predicted Line")

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Linear Regression vs SGDRegressor")
plt.legend()
plt.grid(True)
plt.show()
