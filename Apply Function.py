mn = df1['Total Marks'].min()
mx = df1['Total Marks'].max()
df1['Scaled Marks'] = df1['Total Marks'].apply(lambda x: (x-mn)/(mx-mn))
