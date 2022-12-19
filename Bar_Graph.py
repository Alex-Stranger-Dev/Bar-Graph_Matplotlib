#Bar Graph using Matplotlib Python
import matplotlib.pyplot as pyplot
import numpy as np

#Set up the data
labels = ('Python', 'Scala', 'C#', 'Java', 'PHP')
index = (1, 2, 3, 4, 5) #provides locations on x axis
sizes = [45, 10, 15, 30, 22]
#Set up the bar chart
pyplot.bar(index, sizes, tick_label = labels)

#Configure the layout
pyplot.ylabel('Usage')
pyplot.xlabel('Programming languages')
#Display the chart
pyplot.show()

