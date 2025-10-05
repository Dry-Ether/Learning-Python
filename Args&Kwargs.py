def multiply(*numbers):
    c=1
    for i in numbers:
        c=c*i
    print(f"The result of the multiplication is: {c}")
    return 0
multiply(2,3,-6,8)
multiply(2,5,8,9,0,6)