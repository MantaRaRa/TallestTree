import matplotlib.pyplot as plt
import json

dictionary = json.load(open('assest\data.json', 'r'))
xAxis = [key for key, value in dictionary.items()]
yAxis = [value for key, value in dictionary.items()]
plt.grid(True)

## LINE GRAPH ##
plt.plot(xAxis,yAxis, color='green', marker='o')
plt.xlabel('Species of Trees')
plt.ylabel('Tallest Tree')

## BAR GRAPH ##
fig = plt.figure()
plt.bar(xAxis,yAxis, color='maroon')
plt.xlabel('Species of Trees')
plt.ylabel('Tallest Tree')

plt.show()