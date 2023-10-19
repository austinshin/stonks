# Austin Shin
# This script imports a watchlist of tickers formatted in some weird way
# then exports it into a csv that DAS trader can import it nicely

import pandas as pd

newWL = []

fileName = input("What is the file name?: ")
f = open(fileName, 'r')
print(fileName, " has been imported")

	# algorithm
	# read into the file 
	# separate all words by comma
	# ['NASDAQ:AVGO', 'NASDAQ:GLUE', 'NYSE:CWEN']
	# loop through array
	# remove all the strings before :
	# create a comma delimited text
	# export it into the array


with open(fileName) as f:
	watchlist = f.read()
	wl = watchlist.split(",")

	for i in wl:
		j = i.split(':')
		if len(j) == 2:
			newWL.append(j[1])

print("your watchlist: ", newWL)
print(" ")

df = pd.DataFrame(newWL, columns=["column"])
df.to_csv('watchlist.csv', index=False)

print("your csv has been saved to watchlist.csv")

f.close()
