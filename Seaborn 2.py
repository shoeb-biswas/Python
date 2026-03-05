sns.lineplot(data= student, x='week',y='attendance_rate',errorbar=None,hue = 'gender')

sns.relplot(kind = 'line',data= student, x='week',y='attendance_rate',errorbar=None,hue = 'gender')

sns.relplot(kind = 'line',data= student, x='week',y='test_score',errorbar=None,hue = 'gender')

sns.relplot(kind = 'line',data= student, x='week',y='test_score',errorbar=None,hue = 'class_level')

sns.relplot(kind = 'line',data= student, x='week',y='attendance_rate',errorbar=None,hue = 'class_level')

