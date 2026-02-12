# Basis of any column Delete Duplcaion
# Parmanently Deleting dublicate value
df.drop_duplicates(subset=['Department'])
df.drop_duplicates(subset=['Department'],keep='last')
