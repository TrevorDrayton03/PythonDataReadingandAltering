import random
import matplotlib.pyplot as plt
import numpy as np

ran_data = open("randomdata.txt", "w+")
for i in range(5000) :
    value = random.randrange(51)
    ran_data.write(str(value) + " ")

ran_data = open("randomdata.txt")

numbers = dict()
data_reading = ran_data.read()
data_reading = data_reading.split()

for values in data_reading :
    if values not in numbers :
        numbers[values] = 1
    else :
        numbers[values] = numbers[values] + 1

plt.bar(sorted(numbers.keys()), numbers.values())
plt.xlabel('Numbers')
plt.ylabel('Count')
plt.show()

