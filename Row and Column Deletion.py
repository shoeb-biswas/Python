df.rename(columns = { 'FullName' : 'Full Name', 'Algorithm Marks' : 'Algo Marks'},inplace=True)
df
# Row Deletion
df.drop(0,inplace=True)
df
# Column Deletion
df.drop('Instructor', axis=1, inplace= True)
df
