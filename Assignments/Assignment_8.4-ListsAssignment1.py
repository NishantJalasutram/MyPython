fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File doesn't exist")
    exit()
lst = list()
for line in fh:
    line = line.rstrip()
    for words in line.split():
        if words not in lst:
            lst.append(words)
lst.sort()
print(lst)
