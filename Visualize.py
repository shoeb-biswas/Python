# View the Learned Parameters
print("m: ", model.coef_[0])
print("c: ", model.intercept_)
# marks = 4.3xhours + 44.8

# Visualize the best fit line
plt.scatter(hours, marks, color='blue', label="Actual Data")
predicted_marks = model.predict(hours)
plt.plot(hours, predicted_marks, color='red', label="Best Fit Line")

plt.xlabel("Study hours")
plt.ylabel("Marks")

plt.title("Study Hours vs Marks for Linear Regression")
plt.legend()
plt.grid(True)
plt.show()
