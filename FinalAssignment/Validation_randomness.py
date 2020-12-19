import matplotlib.pyplot as plt
from FinalAssignment.MersenneTwister import MersenneTwister


"""
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||| In dit script wordt het Mersenne Twister algoritme gevalideerd. |||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
"""


test = MersenneTwister(seed=5489)
print(test.array)

result = []
for x in range(1000000):
    result.append(int(test.get_random_number_0_1() * 100))

plt.hist(result)
plt.gca().set(title='Frequency Histogram', ylabel='Frequency')
plt.show()

print(min(result), max(result))
"""
Er is in het histogram duidelijk te zien dat na duizende keren aanroepen van een random getal
de distributie zo goed als gelijk is, dit is te zien aan de vorm van het histogram: vierkant.
Dit valideerd dat elke integer tussen de 0 en de 100 zo goed als even vaak voorkomen.

"""