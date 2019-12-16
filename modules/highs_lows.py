import csv
import matplotlib.pyplot as plt
from datetime import datetime 
filename = 'data\\sitka_weather_2014.csv'

with open(filename) as f:
    #getting headers
    reader = csv.reader(f)
    header_row = next(reader)
    #getting the high temps with dates
    dates, highs, lows = [], [], []
    for row in reader:
        highs.append(int(row[1]))
        lows.append(int(row[3]))
        dates.append(datetime.strptime(row[0], "%Y-%m-%d"))
    #plotting
    fig = plt.figure(figsize=(10, 6))
    plt.plot(dates, highs, c='red')
    plt.plot(dates, lows, c='blue')
    plt.title("Daily high and low temperatures - 2014", fontsize=14)
    plt.xlabel("Days", fontsize=10)
    plt.ylabel("Temperature(F)", fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=8)
    plt.savefig('visualizations\\sitka_weather_2014_plot.png', bbox_inches='tight')
    plt.show()