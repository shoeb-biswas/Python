status = df1.groupby('CompletionStatus').size()
plt.pie(status, labels= status.index,autopct='%1.1f%%', explode=(0.09,0,0),shadow= True)
plt.show()
status
