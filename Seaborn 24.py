sns.jointplot(data = student1, x= 'study_hours', y = 'Marks')
sns.jointplot(kind = 'kde' ,data = student1, x= 'study_hours', y = 'Marks')
sns.jointplot(data = student1, x= 'study_hours', y = 'Marks', hue = 'gender')
