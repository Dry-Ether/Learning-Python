height=float(input("Enter your height:"))
if height>3:
    print("You can ride")
    age=int(input("Enter your age:"))
    if age<12:
        print("Pay 150 Taka")
    elif 12<=age<=18: #for multiple conditions
        print("Pay 250 Taka")
    else:
        print("Pay 500 Taka")
else:
    print("You can't ride")
print("Bye")