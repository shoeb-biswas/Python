students_marks = student1[['Marks', 'study_hours', 'attendance_rate', 'gender']]
students_marks
sns.pairplot(data = students_marks)
sns.pairplot(data = students_marks, kind = 'hist')
sns.pairplot(data = students_marks, hue = 'gender')
