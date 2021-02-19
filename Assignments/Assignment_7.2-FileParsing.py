# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File doesn't exist")
    exit()
index = 0
total = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    else:
        index = index + 1
        pos=line.find(":")
        total = total + float(line[pos+1:].lstrip())

avg = total/index
print("Average spam confidence:",avg)
