df1['EnrollmentDate'] = pd.to_datetime(df1['EnrollmentDate'])
df1['EnrollmentDate']
df1['EnrollmentDate'] = df1['EnrollmentDate'].dt.year
df1['EnrollmentDate']
df1['EnrollmentDate'] = pd.to_datetime(df1['EnrollmentDate'])
df1['Enrollment Date'] = df1['EnrollmentDate'].dt.day
df1['EnrollmentDate'] = pd.to_datetime(df1['EnrollmentDate'])
