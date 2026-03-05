sns.scatterplot(data = student, x= 'study_hours' ,y= 'test_score',hue = 'gender', style  = 'class_level')

sns.scatterplot(data = student, x= 'study_hours' ,y= 'test_score',hue = 'gender', style  = 'subject',size= 'Tshirt_size')

sns.scatterplot(data = student, x= 'study_hours' ,y= 'test_score',hue = 'gender', style  = 'subject')

sns.relplot(kind = 'scatter', data = student, x= 'study_hours' ,y= 'test_score',hue = 'gender', style  = 'subject',size= 'Tshirt_size')

