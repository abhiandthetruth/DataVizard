from die import Die
import pygal

#data generation
die_1 = Die()
die_2 = Die(9) 
results = []
for roll_num in range(10000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#data analysis
frequencies = []
max_value = die_1.num_sides + die_2.num_sides
for value in range(2, max_value + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#data visuaization
hist = pygal.Bar()
hist.title = "Results of rolling one D6 and D9 10000 times"
hist.x_labels = [str(x) for x in range(2, max_value+1)]
hist.x_title = "Result"
hist._y_title = "Frequency of Result"
hist.add('D6 + D9', frequencies)
hist.render_to_file('die_visual.svg')
