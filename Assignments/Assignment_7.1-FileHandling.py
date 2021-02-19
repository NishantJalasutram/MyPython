fname=input("Please enter the file name: ")
try:
  fhand=open(fname)
except:
  print("File doesn't exist")
  quit()

for val in fhand:
  print((val.rstrip()).upper())
