import csv
import sys

with open(sys.argv[1]) as benchmark:
    reader = csv.DictReader(benchmark)
    for row in reader:
        print(row["Date [day]"], end=',')
    print()
