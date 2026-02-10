import pandas as pd
df.loc[df['salary']>80000,'salary'] = 80000
avg_sal = df['salary'].mean()
print("Average salary of all employees after replacement:",avg_sal)
