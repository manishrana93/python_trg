#Variables
marks_1 = int(input("Marks 1: "))
marks_2 = int(input("Marks 2: "))
marks_3 = int(input("Marks 3: "))

#constants
Threshold=33
status= "FAIL"
grade="A"

#Calculations
total = marks_1 + marks_2 + marks_3

avg = total / 3

if marks_1 >=Threshold and marks_2>=Threshold and marks_3>=Threshold:
    status = "PASS" 

if avg>=50 and avg<70:
    grade= "B"
if avg<50:
    grade= "C"
else: 
    grade



print("Total Marks : " + str(total))
print("Percentage: " + str(avg))
print("status : " + status)
print("Grade : " + grade)