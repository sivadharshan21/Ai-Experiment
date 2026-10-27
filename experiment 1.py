#student Marks, Percentage and Graade
name=input("Enter student name:")
n=int(input("Enter number of subjects:"))
total=0
for i in range(1,n+1):
    mark=float(input(f"Enter mark for subject{i}:"))
    total+=mark
    percentage=total/n
    if percentage >= 90:
        grade="A+"
        performance = "outstanding"
    elif percentage>=80:
        grade="A"
        performance="Excellent"
    elif percentage>=70:
        grade="B"
        performance="Very good"
    elif percentage>=60:
        grade="c"
        performance="good"
    elif percentage>=50:
        grade="D"
        performance="Average"
    else:
        grade="F"
        performance="Need improvement"

print("\n --Academic Performance--")
print("Student name:",name)
print("Total Marks:",total)
print("Percetage:",round(percentage,2),"%")
print("Grade:",grade)
print("Performance:",performance)
