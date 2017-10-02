#import csv to get the functions for csv file 
ASSAULT=0
import csv
#file=open('Crime.csv')
#to calculate total no of assault crime happened in last 7 days
#for 
#print(file.read())
with open('Crime.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['	crime1'])
	if('crime1'== 1):
		'crime1'ASSAULT +=1
	else:
		return a
print("count for ASSAULT:",ASSAULT)
