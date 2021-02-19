str="Hello Nishant. How are you doing? "
arr1 = []
index = 0
spaceIndex = 0
for i in str:
    if i == " ":
        print("Words: " + str[spaceIndex:index] + ": End of Word")
        spaceIndex = index + 1
    index = index + 1

if (spaceIndex != index):
    print("Words: " + str[spaceIndex:] + ": End of Word")
