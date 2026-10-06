marks = int(input("Enter student marks:"))

if(marks >= 90):
    grade = "A+"
elif(marks >= 80 and marks < 90):
    grade = "A"
elif(marks >= 70 and marks< 80):
    grade = "B"
elif(marks >= 40 and marks < 70):
    grade = "C"

else:
    grade ="Fail"

print("Grade of student is: ", grade)