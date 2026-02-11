# Making first name column
df['First Name'] = df['FullName'].str.split(' ').str[0]
df
