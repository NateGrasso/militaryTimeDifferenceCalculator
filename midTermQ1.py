#MidTermEssay Question 1
#Nathan Grasso
#CSC 119473
#Description: A program that takes in two different times in military time and prints out the difference
#between the two times in hours and minutes.
####

#Initialize variables.
time1= int(input("Please enter the first time: "))
time2 = int(input("Please enter the second time: "))
difference = 0
hour = 0
minutes = 0

#Setting boundaries for inputs.
if time1 >= 0000 and time1 <= 2359 and time2 >= 0000 and time2 <= 2359:
#Process of converting time into hours and minutes.
    if time1 > time2:
        difference = time1 - time2
        hour = difference // 100
        minutes = difference % 100
        print("Time Difference:", hour, "hours", minutes, "minutes")
    elif time1 < time2:
        difference = time2 - time1
        hour = difference // 100
        minutes = difference % 100
        print("")
        print("Time Difference:", hour, "hours", minutes, "minutes")
    elif time1 == time2:
        print("No time inbetween the two times.")
    else:
        print("Enter a military time.")
else:
    print("Invalid time input: ")


    
    
    
    
