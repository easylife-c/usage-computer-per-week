import matplotlib.pyplot as plt

num_days = int(input("Enter the number of days you want to track: "))

days = []
usage_hours = []

for i in range(1, num_days +1):
    day_name = f"Day {i}"
    hours_used = float(input(f"Enter hours used on {day_name}: "))
    days.append(day_name)
    usage_hours.append(hours_used)

overall_usage = sum(usage_hours)
overall = f'You used the computer for {overall_usage} hours this week'

plt.plot(days, usage_hours, marker='o', color='black', linestyle='-', linewidth=2, markersize=8)
plt.title('Computer Usage per Week')
plt.xlabel('Days')
plt.ylabel('Usage Hours')
plt.ylim(0, 24)

# Annotate overall usage
plt.annotate(overall, xy=(0.5, 0), xycoords='axes fraction', ha='center', fontsize=10, color='blu

plt.grid(True)
plt.show()
