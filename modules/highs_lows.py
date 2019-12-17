import csv
import matplotlib.pyplot as plt
from datetime import datetime 

filename = 'death_valley_2014.csv'

fullfilename = 'data\\' + filename

with open(fullfilename) as f:
    #getting headers
    reader = csv.reader(f)
    header_row = next(reader)
    #getting the high temps with dates
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3]) 
        except ValueError:
            print(date, 'missing data')
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)
    #plotting
    fig = plt.figure(figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    plt.title("Daily high and low temperatures - 2014", fontsize=14)
    plt.xlabel("Days", fontsize=10)
    fig.autofmt_xdate()
    plt.ylabel("Temperature(F)", fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=8)
    plt.savefig('visualizations\\'+filename.split(".")[0]+'_plot.png', bbox_inches='tight')
    plt.show()