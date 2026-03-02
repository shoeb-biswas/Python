# Custom made Function

def grading_system(marks):
    if marks >= 260:
        return 'A+'
    elif marks >= 250:
        return 'A'
    else:
        return 'A-'

df1['Grade'] = df1['Total Marks'].apply(grading_system)
