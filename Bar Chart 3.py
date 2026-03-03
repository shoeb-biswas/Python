status = df1.groupby('CompletionStatus').size()

plt.bar(status.index, status.values, color= ['green','black','red'], edgecolor = 'yellow' )

plt.xlabel('CompletionStatus')
plt.ylabel('Count')
plt.title('Bar chart of Completion Status')
