import csv
with open('albumlist.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    print(reader.fieldnames)
    albums = [row for row in reader]
    
