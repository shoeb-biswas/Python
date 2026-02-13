copy = df.sort_values('Data Structure Marks')
copy
df.sort_values('Data Structure Marks', inplace=True)
df
copy = df.sort_values('Data Structure Marks',ascending=False)
copy
copy = df.sort_values(['Data Structure Marks','Algorithm Marks'],ascending=False)
copy
