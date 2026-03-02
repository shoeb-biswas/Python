def Marking_System(df1):
    a = df1['Data Structure Marks'] * 3
    b = df1['Algorithm Marks'] * 2
    c = df1['Python Marks'] * 5
    return a+b+c


df1['Exceptional Marks'] = df1.apply(Marking_System,axis=1)
