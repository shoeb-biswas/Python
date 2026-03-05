tips_data = sns.load_dataset("tips")
tips_data

sns.relplot(kind = 'scatter',data = tips_data, x = 'total_bill', y = 'tip')
sns.relplot(kind = 'scatter',data = tips_data, x = 'total_bill', y = 'tip', hue = 'sex', style = 'time', size = 'size')
student1 = pd.read_csv('Student_dataset_complete.csv')
student1.head()
