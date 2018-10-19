import csv
import pandas

df = pandas.read_csv('AIS_2017_01_Zone01.csv')
print(df)

with open('AIS_2017_01_Zone01.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=' ', quotechar='|')

	for line in csv_reader:
		print(line)