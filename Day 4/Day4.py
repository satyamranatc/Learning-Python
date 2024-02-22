
TotalDays = 300
RequiredAttendence = TotalDays * 0.6 # TotalDays 60 / 100
Attendence = 0
MadicalCondition = False

if Attendence >= RequiredAttendence:
    print("Good")
    if Attendence >= TotalDays*0.9:
        print("Promoted")
        if Attendence == TotalDays:
            print("Excellent + Bonus")

else:
    print("Not Good")
    if Attendence < RequiredAttendence * 0.1:
        print("Fired")
        


if MadicalCondition == True and Attendence < RequiredAttendence * 0.5:
    print("Insurrence By Company")














