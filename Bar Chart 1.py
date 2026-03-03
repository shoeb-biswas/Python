data = {
    'Student': ['B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
    'StudyHours': [ 2, 5, 3, 7, 4, 8, 1],
    'Attendance': [ 60, 88, 70, 95, 80, 98, 55],
    'Grade': [ 'Fail', 'Pass', 'Fail', 'Pass', 'Pass', 'Pass', 'Fail']
}

df = pd.DataFrame(data)

# Gender wise catagorise
Gender_group = df.groupby('Gender').size()
Gender_group.index
Gender_group.values
