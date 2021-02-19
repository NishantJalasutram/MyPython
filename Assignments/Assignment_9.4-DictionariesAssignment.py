name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mailIds = dict()
lineList = list()
count = 0
for line in handle:
    line = line.rstrip()
    if line.startswith("From:"): continue
    elif line.startswith("From"):
        # Split the entire line with " " and store 2nd value in mailId field
        # Update dictionary with mail Id as the key and the count of occurrence as the value
        # get function eliminates the risk of traceback when the key is not found
        lineList = line.split()
        mailId = lineList[1]
        mailIds[mailId] = mailIds.get(mailId,0) + 1

maxVal = 0
maxKey = ""
for key in mailIds:
    if mailIds[key] > maxVal:
        maxKey = key
        maxVal = mailIds[key]

print(maxKey,maxVal)
