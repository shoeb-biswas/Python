df1.fillna(0)
df1['FullName'].fillna('Unknown')
df1['Python Marks'] = df1['Python Marks'].fillna(df1['Python Marks'].mean())
