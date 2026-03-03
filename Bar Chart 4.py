status = df1.groupby('Location').size()

plt.bar(status.index, status.values,color= 'green' ,edgecolor = 'red' )

plt.xlabel('Location')
plt.ylabel('Count')
plt.title('Bar chart of Location')
