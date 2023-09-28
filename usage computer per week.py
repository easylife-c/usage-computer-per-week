import matplotlib.pyplot as plt
days1=float(input("monday="))
days2=float(input("tuesday="))
days3=float(input("wednesday="))
days4=float(input("thursday="))
days5=float(input("friday="))
days6=float(input("saturday="))
days7=float(input("sunday="))
days = [1, 2, 3, 4, 5,6,7]
overall=('you use computer',days1+days2+days3+days4+days5+days6+days7,'hours in this week')
overall_str=str(overall)
Usage_hours= [days1,days2,days3,days4,days5,days6,days7]
point1 = [days[0], Usage_hours[0]]
point2 = [days[-1], Usage_hours[-1]]
plt.plot(days,Usage_hours,color='black')
plt.axline(point1, point2, color='red', linestyle='--')
plt.title('usge computer per week ')
plt.xlabel('days')
plt.ylabel('Usage Hours')
plt.ylim(0, 24)
plt.show()


