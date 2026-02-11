# Unique with Null
len(df1['Data Structure Marks'].unique())
# Unique with Null
df1['Data Structure Marks'].nunique()

# *** Unique Works only on series ***
df1.isnull()
df1['Data Structure Marks'].notnull()
df1['Data Structure Marks'].hasnans
df1['StudentID'].hasnans
