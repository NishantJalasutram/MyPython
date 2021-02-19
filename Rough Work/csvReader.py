inp1 = inp("enter")
inp2 = inp("enter")

inp1 = int(inp1)
inp2 = int(inp2)

print(inp1*inp2)


import csv

#Reading csv in a list format
fh = open("samplecsv.csv")
lines1 = csv.reader(fh)

#next function will retrieve the first row and move the filepointer to next row
header = next(lines1)

csvList = list()
index = 0
# Doesn't print the header as we have already extracted it above
for row in lines1:
    #print(row,index)
    csvList.append(row)
    index += 1

fh.close()

#Reading csv file in a dictionary format
fh = open("samplecsv.csv")

lines = csv.DictReader(fh)

#for row in lines:
    #print(row)

fh.close()

#Simple way to read csv file

with open('samplecsv.csv') as csvReader:
    csvList2 = list(csv.DictReader(csvReader))

for i in csvList2:
    print(i)
#Writing to a new CSV file
# fh = open("newsamplecsv.csv",'w',newline='')
# writer = csv.writer(fh)
# writer.writerow(header)
#
# for row in csvList:
#     writer.writerow(row)
#
# fh.close()
