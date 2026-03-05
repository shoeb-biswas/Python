sns.regplot(data = student1, x= 'study_hours', y = 'test_score')
#Figure Level
sns.lmplot(data = student1, x= 'study_hours', y = 'test_score')
sns.lmplot(data = student1, x= 'study_hours', y = 'test_score', hue = 'gender')
