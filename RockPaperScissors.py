import random
user_choice=int(input("0 for Rock\n1 for Paper\n2 for Scissors\nEnter Your Choice:"))
if user_choice==0:
    print("Your Choice: 🪨")
elif user_choice==1:
    print("Your Choice: 📜")
elif user_choice==2:
    print("Your Choice: ✂")

if 0<= user_choice<=2:
    com_choice=random.randint(0,2)
    if com_choice==0:
        print("Computer Choice: 🪨")
    elif com_choice==1:
        print("Computer Choice: 📜")
    elif com_choice==2:
        print("Computer Choice: ✂")

    if user_choice==com_choice:
        print("Draw")
    elif user_choice==1 and com_choice==0:
        print("You Loss")
    elif user_choice==2 and com_choice==0:
        print("You Loss")
    elif user_choice==2 and com_choice==1:
        print("You Loss")
    elif user_choice>com_choice:
        print("You Win")
    elif com_choice>user_choice:
        print("You Loss")
else:
    print("Invalid Number.You Loss")