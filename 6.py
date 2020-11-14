from sys import argv
from itertools import count, cycle, islice

for x in islice(cycle(islice(count(int(argv[1])), 5)), 20):
    print(x)
