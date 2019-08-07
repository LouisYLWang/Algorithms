import matplotlib.pyplot as plt



file = open('tsp.txt')
lines = file.readlines()
cities = list()

for l in lines[1:]:
    cities.append(l.split())

plt.plot([float(i[0]) for i in cities], [float(i[1]) for i in cities], 'ro')
plt.show()