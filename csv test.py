import csv

with open('names.csv', 'w') as csvfile:
    fieldnames = ('first_name', 'last_name')
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name' : 'spam'})
 
