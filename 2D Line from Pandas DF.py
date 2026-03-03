plt.xlabel('Years')
plt.ylabel('Enrollment')
plt.title('Student enrollment over 8 years')

plt.plot(df['Year'],df['Programming'])
plt.plot(df['Year'],df['Digital Marketing'])

plt.xlabel('Years')
plt.ylabel('Enrollment')
plt.title('Student enrollment over 8 years')

plt.plot(df['Year'],df['Programming'],label = 'Programming' )
plt.plot(df['Year'],df['Digital Marketing'],label = 'Digital Marketing')

plt.legend()

plt.xlabel('Years')
plt.ylabel('Enrollment')
plt.title('Student enrollment over 8 years')

plt.plot(df['Year'],df['Programming'],label = 'Programming', color = '#b042f5', linewidth = 5, linestyle='dashed',marker ='o',markersize=7)
plt.plot(df['Year'],df['Digital Marketing'],label = 'Digital Marketing',color = 'black', linewidth = 3,linestyle='dotted')

plt.legend(loc='lower right')
plt.grid()
plt.show()
