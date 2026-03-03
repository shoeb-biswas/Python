hours1 = [2,3,4,1,5,7,3]
hours2 = [1,5,6,3,9,8,6]
days = [1,2,3,4,5,6,7]

plt.xlabel('Days')
plt.ylabel('Hours')
plt.title('Trend of a student study time over a week')

plt.plot(days, hours1)
plt.plot(days, hours2)
