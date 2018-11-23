

# translate python list into CSV file
# python 2
import csv

with open(..., 'wb') as myfile:
	wr = csv.writer(myfile, quoting= csv.QUOTE_ALL)
	wr.writerow(mylist)

'''
1. import csv module
2. create a file, open it
3. create a writer object
4. writerow() method imposed on this writer object
5. write list
'''

# python 3
import csv

# write CSV file 
with open(..., 'w', newline= '') as myfile:
	wr = csv.writer(myfile, quoting= csv.QUOTE_ALL)
	wr.writerow(mylist)

# read CSV file
with open('test.csv', mode, **kwargs) as fp:
	reader = csv.reader(fp, delimiter=',', quotechar = ' " ')
	# next(reader, None)
	data_read = [row for row in reader]

print(data_read)