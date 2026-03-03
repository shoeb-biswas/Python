status = df1.groupby('Location').size()
plt.pie(status, labels= status.index,autopct='%1.1f%%')
plt.show()
status
