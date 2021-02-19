import re
fname=input("Enter the file name:")
if(len(fname) <= 1): fname="regex_sum_42.txt"
fhand=open(fname)
tmpLst = list()
for line in fhand:
    line = line.rstrip()
    tmpLst = tmpLst + re.findall('[0-9]+',line)

#print(tmpLst)
finalSum = 0
for val in tmpLst:
    finalSum = finalSum + int(val)

print(finalSum)
