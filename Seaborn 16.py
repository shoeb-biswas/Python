fig = px.scatter(student1, x = 'time_study', y= 'Marks', color='gender')
fig.show()

fig = px.scatter(student1, x = 'time_study', y= 'Marks', color='gender', size= 'Tshirt_size')
fig.show()

fig = px.scatter(student1, x = 'time_study', y= 'Marks', color='gender', size= 'Tshirt_size', hover_data = 'hostel')
fig.show()

