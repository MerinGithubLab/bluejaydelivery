import csv
with open('assignment.csv') as csvdata:
	data=csv.reader(csvdata,delimiter=',')
	for row in data:
		print(f"{row[7]}:-{row[1]}")

