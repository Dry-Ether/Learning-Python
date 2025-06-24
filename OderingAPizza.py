print("Welcome to DryEther's Pizza")
order=input("Would You Like to Oder a Pizza.Press Y for Yes and N for No \n Enter your Choice:")
bill=0
if order=="Y":
    pizza=int(input("1.Small Pizza= 100 \n 2.Medium Pizza= 200 \n 3.Large Pizza= 300 \n Enter your Choice:"))
    if pizza==1:
        bill+=100
    elif pizza==2:
        bill+=200
    elif pizza==3:
        bill+=300
    else:
        print("Invalid Number")
    add=input("Do you need extra add-ons. Y or N \n Enter your Choice:")
    if add=="Y":
        addons=int(input("1.Peparoni= 30 \n 2.Extra Chess= 20 \n Enter your Choice:"))
        if addons==1:
            bill+=30
        elif addons==2:
            bill+=20
if bill>0:
    print(f"Your Total Bill is:{bill}")
print("Thanks for visiting us. See you again")