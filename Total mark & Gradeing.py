# Total Marks
df['Total Marks'] = df['Data Structure Marks'] + df['Algorithm Marks'] + df['Python Marks']
df
import numpy as np
df['A+ i DS'] = np.where(df['Data Structure Marks']>90, 'A+','A')
df
