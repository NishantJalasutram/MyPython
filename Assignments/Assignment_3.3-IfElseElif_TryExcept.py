score = input("Enter Score: ")
# Catch an exception if user enters a non-int input
try:
	score = float(score)
except:
    print ("Invalid input for score")

# Defaulting grade to NA
grade = "NA"

# If block with multiple conditions

if (score > 1.0):
    grade = "NA"
elif (score >= 0.9):
	grade = "A"
elif (score >=0.8):
    grade = "B"
elif (score >=0.7):
    grade = "C"
elif (score >=0.6):
    grade = "D"
elif (score <0.0):
    grade = "NA"
else:
    grade = "F"

if (grade == "NA"):
    print("Invalid input for score")
else:
    print(grade)
