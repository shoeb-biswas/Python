students = pd.read_csv('student_IQdata.csv')
plt.xlabel('Study Hour')
plt.ylabel('IQ Score')
plt.title('Relation between study hours and IQ Score')

plt.scatter(students['Study_Hour'],students['IQ_Score'])
