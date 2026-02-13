not_started = df.loc[df['CompletionStatus'] == 'In Progress']
not_started
Completed = df.loc[df['CompletionStatus'] == 'Completed']
Completed
# Completed and DS maks greater then 90
Completed_ds90 = df.loc[(df['CompletionStatus'] == 'Completed') & (df['Data Structure Marks'] > 90)]
Completed_ds90 
