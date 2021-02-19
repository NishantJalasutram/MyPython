name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hourDict = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith("From:"): continue
    elif line.startswith("From"):
         time = (((line.split())[5]).split(':'))[0]
         hourDict[time] = hourDict.get(time,0) + 1

# Sorting based on keys

for k,v in sorted(hourDict.items()):
    print(k,v)

# Reverse Sorting based on values
newList = list()
for k,v in hourDict.items():
    newt = (v,k)
    newList.append(newt)

for k,v in sorted(newList,reverse=True):
    print(k,v)
