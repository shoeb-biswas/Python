print("Distribution of Embarked Column:")

plt.figure(figsize=(8,6))
sns.countplot(data = df_titanic, x= "Embarked")
plt.title("Embarked Distribution of Titanic Passenger")
plt.xlabel("Embarked")
plt.ylabel("Frequency")
plt.show()
