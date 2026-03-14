
#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
header = next(reader)

for row in reader:
    try:
        region = row[5]
        product = row[9]
        purchase = float(row[8])

        key = region + "_" + product
        print(f"{key}\t{purchase}")

    except:
        continue