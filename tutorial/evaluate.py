import sys
import csv
import math

numParameters = int(sys.argv[3])

with open(sys.argv[2]) as model:
    reader = csv.DictReader(model)
    modeledData = [float(s["Modeled data"]) for s in reader]

with open(sys.argv[1]) as benchmark:
    reader = csv.DictReader(benchmark)
    benchmarkData = [float(s["Value"]) for s in reader]

n = len(modeledData)
rss = sum([(x - y) ** 2 for x, y in zip(modeledData, benchmarkData)])

print(2 * numParameters + n * math.log(rss / n, math.e))
