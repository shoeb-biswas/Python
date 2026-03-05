enrollment = pd.read_csv('enrollment_data.csv')
fig = px.line(enrollment, x= 'Year', y='Programming')
fig.show()

fig = px.line(enrollment, x= 'Year', y='Digital Marketing')
fig.show()
fig = px.line(enrollment, x= 'Year', y='Digital Marketing', markers = True)
fig.show()
fig.write_html('digital_marketing_data.html')
