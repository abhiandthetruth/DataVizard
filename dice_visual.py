from die import Die
import pygal

#data generation
die = Die()
results = []
for roll_num in range(10000):
    result = die.roll()
    results.append(result)

#data analysis
frequencies = []
for value in range(1, die.num_sides +1):
    frequency = results.count(value)
    frequencies.append(frequency)

#data visuaization
hist = pygal.Bar()
hist.title = "Results of rolling one D6 10000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist._y_title = "Frequency of Result"
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
